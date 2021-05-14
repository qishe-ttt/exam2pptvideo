from pdf2image import convert_from_path
from subprocess import call, DEVNULL
import os
import csv
import sys

def readCSV(filename):
  """Read csv file
  
  Args:
    filename (str): csv file name
  
  Returns:
    list of dict: records in csv file
  """
  if not os.path.isfile(filename):
    print("{} DOES NOT exist!!!".format(filename), file=sys.stderr)
    return []
  with open(filename) as csvfile:
    cursor = csv.reader(csvfile, skipinitialspace=True, delimiter='\t')
    header = next(cursor)
    return [dict(zip(header, row)) for row in cursor]

def pptx2pdf(pptx, pdffolder='./'):
  """Convert pptx into pdf

  Args:
    pptx (str): pptx file
    pdffile (str): folder that the pdf is stored in

  Returns:
    str: pdf file path 
  """
  if not os.path.isdir(pdffolder):
    os.mkdir(pdffolder) 
  call(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', pdffolder, pptx], stdout=DEVNULL)
  pdfpath = os.path.join(pdffolder, os.path.basename(pptx).split('.')[0] + '.pdf')
  return pdfpath

def pdf2images(pdfpath, imgfolder='./', start=0, end=None):
  """Convert pdf into images

  Args:
    pdfpath (str): pdf file path
    imgfolder (str): image folder. Default is current folder
    start (int): start page of pdf
    end (int): end page pdf

  Returns:
    int: number of images stored
  """
  if not os.path.isdir(imgfolder):
    os.mkdir(imgfolder) 
  images = convert_from_path(pdfpath, thread_count=2, use_pdftocairo=True, size=(1920, None), timeout=240)
  for index, image in enumerate(images[start:end]):
    image.save(os.path.join(imgfolder, str(index)+".jpg"))
  return len(images[start:end])


