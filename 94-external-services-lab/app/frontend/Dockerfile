FROM python:3.7
EXPOSE 8501

WORKDIR /usr/src/app
 
RUN apt-get update && apt-get install curl

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD ["streamlit", "run", "src/index.py"]

