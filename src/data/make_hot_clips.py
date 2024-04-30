# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 11:18:26 2024

@author: Michaela Alksne

make_hot_clips:
    
    This script converts the original annotation files to binary hot_clips, which are 30 second clips
    spanning the whole wav file where A and B calls are encoded as 1's or 0's if they are present or
    absent in that time clip. 
    
    We read in our annotations and generate "one_hot_clips" for our audio files
    - each row represents a single sample, in our case, a 30 second audio clip
    - the first column "file" contains the path to our audio file. 
    - The second column "start_time" contains the start time of the audio clip, in seconds since the start of the xwav
    - The third column "end_time" contains the end time of the audio clip, in seconds since the start of the xwav 
    - The next columns represent the possible classes: "A NE Pacific", "B NE Pacific"
    - A "0" means that in that sample, the class is not present
    - A "1" means that in that sample, the class is present

"""

from datetime import datetime
import os
import glob
import opensoundscape
import random
import pandas as pd
import numpy as np
from pathlib import Path
from modify_annotations import modify_annotations

print("Current working directory:", os.getcwd()) # print working directory. 

directory_path = "../../data/raw/*.xls" # point to original logger files
save_path = "../../data/interim"
all_files = glob.glob(directory_path) # path for all .xls files
wav_dir = "../../data/raw/"
# Define the directories using Path for OS independence
print("logger annotations directory:", all_files)
print("WAV files directory:", wav_dir)

    
# 'DCPP01A_d01_121106_083945.d100.x.wav' is missing a chunk of data between these bounds:
date1 = datetime(2012, 11, 6, 8, 41, 11)
date2 = datetime(2012, 11, 7, 2, 0, 0)
# Calculate the difference in seconds
seconds_difference = (date2 - date1).total_seconds()

# loop through all annotation files, make hot_clips, and save to subfolder
for file in all_files:
    data = pd.read_excel(file)
    filename = os.path.basename(file) # get the filename 
    new_filename = filename.replace('.xls', '_hot_clips.csv') # replace with csv
    save_name = Path(save_path) / f'{new_filename}'
    print("save_path_location:", save_name)
    # DCPP01A_d01_121106_083945.d100.x.wav, subtract number of seconds for accurate time windows
    if any(data['Input file'].str.contains('DCPP01A_d01_121106_083945.d100.x.wav')):

        mask = data['Input file'].str.contains('DCPP01A_d01_121106_083945.d100.x.wav')
        subset_df = modify_annotations(data, Path(wav_dir))
        print("modified annotations:", subset_df.head())
        
        subset_df.loc[mask, 'start_time'] -= seconds_difference
        subset_df.loc[mask, 'end_time'] -= seconds_difference
        subset_df.reset_index(drop=True)
    else: 
        subset_df = modify_annotations(data, Path(wav_dir))
        subset_df.reset_index(drop=True)
        print("modified annotations:", subset_df.head())
        
    boxed = opensoundscape.BoxedAnnotations(subset_df)
        
    clips = boxed.one_hot_clip_labels(clip_duration=30, clip_overlap=10, min_label_overlap=5, 
                                      class_subset=['A NE Pacific', 'B NE Pacific']) # make hotclips
    print("hot_clips:", clips.head())
    print(save_name)
    clips.to_csv(save_name, index=True)
    
        
        
        
        
        
        

