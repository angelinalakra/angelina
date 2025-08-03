import cv2
from fer import FER
import json
import random

# Load song database
with open("songs.json", "r") as file:
    music_data = json.load(file)

# Initialize webcam and FER detector
cap = cv2.VideoCapture(0)
detector = FER()

print("📸 Capturing your emotion... Look at the camera!")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Error capturing video.")
        break

    # Detect emotions
    result = detector.top_emotion(frame)
    if result:
        emotion, score = result
        print(f"\n🧠 Detected Emotion: {emotion.capitalize()} ({round(score * 100, 2)}%)")
        
        if emotion in music_data:
            song_link = random.choice(music_data[emotion])
            print(f"🎶 Here's a song for your mood: {song_link}")
        else:
            print("😕 Emotion not recognized. Try again.")

        break

    cv2.imshow("Press 'q' to quit", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
