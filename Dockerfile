from python:3.12


RUN apt update -y && apt install awscli -y
WORKDIR /app


COPY . /app
RUN pip install -r requirements.txt


CMD ["python3", "app.py"]