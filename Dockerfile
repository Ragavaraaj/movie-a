FROM python:3.10 as builder

RUN mkdir /app 

COPY . /app

WORKDIR /app

ENV PYTHONPATH=${PYTHONPATH}:${PWD} 

RUN pip3 install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

EXPOSE 8000

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]


