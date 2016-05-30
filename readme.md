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
(rvenv) ➜  hgplot git:(master) ✗ python temperature.py
https://plot.ly/~joe/1
2016-03-06 23:03:56: 21.42
2016-03-06 23:04:58: 21.42
2016-03-06 23:05:58: 21.52
[...]
```

and visit the [plot.ly dashboard](https://plot.ly/organize/home)

## links
- https://github.com/shirk/node-red-contrib-homegear-mqtt
