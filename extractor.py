import google.generativeai as genai
genai.configure(api_key="AIzaSyDGJFFUTdcyFzaIcgS698-I7ZvZiWK0WuI")


def get_class(text):
    model = genai.GenerativeModel('gemini-1.5-flash',
                              generation_config={"response_mime_type": "application/json"})

    prompt = """
    classname is mentioned in the below text example (it-b,it-a,ITA,ITB,IT A)
    """+text+"""
        Class = {"classname": str}
    Return only single `Class`
   
    """

    response = model.generate_content(prompt)
    return response.text