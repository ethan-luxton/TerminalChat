import os
import openai
import json
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
        
        message = input("Ask me anything! ")
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message}
            ]
        )
        if message in ('stop', 'Stop'):
            quit()
        else:
            message_return = json.dumps(completion)
            message_parse = json.loads(message_return)
            print(message_parse['usage']['total_tokens'], "Tokens Used") # Shows how many tokens the response took from the OpenAI API.
            print("GPT: ",message_parse['choices'][0]['message']['content']) # Prints the response from the OpenAI API.
            
            main()


main()



