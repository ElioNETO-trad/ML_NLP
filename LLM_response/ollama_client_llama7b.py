# run_llm_local_python.py
import requests

def query_ollama(input_text, model="codellama:7b"):
    base_url = "http://localhost:11434/api/generate"
    
    payload = {
        "model": model,
        "prompt": input_text,
        "stream": False
    }
    
    try:
        response = requests.post(base_url, json=payload)
        response.raise_for_status()
        return response.json().get("response", "No response found in API result.")
    except requests.exceptions.RequestException as e:
        return f"API request failed: {e}"

def get_ollama_response(input_text, model="codellama:7b"):
    return query_ollama(input_text, model)

if __name__ == "__main__":
    input_text = input("Enter your question: ")
    result = get_ollama_response(input_text)
    print(f"Question: {input_text}\nAnswer: {result}")