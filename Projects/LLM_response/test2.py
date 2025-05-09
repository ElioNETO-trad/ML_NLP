from ollama_client_llama7b import get_ollama_response


question = "Translate to English: 'Olá, eu sou o elio'"
response = get_ollama_response(question)

print("Model response:")
print(response)