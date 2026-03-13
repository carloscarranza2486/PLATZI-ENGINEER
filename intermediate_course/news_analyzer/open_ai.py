import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def analyze_news_with_ia(articles: list[dict], query: str) -> str | None:

    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    context = "\n".join(
        [
            f"- {article['title']}: {(article.get('description') or '')[:100]}..."
            for article in articles[:10]  # Limitar para control de costos
        ]
    )

    prompt = f"""
        Basándote en estas noticias:
        {context}

        Pregunta: {query}

        Responde de forma concisa en español.
    """

    print(prompt)

    response = client.responses.create(
        model="gpt-4o",
        instructions="Eres un agente que lee contexto y responde de manera breve",
        input=prompt,
    )

    print(response.output_text)
