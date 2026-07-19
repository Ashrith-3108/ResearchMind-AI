from langchain_openai import ChatOpenAI

from app.config import settings


class LLMService:

    def __init__(self):

        self.llm = ChatOpenAI(
            api_key=settings.OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1",
            model=settings.MODEL_NAME,
            temperature=settings.TEMPERATURE,
            max_tokens=settings.MAX_TOKENS,
        )

    def invoke(self, prompt: str):
        response = self.llm.invoke(prompt)

        return response


llm_service = LLMService()