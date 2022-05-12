import typer
from ssg import Site

def main(source="content", dest="dist"):
  config ={
    "source": source,
    "dest": dest
  }
  Site(**config).build()

typer.run(main)
