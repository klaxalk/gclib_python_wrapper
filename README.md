# Gclib python wrapper

A python wrapper for the gclib - the library for controlling Galil controllers and APIs.

## Gclib installation

For gclib, follow the instructions on [http://www.galil.com/sw/pub/all/doc/gclib/html/ubuntu.html](http://www.galil.com/sw/pub/all/doc/gclib/html/ubuntu.html) or use this digest:

```bash
os=$(lsb_release -r -s)
wget http://www.galil.com/sw/pub/ubuntu/$os/GALIL-PUB-KEY
sudo apt-key add GALIL-PUB-KEY
wget http://www.galil.com/sw/pub/ubuntu/$os/galil.list -O /etc/apt/sources.list.d/galil.list
sudo apt-get update
sudo apt-get install gclib
```

Install the python support according to the instructions: [http://www.galil.com/sw/pub/all/doc/gclib/html/python.html](http://www.galil.com/sw/pub/all/doc/gclib/html/python.html), or use this digest:

```bash
mkdir /tmp/py
cd /tmp/py
tar -xvf /usr/share/doc/gclib/src/gclib_python.tar.gz
gclib.py
setup.py
tar -xvf /usr/share/doc/gclib/src/gclib_python_examples.tar.gz
sudo python setup.py install
```
