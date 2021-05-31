from exam2pptvideo.sentence_ppt import SentencePPT
import os

class GermanSentencePPT(SentencePPT):
  """Create Exam PPT for German study

  Attributes:
    content (list of dict): read from csv file
  """

  _template_dir = os.path.dirname(__file__)
  _templates = {
    "classic": os.path.join(_template_dir, 'templates/exam_german_classic.pptx'),
  }
  lang = 'de'

  content_keys = ["Question", "A", "B", "C", "D", "Correct", "Level", "Checkpoint", "Explanation"]

  _score_code = {
    "100": ["Perfekt", "非常棒"],
    "60-90": ["Sehr gut", "优秀如你"],
    "0-50": ["So lala", "凑合"]
  }

  def __init__(self, sourcefile, title="", genre="classic"):
    super().__init__(sourcefile, title, genre)

