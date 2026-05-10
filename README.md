# hellbox-fontmake

A hellbox job that wraps [`fontmake`](https://github.com/googlei18n/fontmake) functionality in a chute.

## Usage

- `GenerateOtf` — converts a UFO into an OTF
- `GenerateTtf` — converts a UFO into a TTF

```python
from hellbox import Hellbox
from hellbox.jobs.fontmake import GenerateOtf, GenerateTtf

with Hellbox("build") as task:
    source = task.read("*.ufo")
    source >> GenerateOtf() >> task.write("./build/otf")
    source >> GenerateTtf() >> task.write("./build/ttf")
```

## Installation

```sh
hell add hellbox-fontmake
```

## Development

```sh
uv sync
uv run pytest
```
