# keylogger

A simple keylogger that sends the logs to your gmail account.

## features

- sends the logs to your gmail account
- sends the logs every `60` seconds( _you can change this in the `config.py` file_ )
- captures mouse events

## prerequisities

- `python` >=3.6
- change the `config.py` file to your needs i.e. your gmail address, password and the time interval between each email sent

## installation

```sh
  pip install -r requirements.txt
```

## requirements

- make sure your gmail account has 2FA activated( _Make sure you do so, otherwise you'll stay wishing_ )
- enable _App passwords_ in your Google account
- then create an app under `App passwords`
- use the password google will provide you in order to setup the script
- remember to use the password alongside your email address in the `config.py` file

## usage

- `python main.py`
- or add the shebang line `#!/usr/bin/env python` at the ultimate/very top of the `main.py` file and make it executable `chmod +x main.py` and then run it `./main.py`

## references

- [pynput](https://pynput.readthedocs.io/en/latest/)
- [smtplib](https://docs.python.org/3/library/smtplib.html)

## disclaimer

- This script is for educational purposes only. I am not responsible for any damage you cause using this script. Use at your own risk.
