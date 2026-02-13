import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_script(theme_description):
    prompt = f"""
    You are a short-form Instagram reel creator.

    Based on this description:
    "{theme_description}"

    Generate:
    1. A powerful hook (1 sentence)
    2. 3 short scenes (visual description)
    3. Caption
    4. 5 hashtags

    Keep it short and engaging.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content

