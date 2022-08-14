import os
import openai

def conect_escritor(data):
    
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = data

    try:
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=prompt,
            temperature=0.7,
            max_tokens=2056,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0.5,
            stop=["###"])

        return dict(response["choices"][0])["text"].replace("\n\n", "") , 200
    except Exception as err:
        return {"Error": err}, 500


def read_text_exemple():
    f = open('texto.txt', 'r')
    content = f.read()
    return content