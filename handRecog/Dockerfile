FROM zhlhahaha/mediapipe_base:aarch64
RUN mkdir work
WORKDIR /work
RUN pip install paho-mqtt flask
COPY handRecog.py handRecog.py
COPY templates templates
ENTRYPOINT ["python3", "handRecog.py"]
