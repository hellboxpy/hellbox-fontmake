from unittest.mock import MagicMock

from hellbox.source_file import SourceFile
from hellbox.jobs.fontmake import GenerateTtf


class TestGenerateTtf(object):
    def test_init(self):
        assert GenerateTtf()

    def test_run_without_files(self):
        assert GenerateTtf().run([]) == []

    def test_run(self):
        source = SourceFile("./source", "./content")
        source.transform = MagicMock(return_value=source)

        result = GenerateTtf().run([source])

        source.transform.assert_called_with(
            "fontmake -o ttf -u \"{input}\" --output-path \"{output}\"",
            extension="ttf"
        )