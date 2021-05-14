import click
import json
from exam2pptvideo import SpanishExamPPT, SpanishExamVideo
from exam2pptvideo.lib import pptx2pdf, pdf2images
 
def _print_version(ctx, param, value):
  if not value or ctx.resilient_parsing:
      return
  click.echo(__version__)
  ctx.exit()
 
@click.command()
@click.option("--sourcecsv", prompt="source csv file path", help="Specify the source csv file path")
@click.option("--title", prompt="title of the pptx", help="Specify the title of the pptx")
@click.option("--lang", prompt="language", help="Specify the language")
@click.option("--destpptx", default="test.pptx", prompt="destination pptx file", help="Specify the destination pptx file name")
def csv2pptx(sourcecsv, title, lang, destpptx):
  _PPTS = {
    "es": SpanishExamPPT
  }

  _PPT = _PPTS[lang]

  phase = {"step": 1, "msg": "Start ppt generation"}
  print(json.dumps(phase))

  vp = _PPT(sourcecsv, title)
  vp.convert_to_ppt(destpptx)

  phase = {"step": 2, "msg": "Finish ppt generation"}
  print(json.dumps(phase))


@click.command()
@click.option("--sourcepptx", prompt="source pptx file path", help="Sepcify the source pptx file path")
@click.option("--lang", prompt="language", help="Specify the language")
@click.option("--destdir", prompt="dest pdf and pictures directory", help="Sepcify the pdf and picture destionation directory")
def pptx2video(sourcepptx, lang, destdir):
  _VIDEOS = {
    "es": SpanishExamVideo
  }

  _VIDEO = _VIDEOS[lang]

  phase = {"step": 1, "msg": "Start pdf generation"}
  print(json.dumps(phase))

  ev = _VIDEO(sourcepptx)

  ev.create_videos(destdir)


@click.command()
@click.option("--sourcepptx", prompt="source pptx file path", help="Sepcify the source pptx file path")
@click.option("--destdir", prompt="dest pdf and pictures directory", help="Sepcify the pdf and picture destionation directory")
def pptx2pdf2images(sourcepptx, destdir):
  phase = {"step": 1, "msg": "Start pdf generation"}
  print(json.dumps(phase))

  pdf = pptx2pdf(sourcepptx, destdir)

  phase = {"step": 2, "msg": "Finish pdf generation"}
  print(json.dumps(phase))

  phase = {"step": 3, "msg": "Start images generation"}
  print(json.dumps(phase))

  images_len = pdf2images(pdf, destdir)
   
  phase = {"step": 4, "msg": "Finish images generation", "images_len": images_len}
  print(json.dumps(phase))


