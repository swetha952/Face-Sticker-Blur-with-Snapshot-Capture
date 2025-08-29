# Face-Sticker-Blur-with-Snapshot-Capture
This project detects faces in real-time using OpenCV, applies a smooth blurred sticker effect with a cute background on each detected face, displays the face count, and allows snapshot saving with 's'. It offers a visually appealing, privacy-friendly video experience from webcam input.


***

# 🎭 Face Sticker Blur with Snapshot Capture 📸

## 🚀 Overview  
This project is a **real-time face detection and processing application** built with **Python** and **OpenCV**. It captures webcam video, **detects faces** on the fly, and adds a stylish **blurred “sticker” effect** on each detected face. You also get a **live face count** display 🧑‍🤝‍🧑 and a handy feature to **save snapshots** of your video with the stickers applied!

***

## ✨ Features

- 🔍 **Real-time Face Detection:** Uses OpenCV’s powerful **Haar Cascade classifier** for dynamic face recognition from your webcam.  
- 🎨 **Blurred Sticker Effect:** Extracts detected faces, resizes them, and applies a smooth **Gaussian blur** for a polished, soft-blur “sticker.”  
- 🖼️ **Sticker Overlay with Background:** Blurred face stickers come with a **semi-transparent white rounded rectangle** background, adding a cute and clean look.  
- 👥 **Face Count Display:** Shows the **number of faces** detected live on the top-left of the video.  
- 💾 **Snapshot Saving:** Press **`s`** to quickly capture and save snapshots of your video with stickers!  
- 🚪 **Graceful Exit:** Press the **Down Arrow key (↓)** anytime to quit the application cleanly.

***

## ⚙️ How It Works

1. The script loads the **Haar Cascade XML classifier** for detecting frontal faces.  
2. Continuously grabs frames from your webcam.  
3. For each frame:  
   - Converts it to **grayscale** to speed up face detection.  
   - Detects faces using OpenCV’s `detectMultiScale`.  
   - Extracts and resizes each face, then applies a **Gaussian blur** to create a soft sticker.  
   - Adds a **cute rounded rectangle background** behind each sticker for style.  
   - Displays the **live face count** on the frame.  
4. Renders the processed video in a window.  
5. Listens for keypresses:  
   - **`s`** to save a snapshot 📷.  
   - **Down Arrow (↓)** to exit the app ✋.

***

## 🛠️ Installation & Usage

1. Install the required libraries:  
   ```bash
   pip install opencv-python numpy
   ```
2. Download **`haarcascade_frontalface_default.xml`** from OpenCV’s official repo.  
3. Place the XML file in the **same folder** as your script.  
4. Run the script:  
   ```bash
   python face_sticker_blur.py
   ```
5. Ensure your **webcam** is connected and ready.

***

## 🎨 Customization Tips

- Tweak **`sticker_width`** and **blur parameters** to change sticker size and softness.  
- Edit the background **color** or **opacity** by modifying the rectangle and alpha blending code.  
- Add your own **creative stickers or effects** for unique overlays!

***

## ⌨️ Keyboard Controls

- **`s`** : Save a snapshot of the current frame 📸.  
- **Down Arrow (↓)** : Exit the program smoothly 🚪.

***

## 📦 Dependencies

- **OpenCV** (`cv2`)  
- **NumPy** (`numpy`)

***

## 📜 License

This project is **open-source** and free for **educational** and **personal use**.

***

✨ This project offers a **fun, stylish**, and **privacy-friendly** way to anonymize faces in live webcam feeds by applying **custom blurred stickers**. Perfect for **live streaming**, **creative video content**, or learning **computer vision**! 🎥👩‍💻



