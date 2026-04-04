import os
import argparse
from dotenv import load_dotenv
from google import genai

MODEL = "gemini-2.5-flash"

def main():
    load_dotenv()
    
    # Get API key
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RuntimeError("Api key not found in env file")
    client = genai.Client(api_key=api_key) 

    # Parse command line prompt argument
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    # Generate content
    content = client.models.generate_content(
            model=MODEL,
            contents=args.user_prompt)
    print(f"User prompt: {args.user_prompt}")

    # Get metadata
    content_metadata = content.usage_metadata
    if content_metadata == None:
        raise RuntimeError("Generated Content Metadata does not exist")

    # Output token counts and response
    print(f"Prompt tokens: {content_metadata.prompt_token_count}")
    print(f"Response tokens: {content_metadata.candidates_token_count}")
    print(f"Response:\n{content.text}")


if __name__ == "__main__":
    main()
