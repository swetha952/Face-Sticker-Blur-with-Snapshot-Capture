import cv2
import numpy as np

a=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
b=cv2.VideoCapture(0)
snapshot_count = 0 

while True:
    r_rect,i_img= b.read() 
    c_col=cv2.cvtColor(i_img,cv2.COLOR_BGR2GRAY) 
    f=a.detectMultiScale(c_col,1.3,6)

    sticker_x, sticker_y = 10, 50  #starting coordinates for stickers

    for (x1,y1,w1,h1) in f: 
        cv2.rectangle(i_img,(x1,y1),(x1+w1, y1+h1),(255,0,0))

        face_roi = i_img[y1:y1+h1, x1:x1+w1] #extracting face region

        # Create a smooth, blurred sticker instead of pixelation ###
        # Resize face for sticker (smaller size)
        sticker_width = 100  # Width of sticker
        aspect_ratio = h1 / w1
        sticker_height = int(sticker_width * aspect_ratio)
        small_face = cv2.resize(face_roi, (sticker_width, sticker_height), interpolation=cv2.INTER_AREA)

        # Apply Gaussian blur for smooth effect
        blurred_face = cv2.GaussianBlur(small_face, (15, 15), 10)

         # Draw white rounded rectangle background for sticker (optional for cute effect)
        overlay = i_img.copy()
        y_offset = sticker_y * (f.tolist().index([x1, y1, w1, h1]) + 1)
        # Rounded rectangle approximation with filled rectangle + circles
        cv2.rectangle(overlay, (sticker_x - 5, y_offset - 5),
                      (sticker_x + sticker_width + 5, y_offset + sticker_height + 5), (255, 255, 255), -1)
        alpha = 0.8
        cv2.addWeighted(overlay, alpha, i_img, 1 - alpha, 0, i_img)

        # Paste blurred face sticker onto frame
        i_img[y_offset:y_offset + sticker_height, sticker_x:sticker_x + sticker_width] = blurred_face
        
    #Displaying face count
    cv2.putText(i_img, f"Faces: {len(f)}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        

    

    cv2.imshow('img',i_img)  
    h=cv2.waitKey(40) & 0xff 
    if h==40:
        break
    elif h == ord('s'):  #Optional snapshot saving feature
        cv2.imwrite(f'snapshot_{snapshot_count}.jpg', i_img)
        print(f"Saved snapshot_{snapshot_count}.jpg")
        snapshot_count += 1

b.release() 
cv2.destroyALLWindows()
