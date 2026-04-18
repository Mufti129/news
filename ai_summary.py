from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_ai_summary(news, trends):
    prompt = f"""
    Kamu adalah analis ekonomi Indonesia.

    Berikut data:
    NEWS:
    {news}

    TRENDS:
    {trends}

    Buat:
    1. Ringkasan kondisi ekonomi hari ini
    2. Insight penting
    3. Prediksi singkat
    4. Peluang bisnis

    Gunakan bahasa profesional tapi simple.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
