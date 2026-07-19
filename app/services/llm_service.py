from langchain_openai import ChatOpenAI
from openai import APIStatusError

from app.config import settings


class LLMService:

    def __init__(self):

        self.llm = ChatOpenAI(
            api_key=settings.OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1",
            model=settings.MODEL_NAME,
            temperature=settings.TEMPERATURE,
            max_tokens=settings.MAX_TOKENS,

            default_headers={
                "HTTP-Referer": "https://researchmind-ai-ashrith.streamlit.app",
                "X-Title": "ResearchMind AI",
            },
        )

    def invoke(self, prompt: str):

        try:

            response = self.llm.invoke(prompt)

            return response

        except APIStatusError as e:

            print("Status Code:", e.status_code)

            try:
                print("Response:", e.response.text)
            except Exception:
                pass

            raise

        except Exception as e:

            print("LLM Error:", str(e))

            raise


llm_service = LLMService()