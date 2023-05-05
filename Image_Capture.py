'''

This project is intended for security purposes by automatically capturing an image upon login.
It will take an image with both the normal and IR webcam built into the device. (Mileage may vary if the device does not have Windows Hello hardware.)
It uses external libraries such as OpenCV and datetime as the foundation of the program.

Author: Nand Patel
Date: May 4, 2023
Current Version: v1.2

HISTORY:
v1.0 - Developed function to test image output.
v1.1 - Normal webcam image now successfully saves to local storage.
v1.11 - Image filename now reflects the date and time it was taken on.
v1.2 - Script successfully autoruns upon login after appropiate filepath positioning.
v1.3 - Both (IR and normal) webcams now take pictures and save to local storage. (IN DEVELOPMENT)

Note: The IR camera can not be accessed individually in Windows because it uses the same driver as the normal webcam. 
      However, it is possible to access them separately in Linux (Ubuntu is a good example.) The current solution seems to be to run this script in Linux with a few modifications.

A future plan to improve this program is to use OpenCV for AI-powered face recognition to keep a record of how many times a certain user logged in.

'''

import cv2 # Importing OpenCV library for webcam access

from datetime import datetime # Importing datetime library to access system date for file naming purposes
  
# To be used for testing and debugging purposes only. Displays the captured image in a pop-up window.
def test_output(captured_image):
    
    # Creates a window with the captured image.
    cv2.imshow("PRESS ANY KEY TO EXIT THIS WINDOW", captured_image)

    # Indefinitely scans for key input and closes the window upon detection.
    cv2.waitKey(0)
    cv2.destroyWindow("PRESS ANY KEY TO EXIT THIS WINDOW")

# This variable will store the system date and time.
system_time = datetime.now() 

# Webcam selection can be adjusted by changing argument to a different integer.
device_cam = cv2.VideoCapture(0)
  
# Reading the input from the webcam
frame, image = device_cam.read()
  
# If the image capture is successful, save to local storage.
if frame:

    # Saving image in local storage
    cv2.imwrite(f"C://Users//Nand//Downloads//{system_time.date()}.png", image)
  
else:
    print("No image detected. Please check if the webcam is working.")