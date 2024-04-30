# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 11:18:26 2024

@author: Michaela Alksne

Script to make train, validation, and test datasets. 
First we decide how to split up the data we have available: 
    -Training dataset: used to fit the model to the audio data
    -Validation dataset: used to evaluate model preformance and tune hyper-parameters 
    -Test dataset: used after the model has completed training to evaluate model preformance on unseen/novel data. Best to have this data represent a new "domain" 
    
In this example, we have two annotated datasets: DCPP01A and CINMS18B
    - Here we split DCPP01A into train and validation based on the distribution of calls in each xwav file
    - CINMS18B is used for testing 
    
Next, we balance each of our datasets. This is especially important for our training dataset to avoid biases, improve generalization, and reduce overfitting. 
    - We include 1500 examples from each class for our training dataset
    - We also make sure to include 1500 examples that do not contain either class to improve discrimination between target and non-target images or patterns
    
Lastly, we save our newly created train, validation, and test clips for the next step (which is training the model!)

"""

import opensoundscape
import glob
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
import librosa
import torch
import random
from pathlib import Path


print("Current working directory:", os.getcwd()) # print working directory. 

# read in datasets

DCPP01A = pd.read_csv('../../data/interim/DCPP01A_logs_hot_clips.csv')
CINMS18B = pd.read_csv('../../data/interim/CINMS18B_logs_hot_clips.csv')
save_path = Path("../../data/processed")

# Filter rows for training set where 'audio_file' column does not equal 'DCPP01A_d01_121106_083945.d100.x.wav'
train_clips = DCPP01A[~DCPP01A['file'].str.contains('DCPP01A_d01_121106_083945.d100.x.wav')]
# Filter rows for validation set where 'audio_file' column contains 'DCPP01A_d01_121106_083945.d100.x.wav'
val_clips = DCPP01A[DCPP01A['file'].str.contains('DCPP01A_d01_121106_083945.d100.x.wav')]

test_clips = CINMS18B

#print counts of all the calls from train, val, and test

print("Training A call counts:", train_clips['A NE Pacific'].value_counts(), 
      "Training B call counts:", train_clips['B NE Pacific'].value_counts())

print("Validation A call counts:", val_clips['A NE Pacific'].value_counts(), 
      "Valitation B call counts:", val_clips['B NE Pacific'].value_counts())

print("Test A call counts:", test_clips['A NE Pacific'].value_counts(), 
      "Test B call counts:", test_clips['B NE Pacific'].value_counts())

#now balance the training dataset: 33% A, 33% B, 33% empty
train_clips.set_index(['file', 'start_time', 'end_time'], inplace=True) #first reset the index 
balanced_train_clips = opensoundscape.data_selection.resample(train_clips,n_samples_per_class=1500,random_state=0) # upsample (repeat samples) so that all classes have 1500 samples
print(balanced_train_clips.sum())
train_clips_new = train_clips.reset_index(drop=True) # drop index to allow for indexing in next line
noise_indices = train_clips_new.index[(train_clips['A NE Pacific'] == 0) & (train_clips['B NE Pacific'] == 0)]# indices of negatives (times when there are no calls)
random_noise_indices = random.sample(noise_indices.tolist(), 1500) # random sample subset of the empty examples
train_clips_noise = train_clips.iloc[random_noise_indices] # subset by these indices
train_clips_final = pd.concat([balanced_train_clips, train_clips_noise]) # concatenate dataframes
print(train_clips_final.head())
print("Training A call counts balanced:", train_clips_final['A NE Pacific'].value_counts(), 
      "Training B call balanced:", train_clips_final['B NE Pacific'].value_counts())
train_clips_final.to_csv(save_path / "train.csv", index=True)


#Do the same thing for validation (but with less examples): 33% A, 33% B, 33% empty
val_clips.set_index(['file', 'start_time', 'end_time'], inplace=True) #first reset the index 
balanced_val_clips = opensoundscape.data_selection.resample(val_clips,n_samples_per_class=300,random_state=0) # upsample (repeat samples) so that all classes have 1500 samples
print(balanced_val_clips.sum())
val_clips_new = val_clips.reset_index(drop=True) # drop index to allow for indexing in next line
noise_indices = val_clips_new.index[(val_clips['A NE Pacific'] == 0) & (val_clips['B NE Pacific'] == 0)]# indices of negatives (times when there are no calls)
random_noise_indices = random.sample(noise_indices.tolist(), 1500) # random sample subset of the empty examples
val_clips_noise = val_clips.iloc[random_noise_indices] # subset by these indices
val_clips_final = pd.concat([balanced_val_clips, val_clips_noise]) # concatenate dataframes
print(val_clips_final.head())
print("Training A call counts balanced:", val_clips_final['A NE Pacific'].value_counts(), 
      "Training B call balanced:", val_clips_final['B NE Pacific'].value_counts())
val_clips_final.to_csv(save_path / "validation.csv",index=True)

# We'll run the model on a subset of the test data 

# Filter the data where either 'A NE Pacific' or 'B NE Pacific' is 1
filtered_test = test_clips[(test_clips['A NE Pacific'] == 1) | (test_clips['B NE Pacific'] == 1)]
print(filtered_test.head())
noise_indices = test_clips.index[(test_clips['A NE Pacific'] == 0) & (test_clips['B NE Pacific'] == 0)]
random_noise_indices = random.sample(noise_indices.tolist(), 500) # random sample subset of the empty examples
test_clips_noise = test_clips.iloc[random_noise_indices] # subset by these indices
test_clips_final = pd.concat([filtered_test, test_clips_noise]) # concatenate dataframes
test_clips_final.to_csv(save_path / "test.csv", index=False)
        
        
