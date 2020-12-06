FROM python:3.6.8

WORKDIR /app

copy . .

EXPOSE 5000

RUN pip3 install -r requirements.txt

ENTRYPOINT ["/usr/local/bin/python", "process.py"]
