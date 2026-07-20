from langchain_google_genai import ChatGoogleGenerativeAI

from app.config import settings


class LLMService:
    """
    Wrapper around Google's Gemini model.
    """

    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(
            model=settings.MODEL_NAME,
            google_api_key=settings.GEMINI_API_KEY,
            temperature=settings.TEMPERATURE,

            # Ask Gemini to always return JSON
            response_mime_type="application/json",
        )

    def invoke(self, prompt: str):
        """
        Send prompt to Gemini.
        """

        try:

            response = self.llm.invoke(prompt)

            # Helpful debugging
            print("\n========== GEMINI RESPONSE ==========")
            print("Type:", type(response))
            print("Content:", response.content)
            print("=====================================\n")

            return response

        except Exception as e:

            print("\n========== GEMINI ERROR ==========")
            print(type(e).__name__)
            print(str(e))
            print("==================================\n")

            raise


llm_service = LLMService()