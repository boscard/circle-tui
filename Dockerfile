FROM python:3.6-alpine

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY *.py circle_tui /app/

ENTRYPOINT ["python", "/app/circle-tui.py"]
CMD ["--help"]
