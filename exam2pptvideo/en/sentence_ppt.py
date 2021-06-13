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
    "100": ["PERFECT", "全对了，很棒哦！去下一个等级挑战试试吧"],
    "60-90": ["VERY GOOD", "还不错哦，八啾觉得\n\"多浸泡在语言环境中可以潜移默化的提高语言能\""],
    "0-50": ["JUST SO SO", "没能及格有些遗憾，八啾觉得\n\"刷题虽苦但有用，基础扎实了才能展翅飞翔\""]
  }

  _cal_slogan = "Your score is being calculated."

  def __init__(self, sourcefile, title="", genre="classic"):
    super().__init__(sourcefile, title, genre)

