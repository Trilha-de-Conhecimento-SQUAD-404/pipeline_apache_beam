FROM apache/beam_python3.8_sdk:latest

ENTRYPOINT ["/opt/apache/beam/boot", "--worker_pool"]

# WORKDIR /usr/src/app

RUN pip install apache-beam

COPY ./pipeline .

CMD [ "python", "app.py" ]
