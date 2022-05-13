from curses import meta
from importlib.abc import Loader
import re
from PyYAML import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
  __delimiter = "^(?:-|\+){3}\s*$"
  __regex = re.compile(__delimiter, re.MULTILINE)

  @classmethod
  def load(cls, string):
    _, fm, content = Content.__regex.split(string, 2)
    load(fm, Loader=FullLoader)
    return cls(metadata, content)

  class Content:
    def __init__(self, metadata, content):
      self.data = metadata
      self.data.append({"content": content})

    @property
    def body(self): return self.data["content"]

    @property
    def type(self): return self.data["type"] if "type" in self.data else None
    @property.setter
    def type(self):
      self.data["type"] = property(type)

    def __getitem__(self, key: str):
      return self.data[key] if key in self.data else None

    def __iter__(self):
      self.data.__iter__()
