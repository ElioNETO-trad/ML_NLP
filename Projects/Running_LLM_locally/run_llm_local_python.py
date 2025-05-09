import requests

def query_ollama(input_text):
    
    base_url = "[API_address+/api/generate]"

    payload = {
    "model": "[your_model_name]",
    "prompt": input_text,  # Use "prompt" instead of "messages"
    "stream": False  # Disable streaming for a clean response
    }
    try:
        response = requests.post(base_url, json=payload)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        return response.json().get("response", "No response found in API result.")
    except requests.exceptions.RequestException as e:
        return f"API request failed: {e}"

if __name__ == "__main__":
    input_text = input("Enter your question: ")
    result = query_ollama(input_text)
    print(f"Question: {input_text}\nAnswer: {result}")



# get_ollama_response = lambda: print(f"Question: {input_text}\nAnswer: {query_ollama(input_text)}")

get_ollama_response = lambda: (
    (lambda input_text: print(f"Question: {input_text}\nAnswer: {query_ollama(input_text)}"))
    (input('Enter your question: '))
)



