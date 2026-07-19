from app.services.llm_service import llm_service


class ChatService:

    def ask(self, paper: str, question: str):

        prompt = f"""
You are an expert research assistant.

Answer ONLY using the information in the research paper below.

If the answer is not present in the paper, reply exactly:

"I couldn't find that information in the uploaded paper."

Research Paper
--------------
{paper}

Question
--------
{question}
"""

        response = llm_service.invoke(prompt)

        return response.content


chat_service = ChatService()