import typer
from ssg import site

def main(source="content", dest="dist"):
  config ={
    "source": source,
    "dest": dest
  }
  s = site.Site(**config).build()

typer.run(main)
