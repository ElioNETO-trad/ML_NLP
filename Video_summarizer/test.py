from ollama_client_llama7b import get_ollama_response


query = input("Type your text: ")

print(query)

prompt = f"Explain to me the following text: {query}"

response = get_ollama_response(prompt)

print(response)