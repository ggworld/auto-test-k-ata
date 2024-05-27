from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pydub import AudioSegment
import simpleaudio as sa
import time
import os

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the Rev Online Voice Recorder page
driver.get("https://www.rev.com/onlinevoicerecorder")

# Wait for the page to load completely and the necessary elements to be available
wait = WebDriverWait(driver, 30)

# Start the recording
record_button = wait.until(EC.element_to_be_clickable((By.ID, 'record-button')))
record_button.click()

# Wait for the recording interface to be ready
time.sleep(5)  # Adjust as needed based on the page load time

# Play the audio file using Python's pydub and simpleaudio libraries
# Replace 'your_audio_file_path.mp3' with the path to your audio file
audio_file_path = 'vrec1.mp3'

# Load and play the audio file
audio = AudioSegment.from_mp3(audio_file_path)
play_obj = sa.play_buffer(audio.raw_data, num_channels=audio.channels, bytes_per_sample=audio.sample_width, sample_rate=audio.frame_rate)

# Wait for the audio file to finish playing
play_obj.wait_done()

# Stop the recording
stop_button = wait.until(EC.element_to_be_clickable((By.ID, 'pause-button')))
stop_button.click()

preview_button = wait.until(EC.element_to_be_clickable((By.ID, 'preview-button')))
preview_button.click()

# Download the recording
download_button = wait.until(EC.element_to_be_clickable((By.ID, 'download-icon-desktop')))
download_button.click()

# Wait for the download to complete
time.sleep(10)  # Adjust as needed based on the download time

# Close the browser
driver.quit()
