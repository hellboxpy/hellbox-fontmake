from hellbox import Chute, Hellbox


class GenerateOtf(Chute):
    def run(self, files):
        return [self._generate(file) for file in files]

    def _generate(self, file):
        Hellbox.info(f"Generating OTF: {file.basename}")

        return file.transform(
            "fontmake -o otf -u \"{input}\" --output-path \"{output}\"",
            extension="otf"
        )
