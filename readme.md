# readme
Reads temperature from mqtt and plots on [plot.ly](https://plot.ly). Best used together with homematic HM-CC-RT-DN and [homegear](https://www.homegear.eu/index.php/Main_Page)

## api access
### tokens
get tokens at
  - [https://plot.ly/settings/api](https://plot.ly/settings/api)

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
