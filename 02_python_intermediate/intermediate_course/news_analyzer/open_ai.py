import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def analyze_news_with_ia(articles: list[dict], query: str) -> str | None:
    # Eliminamos el os.environ.get(), la librería lo busca automáticamente
    client = OpenAI()

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

    # Sintaxis moderna de OpenAI (Chat Completions)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # o gpt-4o-mini
        messages=[
            {
                "role": "system",
                "content": "Eres un agente que lee contexto y responde de manera breve",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
    )

    # Extraer el texto de la respuesta
    output = response.choices[0].message.content
    print(output)

    return output
