FROM python:3.6-alpine
RUN adduser -D apiproj
WORKDIR /home/apiproj
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY api.py worker.py ./

RUN chown -R apiproj:apiproj .
USER apiproj
CMD uvicorn api:app --host 0.0.0.0 --port 5057
