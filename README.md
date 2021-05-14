# Installation

```
pip3 install --verbose exam2pptvideo 
```

# Usage

Please refer to [api docs](https://qishe-ttt.github.io/exam2pptvideo/).

### Execute usage

* Validate ppt template
```
exam_pptx_validate --pptx [pptx file]
```

* Convert exam csv file into ppt file
```
exam_csv2pptx --sourcecsv [exam csv file] --lang [language] --title [title shown in ppt] --destpptx [pptx file]
```

* Convert ppt into pdf and images
```
exam_pptx2media --sourcepptx [pptx file] --destdir [dest directory storing pdf and images]
```

* Convert ppt into videos 
```
exam_pptx2video --sourcepptx [pptx file] --destdir [dest directory storing videos] --lang es
```

### Package usage
```
from exam2pptvideo import SpanishExamPPT, SpanishExamVideo
from exam2pptvideo.lib import pptx2pdf, pdf2images
 
def csv2pptx(sourcecsv, title, lang, destpptx):
  _PPTS = {
    "es": SpanishExamPPT
  }

  _PPT = _PPTS[lang]

  vp = _PPT(sourcecsv, title)
  vp.convert_to_ppt(destpptx)

def pptx2video(sourcepptx, lang, destdir):
  _VIDEOS = {
    "es": SpanishExamVideo
  }

  _VIDEO = _VIDEOS[lang]

  ev = _VIDEO(sourcepptx)

  ev.create_videos(destdir)

def pptx2pdf2images(sourcepptx, destdir):
  pdf = pptx2pdf(sourcepptx, destdir)
  images_len = pdf2images(pdf, destdir)

```

# Development

### Clone project
```
git clone https://github.com/qishe-ttt/exam2pptvideo 
```

### Install [poetry](https://python-poetry.org/docs/)

### Install dependencies
```
poetry update
```

### Test
```
poetry run pytest -rP --capture=sys
```
which run tests under `tests/*`


### Execute
```
poetry run exam_pptx_validate --help
poetry run exam_csv2pptx --help
poetry run exam_pptx2media --help
poetry run exam_pptx2video --help
```

### Create sphinx docs
```
poetry shell
cd apidocs
sphinx-apidoc -f -o source ../exam2pptvideo
make html
python -m http.server -d build/html
```

### Host docs on github pages
```
cp -rf apidocs/build/html/* docs/
```

### Build
* Change `version` in `pyproject.toml` and `exam2pptvideo/__init__.py`
* Build python package by `poetry build`

### Git commit and push

### Publish from local dev env
* Set pypi test environment variables in poetry, refer to [poetry doc](https://python-poetry.org/docs/repositories/)
* Publish to pypi test by `poetry publish -r test`

### Publish through CI 
* Github action build and publish package to [test pypi repo](https://test.pypi.org/)

```
git tag [x.x.x]
git push origin master
```

* Manually publish to [pypi repo](https://pypi.org/) through [github action](https://github.com/qishe-ttt/exam2pptvideo/actions/workflows/pypi.yml)

