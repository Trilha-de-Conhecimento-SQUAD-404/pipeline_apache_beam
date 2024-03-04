FROM apache/beam_python3.7_sdk:2.25.0

RUN pip install apache-beam

COPY ./pipeline /pipeline

CMD ["python3", "/pipeline/app.py"]