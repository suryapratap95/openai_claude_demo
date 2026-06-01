import os
from openai import OpenAI
import anthropic 
from dotenv import load_dotenv

load_dotenv()


openai_client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

anthropic_client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

PROMPT = "What do you understand by machine learning"

def ask_openai():
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.1,
        messages=[
            {
                "role":"user",
                "content":PROMPT
            }
        ]
    )

    return response.choices[0].message.content

def ask_anthropic():
    response = anthropic_client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=400,
        temperature =0.1,
        messages=[
            {
                "role":"user",
                "content":PROMPT

            }
        ]
    )

    return response.content[0].text



openai_response = ask_openai()
print("Response: ", openai_response)

print("="* 60)

anthropic_reponse=ask_anthropic()
print(anthropic_reponse)