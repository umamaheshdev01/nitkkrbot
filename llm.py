import google.generativeai as genai
genai.configure(api_key="AIzaSyDGJFFUTdcyFzaIcgS698-I7ZvZiWK0WuI")


def generate(template,prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(template+prompt)
    return response.text

print(generate('What is time now',''))