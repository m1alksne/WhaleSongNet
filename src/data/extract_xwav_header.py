# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 11:12:40 2024

@author: Michaela Alksne

helper function to extract xwav file header name
"""

from AudioStreamDescriptor import XWAVhdr


# hepler function uses XWAVhdr to read xwav file header info and extract xwav file start time as a datetime object
def extract_wav_start(path):
    xwav_hdr = XWAVhdr(path)
    xwav_start_time = xwav_hdr.dtimeStart
    return xwav_start_time
