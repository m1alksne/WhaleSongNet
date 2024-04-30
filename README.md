# WhaleSongNet: Blue Whale Song Classifier

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green)

![Blue whale fluking](https://github.com/m1alksne/WhaleSongNet/blob/main/reports/figures/blue_whale_CalCOFI.JPG)
Blue whale off the coast of San Diego

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
    │   │                 predictions
    │   ├── predict.py
    │   └── train.py
    │
    └── visualization  <- Scripts to create exploratory and results oriented visualizations
        └── visualize.py
```

## Setup

1. Clone the Repository:

	```git clone  https://github.com/m1alksne/WhaleSongNet.git```
	```cd WhaleSongNet```

2. (optional) Create a Virtual Environment:
	```conda create -n whalesongnet pyhton=3.8```

	```conda activate whalesongnet```

3. Install Dependencies:

	```conda install --file requirements.txt```

4. Download Data:

*note, this will take a while! The raw .WAV files are available on [figshare](https://figshare.com/articles/dataset/Low-frequency_HARP_recordings_from_Southern_California_Bight/25433875)

	```python src/data/download_data.py```

