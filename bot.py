import google.generativeai as genai
genai.configure(api_key="AIzaSyDGJFFUTdcyFzaIcgS698-I7ZvZiWK0WuI")

# model = genai.GenerativeModel("gemini-1.5-flash")
# chat = model.start_chat(
#     history=[
#         {"role": "user", "parts": "Hello"},
#         {"role": "model", "parts": "Great to meet you. What would you like to know?"},
#     ]
# )
# response = chat.send_message("I have 2 dogs in my house.")
# print(response.text)
# response = chat.send_message("How many paws are in my house?")
# print(response.text)


def chatbaby(history,prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat(
        history=history
    )
    response = chat.send_message(prompt)
    return response.text


