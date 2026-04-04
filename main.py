import os
from dotenv import load_dotenv
from google import genai

MODEL = "gemini-2.5-flash"

def main():
    load_dotenv()
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RuntimeError("Api key not found in env file")
    client = genai.Client(api_key=api_key)

    prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    content = client.models.generate_content(
            model=MODEL,
            contents=prompt)
    print(f"User prompt: {prompt}")

    content_metadata = content.usage_metadata
    if content_metadata == None:
        raise RuntimeError("Generated Content Metadata does not exist")

    print(f"Prompt tokens: {content_metadata.prompt_token_count}")
    print(f"Response tokens: {content_metadata.candidates_token_count}")
    print(f"Response:\n{content.text}")


if __name__ == "__main__":
    main()
