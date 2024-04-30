# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 11:20:28 2024

@author: Michaela Alksne 

"""

from datetime import datetime
import numpy as np
from extract_xwav_header import extract_wav_start
from pathlib import Path

def modify_annotations(df, file_path):
    
    """
    helper function to modify the original logger files to new format
    # replaces xwav file path and converts start and end time to seconds since start of xwav file.
    First function to run when modifying Triton logger annotation excel datasheets
    converts xls to csv containing the audio file path, the annotation label, the frequency bounds, and time bounds. 
    xwav is the audio file
    start time = start time of call in number of seconds since start of xwav 
    end time = end time of call in number of seconds since start of xwav
    
    """
    # this should work between Windows and Linux and Mac:
    df['audio_file'] = df['Input file'].apply(lambda x: file_path / Path(x).name)

    #df['audio_file'] = df['Input file'].apply(lambda x: new_base_path + x.split('\\')[-1])

    df['file_datetime'] = df['audio_file'].apply(extract_wav_start)  # uses .apply to apply extract_wav_start time from each wav file in the list
    df['start_time'] = (df['Start time'] - df['file_datetime']).dt.total_seconds()  # convert start time difference to total seconds
    df['end_time'] = (df['End time'] - df['file_datetime']).dt.total_seconds()  # convert end time difference to total seconds
    df['annotation'] = df['Call']
    df['high_f'] = df['Parameter 1']
    df['low_f'] = df['Parameter 2']
    df = df.loc[:, ['audio_file', 'annotation', 'high_f', 'low_f', 'start_time','end_time']]  # subset all rows by certain column name
    return df

