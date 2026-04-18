import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class AIService:
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-1.5-pro')
        else:
            self.model = None

    async def process_multimodal_query(self, prompt: str, image_data: str = None):
        if not self.model:
            return "AI Service is currently offline. Please check your GOOGLE_API_KEY."

        try:
            if image_data:
                # Real implementation would decode b64 and pass to Gemini
                # For now, we simulate the multimodal response structure
                response = self.model.generate_content([prompt, "Image binary data placeholder"])
            else:
                response = self.model.generate_content(prompt)
            
            return response.text
        except Exception as e:
            return f"Error processing AI request: {str(e)}"

ai_service = AIService()
