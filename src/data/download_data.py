# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 09:56:52 2024

@author: Michaela Alksne

download wav files from figshare

"""

import requests
import os

print("Current working directory:", os.getcwd()) # print working directory. 
# should be running from WhaleSongNet directory 

# Define the directory where you want to download the files
base_dir = 'data/raw' 

# Ensure the directory exists, if not create it
os.makedirs(base_dir, exist_ok=True)

# Figshare article URL
article_url = "https://api.figshare.com/v2/articles/25433875"

# Send a GET request to the Figshare API to get article details
response = requests.get(article_url)
article_details = response.json()

# Extract and print file information
files_info = article_details.get('files', [])

for file in files_info:
    file_url = file['download_url']
    file_name = file['name']
    print(f"Downloading: {file_name}, URL: {file_url}")

    # Send a GET request to the file URL
    response = requests.get(file_url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open a file in binary write mode in the specified directory
        full_path = os.path.join(base_dir, file_name).replace("\\", "/")  # Combine base directory with file name
        with open(full_path, 'wb') as file:
            file.write(response.content)
        print("File downloaded successfully!")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
        
        
        
        
        
        
        
        
        
        
        