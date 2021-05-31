from exam2pptvideo.exam_video import ExamVideo
import os

class EnglishExamVideo(ExamVideo):
  """Create Exam Video for English study

  Attributes:
    slides (list of Slide): read from pptx file
  """

  _soundindex = {
    "Cover": "cover.m4a",
    "Question": "question.m4a",
    "Question with choices": "question.m4a",
    "Analysis": "analysis.m4a",
    "Analysis with choices": "analysis.m4a",
    "Correct": "correct.m4a",
    "Wrong": "wrong.m4a",
    "Calculation": "calculate.m4a",
    "100": "Perfect.m4a",
    "60-90": "Very_good.m4a",
    "0-50": "Just_so_so.m4a"
  }

  lang = 'en'

  def __init__(self, sourceppt):
    super().__init__(sourceppt)
    _sound_dir = os.path.join(os.path.dirname(__file__), 'soundaffects')
    self.soundaffects = {k:os.path.join(_sound_dir, v) for k, v in self.__class__._soundindex.items()}

  def _get_slide_sound(self, i):
    slide = self.slides[i]
    slide_name = slide.name
    slide_type = slide.slide_layout.name
    if slide_type == "Score": 
      slide_type = slide_name 
    # TODO: will be modified according to specified language
    return self.soundaffects[slide_type]

