from langchain_google_genai import ChatGoogleGenerativeAI

from app.config import settings


class LLMService:

    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(
            model=settings.MODEL_NAME,
            google_api_key=settings.GEMINI_API_KEY,
            temperature=settings.TEMPERATURE,
        )

    def invoke(self, prompt: str):

        try:

            response = self.llm.invoke(prompt)

            return response

        except Exception as e:

            print("Gemini Error:", str(e))
            raise


llm_service = LLMService()