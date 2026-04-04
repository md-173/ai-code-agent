import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

MODEL = "gemini-2.5-flash"

def main(): 
    # Parse command line prompt
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
   
    # List of all messages
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    # Get API key
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Api key not found in env file")
    
    # Generate response
    client = genai.Client(api_key=api_key) 
    response = client.models.generate_content(
            model=MODEL,
            contents=messages)
    if not response.usage_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")

    # Output token counts and response
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Response:\n{response.text}")

if __name__ == "__main__":
    main()
