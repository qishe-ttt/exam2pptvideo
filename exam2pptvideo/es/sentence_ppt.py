from exam2pptvideo.sentence_ppt import SentencePPT
import os

class SpanishSentencePPT(SentencePPT):
  """Create Exam PPT for Spanish study

  Attributes:
    content (list of dict): read from csv file
  """

  _template_dir = os.path.dirname(__file__)
  _templates = {
    "classic": os.path.join(_template_dir, 'templates/exam_spanish_classic.pptx'),
  }
  lang = 'es'

  _score_code = {
    "100": ["Perfecto", "非常棒"],
    "60-90": ["Muy bien", "优秀如你"],
    "0-50": ["Asi Asi", "凑合"]
  }

  content_keys = ["Question", "A", "B", "C", "D", "Correct", "Level", "Checkpoint", "Explanation"]

  def __init__(self, sourcefile, title="", genre="classic"):
    super().__init__(sourcefile, title, genre)

