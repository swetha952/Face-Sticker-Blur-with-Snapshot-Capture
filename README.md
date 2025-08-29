# Face-Sticker-Blur-with-Snapshot-Capture
This project detects faces in real-time using OpenCV, applies a smooth blurred sticker effect with a cute background on each detected face, displays the face count, and allows snapshot saving with 's'. It offers a visually appealing, privacy-friendly video experience from webcam input.
Face Sticker Blur with Snapshot Capture
Overview
This project is a real-time face detection and processing application using OpenCV in Python. It captures video feed from the webcam, detects faces in each frame, and applies a visually appealing blurred "sticker" effect on detected faces. Additionally, it displays a count of faces detected and offers a feature to save snapshots of the current frame with stickers applied.

Features
Real-time face detection: Utilizes OpenCV’s Haar Cascade classifier to detect frontal faces dynamically from webcam feed.

Blurred sticker effect: Extracts each detected face region, resizes it to a smaller sticker size, and applies a smooth Gaussian blur for aesthetic enhancement.

Sticker overlay with background: Places blurred face stickers onto the video frame with a semi-transparent white rounded rectangle background, creating a cute and polished look.

Face count display: Shows the number of faces detected on the top-left of the video frame, updating in real time.

Snapshot saving: Press ‘s’ to capture and save the current frame with stickers as an image file for quick sharing or record-keeping.

Graceful exit: Press the down arrow key (key code 40) to exit the video stream and close all windows cleanly.

How It Works
The script loads the Haar Cascade XML classifier for frontal face recognition.

It captures webcam video feed frame-by-frame.

In each frame:

Converts the frame to grayscale for face detection.

Detects faces using detectMultiScale.

For each face, extracts the face region, resizes it, applies Gaussian blur, and overlays it as a sticker on the frame.

Adds a rounded rectangle background for each sticker for a cute and smooth appearance.

Displays the total face count.

Outputs the processed frame live in a window.

Listens for keyboard inputs:

Save snapshot on pressing ‘s’.

Exit on pressing the down arrow key.

Installation & Usage
Install required package:

bash
pip install opencv-python numpy
Download haarcascade_frontalface_default.xml from the OpenCV GitHub or official repository.

Place the XML file in the same directory as the script.

Run the script:

bash
python face_sticker_blur.py
Make sure a webcam is connected and accessible.

Customization Tips
Adjust sticker size or blur intensity by modifying sticker_width and Gaussian blur parameters.

Change the background color or transparency by editing the rectangle drawing and alpha blending sections.

Integrate different types of stickers or effects for creative face overlays.

Keyboard Controls
s : Save the current frame snapshot with stickers.

Down arrow (↓) : Exit the application.

Dependencies
OpenCV (cv2)

NumPy (numpy)

License
This project is open-source and free to use for educational and personal projects.

This project offers a fun and visually pleasing way to anonymize faces in webcam video streams with custom blurred stickers while also enabling snapshot capturing seamlessly. Perfect for privacy-aware live streaming or creative video processing experiments.
