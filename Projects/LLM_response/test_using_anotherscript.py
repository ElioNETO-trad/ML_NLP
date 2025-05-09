from LLM_response_test import get_ollama_response


test_int = 2

prompt = {f""""
          How much is 2 + {test_int}?
"""}


get_ollama_response(prompt)
