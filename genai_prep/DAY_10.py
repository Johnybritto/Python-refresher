# GenAI Prep Day 10 practice
# Write code that:
# - creates response_data with one nested content value
# - tries to read response_data["choices"][0]["message"]["content"]
# - prints the content if it exists
# - otherwise prints "No response text available"

response_data = {
    "choices": [
        {
            "message": {
                "content": "AI reply here"
            }
        }
    ]
}

try:
    content = response_data["choices"][0]["message"]["content"]
    print(content)
except:
    print("no response text available")
