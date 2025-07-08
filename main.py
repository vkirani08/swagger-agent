import ollama
from prance import ResolvingParser

def load_swagger_context(file_path):
    print("📄 Parsing Swagger file...")
    parser = ResolvingParser(file_path)
    spec = parser.specification
    print("✅ Parsed successfully.")

    endpoints = []
    paths = spec.get("paths", {})

    for path, methods in paths.items():
        for method, details in methods.items():
            summary = details.get("summary", "No summary provided")
            parameters = details.get("parameters", [])
            responses = details.get("responses", {})

            param_lines = []
            for param in parameters:
                param_name = param.get("name", "unknown")
                param_type = param.get("schema", {}).get("type", "unknown")
                required = param.get("required", False)
                param_lines.append(f"- {param_name} ({param_type}) {'[required]' if required else '[optional]'}")

            response_lines = []
            for code, resp in responses.items():
                desc = resp.get("description", "")
                response_lines.append(f"{code}: {desc}")

            endpoint_block = f"""
=== {method.upper()} {path} ===
Summary: {summary}

Parameters:
{chr(10).join(param_lines) if param_lines else 'None'}

Responses:
{chr(10).join(response_lines) if response_lines else 'None'}
"""
            endpoints.append(endpoint_block.strip())

    context = "\n\n".join(endpoints[:20])  # Limit to top 20 for token safety
    print(f"📋 Loaded {len(endpoints)} endpoints.")
    return context


def ask_llm_with_context(user_prompt, api_context):
    system_message = f"""You are an assistant for Petstore API developers.

Answer only based on the following OpenAPI spec:

{api_context}
"""

    response = ollama.chat(
        model='llama3.2',
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response['message']['content']


if __name__ == "__main__":
    print("🤖 Swagger Agent is running (powered by Llama 3 via Ollama)...\n")
    swagger_context = load_swagger_context("petstore.json")

    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        answer = ask_llm_with_context(query, swagger_context)
        print(f"Assistant: {answer}\n")
