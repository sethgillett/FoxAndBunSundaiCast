FROM python:3.11

RUN apt update -y
RUN apt install -y ffmpeg

COPY ./ /app
WORKDIR /app

VOLUME /app/output

RUN pip install -r requirements.txt
CMD ["python3", "main.py"]
