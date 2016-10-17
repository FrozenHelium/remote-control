# Remote Control

An awesome remote control server for linux. Run it, use it, love it.

## Requirements

* python-3
* django (>=1.10)
* pyuserinput
* psutil


## Running

Run the django server:

```bash
$ python3 manage.py runserver 0.0.0.0:8000
```

Load the remote control from a mobile browser:

```
http://<ip-of-pc>:8000/
```

You can obtain ip of your pc with bash command `ifconfig`.

## Installing the app indicator

Copy *remote-control.desktop* file to */usr/share/applications/*.

Modify the file by replacing *<path>* so that it points to the path where you have stored the repository (containing the *rc_indicator.py* file).
