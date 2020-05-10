# falcon-boilerplate [![Build Status](https://travis-ci.org/admiralobvious/falcon-boilerplate.svg?branch=master)](https://travis-ci.org/admiralobvious/falcon-boilerplate)

A Python 3.7+ boilerplate for the [Falcon](https://github.com/falconry/falcon) framework.
Uses [gunicorn](https://github.com/benoitc/gunicorn) as the WSGI HTTP server and [meinheld](https://github.com/mopemope/meinheld) as the gunicorn worker.
It also uses [Vyper](https://github.com/admiralobvious/vyper) for [12-factor](https://12factor.net/).

## Using

```
$ git clone https://github.com/admiralobvious/falcon-boilerplate.git myapp
$ cd myapp
$ make build
$ source venv/bin/activate
$ python run.py
```

To run the tests:

```
$ make test
```

## Optional Dependencies

Install [fastjsonschema](https://github.com/horejsek/python-fastjsonschema) or 
[jsonschema](https://github.com/Julian/jsonschema) if you wanna validate the requests/responses with 
[JSON Schema](https://json-schema.org/).

NOTE: The `/users` resources will not work if you don't have fastjsonschema or jsonschema installed.

Install [falcon-crossorigin](https://github.com/admiralobvious/falcon-crossorigin) if you need 
[CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) headers.
Must be enabled by passing `--cors-enabled` to `run.py` or any of the other ways supported by Vyper.
