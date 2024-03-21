FROM apache/beam_python3.8_sdk:latest

RUN pip install apache-beam

COPY ./pipeline /opt/apache/beam/pipeline

WORKDIR /opt/apache/beam/pipeline

ENTRYPOINT ["/opt/apache/beam/boot", "--worker_pool"]

