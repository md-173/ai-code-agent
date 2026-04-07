import os
import argparse
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.get_files_info import schema_get_files_info
from call_function import available_functions, call_function

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
   
    for _ in range(20):
        final = generate_content(client, messages, args.verbose)
        if final:
            print(final)
            break
    else:
        print("Max iterations reached without a final response")
        sys.exit(1)



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
    
    if response.candidates is None:
        raise Exception("Response has no candidates")
    else:
        for candidate in response.candidates:
            messages.append(candidate.content)

    function_calls = response.function_calls
    
    function_result_list = []
    if function_calls is not None:
        for call in function_calls:
            function_call_result = call_function(call, verbose)
            if not function_call_result.parts:
                raise Exception(f'Function call {call.name} has no parts list')
            if function_call_result.parts[0].function_response is None:
                raise Exception(f'Function response of {call.name} is empty')
            if function_call_result.parts[0].function_response.response is None:
                raise Exception(f'Function result of {call.name} is none')
            function_result_list.append(function_call_result.parts[0])
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")

    else:
        return f"Response:\n{response.text}"
        

    messages.append(types.Content(role="user", parts=function_result_list))

if __name__ == "__main__":
    main()
