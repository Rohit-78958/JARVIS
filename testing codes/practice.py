import google.generativeai as genai
import os

genai.configure(api_key="#-4")

        # Create a model (e.g., 'gemini-1.0-pro-latest')
        # model = genai.GenerativeModel('gemini-1.0-pro-latest')
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("tell me about rohit sharma is less than 50 words")
# speak(response.text)
print(response.text)