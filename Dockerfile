# docker build -f Dockerfile -t matthewshirtliffecouk/spatchcock .
# docker run -d -p 5000:5000 --name spatchcock  matthewshirtliffecouk/spatchcock

FROM python:3.6

MAINTAINER Matthew Shirtliffe

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt


COPY . .
EXPOSE 5000
EXPOSE 8098


CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app"]