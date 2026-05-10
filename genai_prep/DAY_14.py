# GenAI Prep Day 14 practice
# Write code that:
# - defines get_model_reply(user_text)
# - returns f"Mock reply: {user_text}"
# - uses a while True loop
# - asks the user for input
# - stops if the user types "exit"
# - otherwise prints the reply


# Add the function and chatbot loop below.



def get_model_reply(user_text):
        return f"Mock reply: {user_text}"

while True:
        user_text = input("You: ")

        if user_text == "exit":
                break
        
        print(get_model_reply(user_text))