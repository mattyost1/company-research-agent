import anthropic
from tavily import TavilyClient

client = anthropic.Anthropic(api_key="your-anthropic-key-here")
tavily = TavilyClient(api_key="your-tavily-key-here")

# --- TOOLS ---

tools = [
    {
        "name": "search_web",
        "description": "Search the web for information about a company",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query"
                }
            },
            "required": ["query"]
        }
    }
]

def search_web(query):
    print(f"Searching: {query}...")
    results = tavily.search(query=query)
    return results['results'][0]['content']

# --- AGENT LOOP ---

def run_agent(user_message):
    print(f"\nResearching: {user_message}\n")
    messages = [{"role": "user", "content": user_message}]

    system = "You are a company research assistant. Search the web multiple times to gather comprehensive information about the company and return a structured overview including financials, recent news, products, and key facts."

    while True:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=4096,
            system=system,
            tools=tools,
            messages=messages
        )

        print(f"Stop reason: {response.stop_reason}")

        if response.stop_reason == "end_turn":
            print(response.content[0].text)
            break

        if response.stop_reason == "tool_use":
            messages.append({"role": "assistant", "content": response.content})
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    result = search_web(block.input["query"])
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result
                    })
            messages.append({"role": "user", "content": tool_results})

# --- RUN ---
# Replace the company name below with any company you want to research
run_agent("Research [COMPANY NAME] and give me a structured company overview.")