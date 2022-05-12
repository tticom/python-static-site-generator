from msilib.schema import Directory
from pathlib import Path

class Site:
  def __init__(self, source, dest):
    self.source = Path(source)
    self.dest = Path(dest)

  def create_dir(self, path):
    directory = self.dest / path.relative_to(path)
    directory.mkdir(parents=True, exist_ok=True)

  def build(self):
    self.dest.mkdir(parents=True, exist_ok=True)
    for p in self.source.rglob("*"):
      if p.is_dir(p):
        self.create_dir(p)
