# GenAI Prep Day 9 practice
# Write code that:
# - creates response_data with model, choices, message, role, and content
# - prints only the nested content value


#import requests 

#url = "https://httpbin.org/post"

#headers= {
#    "Content-Type": "application/json"
#}

#payload = {
#        "model" : "demo-model",
#        "messages": [{"role": "user", "content": "Hello"}]
#    }

#response = requests.post(url,headers=headers, json=payload)

#print(response.status_code)
#print(response.json()['data'])

response_data = {
    "model" : "demo-model",
    "choices": [
        {
            "messages" : {
                "role" : "assistant",
                "content": "hello from assistant"
            }
        }
    ]
}

print(response_data['choices'][0]['messages']['content'])