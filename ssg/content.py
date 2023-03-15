import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(_delimeter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        _, fm, content = __regex.split(string, 2)
        load(fm, Loader=FullLoader)
        return cls(metadata, content)

    def __init__(self, metadata, content):
        data = metadata
        self.data = { "content": content }

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        return self.data["type"] if "type" in self.data else return None
    
    @type.setter
    def type(self, value):
        self.data["type"] = value

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        self.data.__iter__()

    def __len__(self):
        return self.data.__len__()

    def __repr__(self):
        data = dict()
        for item in self.data.items():
            if item.key != "content":
                data[item.key] = item.value
        return str(data)
