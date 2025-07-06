import ollama
from prance import ResolvingParser

def load_swagger_context(file_path):
    print("📄 Parsing Swagger file...")
    parser = ResolvingParser(file_path)
    spec = parser.specification
    print("✅ Parsed successfully.")
    endpoints = []

    for path, methods in spec['paths'].items():
        for method, details in methods.items():
            summary = details.get("summary", "No summary provided")
            endpoints.append(f"{method.upper()} {path} — {summary}")

    context = "\n".join(endpoints[:30])  # Limit for token safety
    print(f"📋 Loaded {len(endpoints)} endpoints.")
    return context

# Ask the LLM with Swagger context
def ask_llm_with_context(user_prompt, api_context):
    system_message = system_message = f"""You are a helpful assistant for Petstore developers.
Use the OpenAPI spec below to help users understand which endpoint to use, what parameters it needs, and what response they can expect.

ONLY answer based on the API spec.

OpenAPI (Petstore) Spec Overview:
{api_context}
"""

    response = ollama.chat(
        model='phi',
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response['message']['content']

if __name__ == "__main__":
    print("🤖 GitHub Swagger Assistant is running (powered by local Phi)...\n")
    swagger_context = load_swagger_context("petstore.json")

    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        answer = ask_llm_with_context(query, swagger_context)
        print(f"Assistant: {answer}\n")
