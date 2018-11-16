# minecraft map monitor
a minecraft map monitor(dynmap) for recording our excellent time in MC by the map plugin. Statistics includes each player's spatio-temporal track, hit-point, etc.

![](https://github.com/liubai01/minecraft_map_monitor/blob/master/img/screenshot.png)

### Player-info Sample

```json
{
	"currentcount": 13,
	"hasStorm": true,
	"players": [{
		"world": "world",
		"armor": 19,
		"name": "xxx",
		"x": 2131.0,
		"y": 65.0,
		"health": 20.0,
		"z": 460.0,
		"sort": 1,
		"type": "player",
		"account": "xxx"
	}, {
		"world": "world",
		...
```

### Prerequisite

python3, requests

### Quick Start

```bash
pip3 install requests
python3 ./MAIN.py
```

### Update Log

2018/11/16: realize the function of downloading the player meta info