import anthropic
import test_config
CLAUDE_API_KEY = test_config.CLAUDE_API_KEY

client = anthropic.Anthropic(
    api_key=CLAUDE_API_KEY,
    
)

message = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=1000,
    temperature=0.0,
    system="Respond only in Yoda-speak.",
    messages=[
        {"role": "user", "content": "How are you today?"}
    ],
    # input = 'claude connected?' # input message(?)
)

print(message.content)
