from exam2pptvideo.sentence_ppt import SentencePPT
import os

class EnglishSentencePPT(SentencePPT):
  """Create Exam PPT for English study

  Attributes:
    content (list of dict): read from csv file
  """

  _template_dir = os.path.dirname(__file__)
  _templates = {
    "classic": os.path.join(_template_dir, 'templates/exam_english_classic.pptx'),
  }
  lang = 'en'

  content_keys = ["Question", "A", "B", "C", "D", "Correct", "Level", "Checkpoint", "Explanation"]

  _score_code = {
    "100": ["Perfect", "非常棒"],
    "60-90": ["Very good", "优秀如你"],
    "0-50": ["Just so so", "凑合"]
  }

  def __init__(self, sourcefile, title="", genre="classic"):
    super().__init__(sourcefile, title, genre)

