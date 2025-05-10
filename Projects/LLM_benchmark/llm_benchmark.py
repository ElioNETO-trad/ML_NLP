#Still working on it

from llm_benchmark import benchmark
from llm_benchmark.backends import OllamaBackend

#To set up the Ollama model to benchmark

model_name = "llama3:instruct"

#Defining the back end for ollama

ollama_backend = OllamaBackend(model_name=model_name)

# Checking the benchmarking process

results = benchmark(
    backend = ollama_backend
    prompt = "What is the capital of France?"
    num_samples = 10
)

