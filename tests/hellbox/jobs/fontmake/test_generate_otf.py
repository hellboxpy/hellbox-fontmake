from unittest.mock import MagicMock

from hellbox.source_file import SourceFile
from hellbox.jobs.fontmake import GenerateOtf


class TestGenerateOtf(object):
    def test_init(self):
        assert GenerateOtf()

    def test_run_without_files(self):
        assert GenerateOtf().run([]) == []

    def test_run(self):
        source = SourceFile("./source", "./content")
        source.transform = MagicMock(return_value=source)

        result = GenerateOtf().run([source])

        source.transform.assert_called_with(
            "fontmake -o otf -u \"{input}\" --output-path \"{output}\"",
            extension="otf"
        )