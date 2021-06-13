from exam2pptvideo.vocab_phrase_ppt import VocabPhrasePPT
import os

class SpanishVocabPhrasePPT(VocabPhrasePPT):
  """Create Exam PPT for Spanish study

  Attributes:
    content (list of dict): read from csv file
  """

  _template_dir = os.path.dirname(__file__)
  _templates = {
    "classic": os.path.join(_template_dir, 'templates/exam_spanish_classic.pptx'),
  }
  lang = 'es'

  content_keys = ["Question", "A", "B", "C", "D", "Correct", "Level", "Checkpoint", "Explanation_A", "Explanation_B", "Explanation_C", "Explanation_D"]

  _score_code = {
    "100": ["PERFECTO", "全对了，很棒哦！去下一个等级挑战试试吧"],
    "60-90": ["MUY BIEN", "还不错哦，八啾觉得\"多浸泡在语言环境中可以潜移默化的提高语言能\"" ],
    "0-50": ["ASI ASI", "没能及格有些遗憾，八啾觉得\"刷题虽苦但有用，基础扎实了才能展翅飞翔\""]
  }

  _cal_slogan = "Se está calculando tu puntuación."

  def __init__(self, sourcefile, title="", genre="classic"):
    super().__init__(sourcefile, title, genre)

