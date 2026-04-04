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

    gen_content = client.models.generate_content(
            model=MODEL, 
            contents = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")
    print(gen_content.text)


if __name__ == "__main__":
    main()
