FROM python:3.8
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt
CMD gunicorn --workers=4 --threads=16 --bind 0.0.0.0:5000 app:app --access-logfile '-' --error-logfile '-'
