from google import genai
from src.ai.base import AIPlatform   # avoid relative import issues


class GeminiAI(AIPlatform):
    def __init__(self, api_key: str, system_prompt: str = None):
        self.api_key = api_key
        self.system_prompt = system_prompt

        # New SDK uses client
        self.client = genai.Client(api_key=self.api_key)

        # Model name (updated)
        self.model = "gemini-2.5-flash-lite"

    def chat(self, prompt: str) -> str:
        if self.system_prompt:
            prompt = self.system_prompt + "\n" + prompt

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return response.text