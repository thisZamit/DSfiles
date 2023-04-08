FROM python:3.11.2
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python ./flaskapp.py
