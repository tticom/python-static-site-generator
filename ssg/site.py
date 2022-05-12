from msilib.schema import Directory
from pathlib import Path

class Site:
  def __init__(self, source, dest):
    self.source = Path(source)
    self.dest = Path(dest)

  def create_dir(self, path):
    directory = self.dest / path.relative_to(path)
    Path.mkdir(directory, parents=True, exist_ok=True)

  def build(self):
    Path.mkdir(self.dest, parents=True, exist_ok=True)
    for p in self.source.rglob("*"):
      if Path.is_dir(p):
        self.create_dir(p)
