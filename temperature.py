#!/usr/bin/env python
"""reads temperature from homegear mqtt broker and plots on plot.ly."""

import datetime
import pytz
import json
import yaml

import paho.mqtt.client as mqtt

import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls

# read config filename
with open('config.yml', 'r') as f:
    config = yaml.load(f)

print(config)

# plot.ly auth
py.sign_in(config["plotly"]["user"], config["plotly"]["apikey"])

# one stream token per trace to be plotted
# https://plot.ly/settings/api
tls.set_credentials_file(stream_ids=config["plotly"]["stream_ids"])

stream_ids = tls.get_credentials_file()['stream_ids']

# hold traces to plot later
trace_arr = []

# holds the streams to write to
stream_dict = {}

# create stream from device
for dev in config["homegear"]["devices"]:
    # create plotly token
    token = dev["stream"]
    # create plotly logical stream
    stream = dict(token=token, maxpoints=config["plotly"]["maxpoints"])
    # setup graph layout
    trace = go.Scatter(
        x=[],
        y=[],
        mode='lines',
        line=dict(
            shape='spline'
        ),
        stream=stream,
        name=dev["name"]
    )

    trace_arr.append(trace)

    # new plotly protocol stream
    pystream = py.Stream(token)
    stream_dict[dev["id"]] = pystream

data = go.Data(trace_arr)

# Define dictionary of axis style options
axis_style = dict(
    showgrid=False,    # remove grid
    showline=False,    # remove axes lines
    zeroline=False     # remove x=0 and y=0 lines
)

# Add title to layout object
layout = go.Layout(title='temperature',
                   xaxis=go.XAxis(
                       axis_style,   # add style options
                   ), yaxis=go.YAxis(
                       range=[16, 26]
                   ),)

# Make a figure object
fig = go.Figure(data=data, layout=layout)

# Send fig to Plotly, initialize streaming plot, open new tab
unique_url = py.plot(fig, filename='temperature')
print('%s' % (unique_url))

# open plotly stream with the stream_id
for key in stream_dict.keys():
    stream_dict[key].open()


def on_connect(client, userdata, flags, rc):
    """callback function from mqtt initial connection."""
    print("Connected to broker " + config["mqtt"]["host"])
    # subscribe to topic
    client.subscribe(config["mqtt"]["topic"])


def on_message(client, userdata, msg):
    """callback function from mqtt message."""
    writeToPlotly(msg.topic, msg.payload.decode("utf-8"))


# write data to plotly stream
def writeToPlotly(topic, payload):
    """callback function from mqtt on_message."""
    parsed_json = json.loads(payload)

    # get the homegear peer id from mqtt topic
    # TODO find better way to get device
    device = topic[30:31]

    # read temperature from actual_temperature
    temp = parsed_json[0]

    # timestamp
    tz = pytz.timezone(config["homegear"]["timezone"])
    now = datetime.now(tz)

    print('%s: %s, %s' % (now, device, temp))

    # write to the homegear.devices.id plotly stream
    for key in stream_dict.keys():
        if key == int(device):
            stream_dict[key].write(dict(x=now, y=temp))

# set up mqtt connection
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(config["mqtt"]["host"], config["mqtt"]["port"], 60)

# loop until ctrl-c
client.loop_forever()

# close plotly stream
print('closing plotly stream')
for stream in stream_dict.values():
    stream.close()
