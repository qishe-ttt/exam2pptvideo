from exam2pptvideo.exam_video import ExamVideo
import os

class SpanishExamVideo(ExamVideo):
  """Create Exam Video for Spanish study

  Attributes:
    slides (list of Slide): read from pptx file
  """

  _soundindex = {
    "Cover": "cover.m4a",
    "Sentence": "question.m4a",
    "Sentence with choices": "question.m4a",
    "Sentence analysis": "analysis.m4a",
    "Sentence analysis with choices": "analysis.m4a",
    "VocabPhrase": "question.m4a",
    "VocabPhrase with choices": "question.m4a",
    "VocabPhrase analysis": "analysis.m4a",
    "VocabPhrase analysis with choices": "analysis.m4a",
    "Correct": "correct.m4a",
    "Wrong": "wrong.m4a",
    "Calculation": "calculate.m4a",
    "100": "100.m4a",
    "60-90": "60-90.m4a",
    "0-50": "0-50.m4a"
  }

  lang = 'es'

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

