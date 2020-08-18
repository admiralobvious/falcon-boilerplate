import io

import pytest

from app.media import json


class Stream:
    data = None

    def write(self, data):
        self.data = data


def test_json_dumps():
    doc = {"k": "v"}
    result = json.dumps(doc)

    assert result == '{"k":"v"}'


def test_json_dump():
    doc = {"k": "v"}
    stream = Stream()
    json.dump(doc, stream, chunk_size=100)

    assert stream.data == b'{"k":"v"}'


def test_json_dumps_exception():
    doc = {"k": frozenset}
    with pytest.raises(ValueError):
        json.dumps(doc)


def test_json_loads():
    doc = {"k": "v"}
    doc_str = '{"k": "v"}'
    result = json.loads(doc_str)

    assert result == doc


def test_json_load():
    doc = '{"k": "v"}'
    b = io.BytesIO(bytes(doc.encode("utf-8")))
    result = json.load(b)

    assert result == {"k": "v"}
