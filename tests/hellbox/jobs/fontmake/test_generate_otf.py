from pathlib import Path
from unittest.mock import patch

from hellbox.source_file import SourceFile
from hellbox.jobs.fontmake import GenerateOtf


class TestGenerateOtf(object):
    def test_init(self):
        assert GenerateOtf()

    def test_flush_empty(self):
        assert GenerateOtf().flush([]) == []

    def test_process(self, tmp_path):
        source = SourceFile(Path("source.ufo"), Path("source.ufo"), tmp_path)
        with patch.object(SourceFile, "transform", return_value=source) as mock:
            GenerateOtf().process(source)
            mock.assert_called_once_with(
                'fontmake -o otf -u "{input}" --output-path "{output}"', suffix=".otf"
            )
