from exam2pptvideo.vocab_phrase_ppt import VocabPhrasePPT
import os

class GermanVocabPhrasePPT(VocabPhrasePPT):
  """Create Exam PPT for German study

  Attributes:
    content (list of dict): read from csv file
  """

  _template_dir = os.path.dirname(__file__)
  _templates = {
    "classic": os.path.join(_template_dir, 'templates/exam_german_classic.pptx'),
  }
  lang = 'de'

  content_keys = ["Question", "A", "B", "C", "D", "Correct", "Level", "Checkpoint", "Explanation_A", "Explanation_B", "Explanation_C", "Explanation_D"]

  _score_code = {
    "100": ["PERFEKT", "全对了，很棒哦！去下一个等级挑战试试吧"],
    "60-90": ["SEHR GUT", "还不错哦，八啾觉得\n\"多浸泡在语言环境中可以潜移默化的提高语言能\""],
    "0-50": ["SO LALA", "没能及格有些遗憾，八啾觉得\n\"刷题虽苦但有用，基础扎实了才能展翅飞翔\""]
  }
  
  _cal_slogan = "Ihre Punktzahl wird nun berechnet."

  def __init__(self, sourcefile, title="", genre="classic"):
    super().__init__(sourcefile, title, genre)

