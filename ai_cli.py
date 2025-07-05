import openai
import os
import argparse
from dotenv import load_dotenv

load_dotenv()


client = openai.OpenAI(api_key= os.getenv("OPENAI_API_KEY"))


def get_ai_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                # {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"Error: {str(e)}"
    
def main():
    parser = argparse.ArgumentParser(description="CLI tool to interact with OpenAI's GPT model")
    parser.add_argument("prompt", type=str, help="The prompt to send to the AI model")
    args = parser.parse_args()

    prompt = " ".join(args.prompt)

    response = get_ai_response(prompt)
    print(response)

if __name__ == "__main__":
    load_dotenv()
    main()