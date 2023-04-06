FROM python:3.11-alpine3.17
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 3000
CMD python ./flaskapp.py