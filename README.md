[![Python](https://img.shields.io/pypi/pyversions/shell2http.svg)](https://badge.fury.io/py/shell2http)
[![PyPI](https://badge.fury.io/py/shell2http.svg)](https://badge.fury.io/py/shell2http)

# shell2http
HTTP-server to execute shell commands. Designed for development, prototyping or remote control. Settings through two command line arguments, path and shell command. By default bind to :8080.

# Usage

```bash
shell2http [options] ["shell command" for /] /path "shell command" /path2 "shell command2" ...
options:
    -p, --port NNNN : port for http server ( default 8080 )
```

# Install

```bash
pip install shell2http
```

# Examples

## Windows

```powershell
shell2http 'shutdown -s -t 0'
```

```powershell
shell2http 'shutdown -s -t 0' /beep 'echo ^G'
```

## Linux

```bash
shell2http 'notify-send Hello root'
```


```bash
shell2http -p3000 'notify-send Hello root' /path 'canberra-gtk-play -i desktop-login'
```

```bash
shell2http -p3000 /path 'canberra-gtk-play -i desktop-login'
```

# Acknowledgements

https://github.com/msoap/shell2http

https://github.com/eshaan7/Flask-Shell2HTTP
