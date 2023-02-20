FROM python:3.9.10-slim-bullseye

WORKDIR /app

COPY ./src .

EXPOSE 5555

CMD [ "python", "main.py" ]

