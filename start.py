import requests
import json

with open("API_KEY.json", "r") as api_key_file:
    api_key_data = json.load(api_key_file)
    API_KEY = api_key_data["API_KEY"]

with open('prompt.txt', 'r') as file:
    # Read the entire file into a string
    original_context = file.read()

def send_gpt_request(question, context):
    # Define the URL
    url = "https://api.openai.com/v1/chat/completions"

    # Define the headers
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    # Define the request payload as a Python dictionary
    payload = {
        "model": "gpt-4",
        "messages": [
            {
                "role": "system",
                "content": context
            },
            {
                "role": "user",
                "content": question
            }
        ],
        "temperature": 1,
        "top_p": 1,
        "n": 1,
        "stream": False,
        "max_tokens": 400,
        "presence_penalty": 0,
        "frequency_penalty": 0
    }

    # Convert the payload dictionary to a JSON string
    json_payload = json.dumps(payload)

    # Send the POST request
    response = requests.post(url, headers=headers, data=json_payload)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")
        print(f"Response content: {response.text}")  # Print the response content for debugging
        return None

context = original_context
i = 5
print("how can I help you")
while i > 0:
    i-=1
    user_input = input("type: ")
    response = send_gpt_request(user_input, context)

    if 'choices' in response and response['choices']:
        content = response['choices'][0]['message']['content']

        # Check if the message starts with [[CMD!]]
        if content.startswith("[[CMD!]]"):
            print("Executing:", content)  # Print the content after "[[CMD!]]"
            exit()
        else:
            print(content)
            context = content + context  # Set context for the next request
    else:
        print("No 'content' field found in the response.")
