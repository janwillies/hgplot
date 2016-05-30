FROM python:3-alpine

RUN pip install --upgrade pip

RUN pip install pyyaml \
    plotly \
    paho-mqtt \
    pytz

ADD temperature.py /temperature.py

ENTRYPOINT python /temperature.py
