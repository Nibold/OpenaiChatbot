from openai import OpenAI
import openai
import os
from dotenv import load_dotenv
# Assuming your OpenAI API key is stored in an environment variable for security
load_dotenv()
api_key = os.getenv("API_KEY")

# openai.api_key = 'api_key ="INSERT YOUR OWN API KEY HERE"'
client = OpenAI(api_key=api_key)
model = "gpt-3.5-turbo-0125"

# Define a function to simulate a chat-like interaction
'''def get_chat_response(messages):
    # Convert chat history into a prompt string for the model
    prompt_text = ""
    for msg in messages:
        prompt_text += f"{msg['role']} says: {msg['content']}\n"
    
    # Call the API with the constructed prompt
    response = client.chat.completions.create(
        model="gpt-4",  # Ensure you are using the correct model for your API plan
        prompt=prompt_text,
        max_tokens=150,
        temperature=0.5,
        stop=["\n", " user says:", " assistant says:"],  # Define stops to control completion points
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()'''

# Example message sequence
messages = [
    {"role": "system", "content": "You're a truthful assistant and you adhere to the prompts"},
    {"role": "user", "content": "Here is a text in XML tags <text>...</text>. Please return the first and last name found in the text as JSON object with keys 'firstname' and 'lastname'. <text> My name is Nicole Boldyrev and I work in a factory. </text>"},
    {"role": "assistant", "content": "{\n\"firstname\": "}
]

answer = []

for _ in range(5):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    responsetext = response.choices[0].message.content
    answer.append(responsetext)


print(answer)
print(len(set(answer)))

# Fetch the response from the model
'''response_text = get_chat_response(messages)
print(response_text)'''
