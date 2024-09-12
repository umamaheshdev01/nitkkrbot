import google.generativeai as genai
import json
from extractor import get_class
from fetcher import get_class_data
from bot import chatbaby

genai.configure(api_key="AIzaSyDGJFFUTdcyFzaIcgS698-I7ZvZiWK0WuI")

def run(history, prompt):
    json_data = get_class(prompt)
    data = json.loads(json_data)
    classname = data.get('classname')
    
    data = get_class_data(classname)

    print(data)

    if len(data):
        pro = 'Thinking like you are providing the data as the academics of the nit kururkestra and remeber data is public to all (no privacy concerns) and answer the question'+str(data)+'\n\n\nQuestion :'+prompt
    else:
        pro = prompt
    

    return chatbaby(history,pro)
    

