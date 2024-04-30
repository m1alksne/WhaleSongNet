# WhaleSongNet: Blue Whale Song Classifier

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green)

![Blue whale fluking](https://github.com/m1alksne/WhaleSongNet/blob/main/reports/figures/blue_whale_CalCOFI.JPG)
Blue whale off the coast of San Diego.

Photo credit: Katherine Whitaker

## Overview

This repository details how to train, validate, and test a ResNet-18 CNN to classify blue whale A and B calls in 30 second spectrogram windows. The opensource Python package, [opensoundscape](https://opensoundscape.org/en/latest/), is used for preprocessing and model training. The model is trained on publicly available acoustic data from the [DCLDE 2015 Workshop](https://www.cetus.ucsd.edu/dclde/). 

## Central and Southern California High Frequency Acoustic Recording Package (HARP) locations:
![Southern California High Frequency Acoustic Recording Package (HARP) locations](https://github.com/m1alksne/WhaleSongNet/blob/main/reports/figures/site_map.jpg)

## WhaleSongNet Directory Structure:
```
WhaleSongNet/
├── LICENSE
├── README.md          <- The top-level README for users.
├── data
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical train, validation, and test data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── models             <- Trained models
│
├── notebooks          <- Jupyter notebooks. 
│   └── plot_spectrograms
|	└── plot_spectrograms.ipynb
| 
├── references         <- Relevant literature.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `conda list --export > requirements.txt`
│
├── src                <- Source code for use in this project.
    ├── __init__.py    <- Makes src a Python module
    │
    ├── data           <- Scripts to download or generate data
    │   └── AudioStreamDescriptor.py 
    |	└── download_data.py	
    |	└── extract_xwav_header.py
    |	└── make_dataset.py
    |	└── make_hot_clips.py
    |	└── modify_annotations.py
    │
    ├── models         <- Scripts to train models and then use trained models to make
        │                 predictions
        ├── predict.py
        └── train.py
   
```

## Setup

1. Clone the Repository:

	```git clone  https://github.com/m1alksne/WhaleSongNet.git```

	```cd WhaleSongNet```

2. (optional) Create a Virtual Environment:

	```conda create -n whalesongnet python=3.8```

	```conda activate whalesongnet```

3. Install Dependencies:

	```conda install --file requirements.txt```

## Prepare the Data

4. Download Data:

	*note, this will take a while! The raw .WAV files are available on [figshare](https://figshare.com/articles/dataset/Low-frequency_HARP_recordings_from_Southern_California_Bight/25433875)


	```python src/data/download_data.py```

5. Preprocess the Data:

	a. ```python src/data/make_hotclips.py```

	b. ```python src/data/make_dataset.py```

## Train and Test the Model:

6. Train the Model:

	```python src/models/train.py```

7. Evaluate Model Performance:

	```python src/models/evaluate_model.py```

8. Make Predictions:

	```python src/models/predict.py```

## User information 

The training, validation, and testing clips are already included along with each epoch of the model. Depending on the use-case, step 5-6 may not be necessary. The trained model and the surrounding data processing and evaluation workflows are meant to be used for educational purposes. This workflow is flexible and model hyper-parameters are easy to fine-tune (in the train.py script). The overall workflow can also be modified to retrain the model on a different acoustic dataset, which has implications for broadening the scope of computer vision accessibility to the bioacousitcs community!

To visualize labeled spectrograms:

```jupyter notebook notebook/plot_spectrograms/plot_spectrogram.ipynb```

![spec](https://github.com/m1alksne/WhaleSongNet/blob/main/reports/figures/spectrogram_74_DCPP01A_d01_121109_191242.d100.x.png)
![spec](https://github.com/m1alksne/WhaleSongNet/blob/main/reports/figures/spectrogram_84_DCPP01A_d01_121112_122652.d100.x.png)

## Acknowledgements:

This work was made possible with the support of the [Resnick Sustainability Institute](https://resnick.caltech.edu/), the [Computer Vision for Ecology summer workshop](https://cv4ecology.caltech.edu/), the [National Defense and Graduate Engineering Fellowship](https://ndseg.org/), the [Kitzes Lab](https://github.com/kitzeslab), and the [Scripps Acoustic Ecology Lab](https://sael.ucsd.edu/)