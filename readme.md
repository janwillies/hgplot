# hgplot
Reads information from mqtt and plots on [plot.ly](https://plot.ly). Best used  with homematic [HM-CC-RT-DN](http://www.fhemwiki.de/wiki/HM-CC-RT-DN_Funk-Heizk%C3%B6rperthermostat) and [homegear](https://www.homegear.eu/index.php/Main_Page)

## prerequisites
### homegear
enable mqtt in `/etc/homegear/mqtt.conf`
### plotly
get api-key and tokens at [https://plot.ly/settings/api](https://plot.ly/settings/api)
and edit  `config.yml`

## docker quickstart
```
$ cp config-dist.yml config.yml
$ vim config.yml
$ docker run -it -v $(pwd)/config.yml:/config.yml willies/hgplot:latest
```
## dev
### virtualenv
use `pyvenv rvenv` to setup virtualenv and `source rvenv/bin/activate` to activate


## run

```
(rvenv) ➜  hgplot git:(master) ✗ python hgplot.py
https://plot.ly/~joe/1
Connected to broker mqtt.broker.lan
2016-05-31 21:29:42.130964+02:00: 1, 23.7
2016-05-31 21:29:42.131873+02:00: 2, 23.9
2016-05-31 21:29:42.132849+02:00: 3, 23.4
[...]
```

and visit the [plot.ly dashboard](https://plot.ly/organize/home)

## links
- https://github.com/shirk/node-red-contrib-homegear-mqtt
