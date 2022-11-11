FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD sh -c "sleep 10s; python3 ./app.py"
