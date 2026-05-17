import ollama


MODEL_NAME = "gpt-oss:120b-cloud"


def generate_response(prompt):

    response = ollama.generate(
        model=MODEL_NAME,
        prompt=prompt
    )

    return response["response"]