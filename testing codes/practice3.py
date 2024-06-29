from gtts import gTTS
from playsound import playsound
import os

hindi_text = "नमस्ते, कैसे हैं आप?"

# Generate the audio
tts = gTTS(text=hindi_text, lang='hi')

# Play the audio (in real-time)
tts.save("temp.mp3")  # Save as a temporary file
playsound("temp.mp3")  # Play the audio

# Clean up (optional)
os.remove("./temp.mp3")
