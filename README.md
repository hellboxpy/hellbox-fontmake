hellbox-fontmake
================

A hellbox job that wraps [`fontmake`](https://github.com/googlei18n/fontmake) functionality in a chute.

* `GenerateOtf` — converts a UFO into an OTF
* `GenerateTtf` — converts a UFO into an TTF

```python
from hellbox.job.fontmake import GenerateOtf, GenerateTtf

with Hellbox("build") as task:
    source = task.read("*.ufo")
    source >> GenerateOtf() >> task.write("./build/otf")
    source >> GenerateTtf() >> task.write("./build/ttf")
```

Development
-----------

```shell
$ pip install -e .
$ pytest
```

Contributing
------------

To come...