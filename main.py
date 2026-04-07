import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.get_files_info import schema_get_files_info
from call_function import available_functions

MODEL = "gemini-2.5-flash"

def main(): 
    # Parse command line prompt
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
   
    
    # Get API key
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Api key not found in env file")
    
    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")
    
    generate_content(client, messages, args.verbose) 

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
            model=MODEL,
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt)
    )
    if not response.usage_metadata:
        raise RuntimeError("Gemini API response appears to be malformed")

    # Output token counts and response
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    function_calls = response.function_calls
    
    if function_calls is not None:
        for call in function_calls:
            print(f"Calling function: {call.name}({call.args})")
    else:
        print(f"Response:\n{response.text}")

if __name__ == "__main__":
    main()
