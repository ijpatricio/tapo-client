To get started:

```
./run.sh install
```

Inside main.py, add devices:

```
# Find this region and update:
---
# Device IP Addresses
device_ips = {
    "micro": "192.168.68.100",
    "camera": "192.168.68.110",
}
```

Generate a `env` file, and fill accordingly

```
cp .env.example .env
```

Now you can run commands on a device.

```
python3 main.py micro on
python3 main.py micro off
python3 main.py micro toggle
```
