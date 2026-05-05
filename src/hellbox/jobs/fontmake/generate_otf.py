from hellbox import Chute, Hellbox


class GenerateOtf(Chute):
    def process(self, file):
        Hellbox.info(f"Generating OTF: {file.basename}")

        return file.transform(
            "fontmake -o otf -u \"{input}\" --output-path \"{output}\"",
            extension="otf"
        )
