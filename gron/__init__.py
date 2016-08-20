# -*- coding:utf-8 -*-
import re


def walk(data, root):
    r = []
    _walk(data, [root], r)
    return r


def _walk(data, path, r):
    if data is None:
        r.append('{path} = {value};'.format(path=to_path(path), value='null'))
    elif isinstance(data, bool):
        r.append('{path} = {value};'.format(path=to_path(path), value=str(data).lower()))
    elif isinstance(data, dict):
        r.append('{path} = {{}};'.format(path=to_path(path)))
        for k, v in sorted(data.items()):
            path.append(k)
            _walk(v, path, r)
            path.pop()
    elif isinstance(data, (list, tuple)):
        r.append('{path} = [];'.format(path=to_path(path)))
        for i, e in enumerate(data):
            path.append(str(i))
            _walk(e, path, r)
            path.pop()
    elif isinstance(data, (str, bytes)):
        r.append('{path} = "{value}";'.format(path=to_path(path), value=data))
    else:
        r.append('{path} = {value!r};'.format(path=to_path(path), value=data))


def to_path(path, rx=re.compile("^[a-zA-Z][_0-9a-zA-Z]+$")):
    r = [path[0]]
    for x in path[1:]:
        if x.isdigit():
            r.append('[{}]'.format(x))
        elif not rx.search(x):
            r.append('["{}"]'.format(x))
        else:
            r.append('.{}'.format(x))
    return "".join(r)


def gron(data, root='json'):
    r = walk(data, root)
    return r
