import os
import openai

def conect_antibloqueo(data):
    
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = data

    try:
        response = openai.Completion.create(
            model="text-curie-001",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["###"])

        return dict(response["choices"][0])["text"].replace("\n\n", "") , 200
    except Exception as err:
        return {"Error": err}, 500


def read_text_exemple():
    f = open('texto.txt', 'r')
    content = f.read()
    return content