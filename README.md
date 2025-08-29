# Face-Sticker-Blur-with-Snapshot-Capture
This project detects faces in real-time using OpenCV, applies a smooth blurred sticker effect with a cute background on each detected face, displays the face count, and allows snapshot saving with 's'. It offers a visually appealing, privacy-friendly video experience from webcam input.
Face Sticker Blur with Snapshot Capture
Overview
This project is a real-time face detection and processing application built with Python and OpenCV. It captures video from the webcam, detects faces in each frame, and applies a visually appealing blurred "sticker" effect on the detected faces. Additionally, it displays the number of faces detected and provides a feature to save snapshots of the current frame with stickers applied.

Features
Real-time Face Detection: Uses OpenCV’s Haar Cascade classifier for dynamic frontal face detection from the webcam feed.

Blurred Sticker Effect: Extracts each detected face, resizes it to a smaller size, and applies a smooth Gaussian blur to create an aesthetic enhancement.

Sticker Overlay with Background: Blurred face stickers are placed on the video frames with a semi-transparent white rounded rectangle background, delivering a polished and cute visual style.

Face Count Display: Shows the live count of detected faces on the top-left corner of the frame.

Snapshot Saving: Press s to capture and save the current frame with stickers applied for sharing or record-keeping.

Graceful Exit: Press the Down Arrow key (↓) to exit the video stream and cleanly close all windows.

How It Works
Loads the Haar Cascade XML classifier for frontal face recognition.

Captures video frames from the webcam continuously.

For each frame:

Converts to grayscale for efficient face detection.

Detects faces using detectMultiScale.

Extracts, resizes, and applies Gaussian blur to each face region to create a sticker.

Adds a cute rounded rectangle background behind each sticker for smoothness.

Displays the total live face count on the frame.

Outputs the processed frame in a display window.

Listens for keyboard inputs:

s to save a snapshot.

Down Arrow (↓) to exit the program.

Installation & Usage
Install dependencies:

bash
pip install opencv-python numpy
Download the haarcascade_frontalface_default.xml file from the official OpenCV repository.

Place the XML file in the same directory as the script.

Run the script with:

bash
python face_sticker_blur.py
Ensure a webcam is connected and accessible.

Customization Tips
Modify sticker_width and Gaussian blur parameters to change sticker size and blur intensity.

Customize the sticker background color or transparency by adjusting the rectangle and alpha blending code.

Add different types of stickers or effects for more creative overlays.

Keyboard Controls
s : Save snapshot of the current frame with stickers.

Down Arrow (↓) : Exit the application cleanly.

Dependencies
OpenCV (cv2)

NumPy (numpy)

License
This project is open-source and free to use for educational and personal purposes.

This project offers a fun and visually pleasing way to anonymize faces in webcam video streams by applying custom blurred stickers while enabling seamless snapshot capturing. It is perfect for privacy-aware live streaming, creative video processing, or computer vision learning experiments.
