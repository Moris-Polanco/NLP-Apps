FROM python:3.9
RUN apt-get update && apt-get clean


WORKDIR /app

RUN pip install --upgrade pip
COPY ./requirements.txt /app
RUN pip install -r requirements.txt

EXPOSE 8501

COPY . /app
CMD streamlit run --server.port $PORT main.py