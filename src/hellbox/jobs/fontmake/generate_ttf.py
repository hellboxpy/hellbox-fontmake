from hellbox import Chute, Hellbox


class GenerateTtf(Chute):
    def process(self, file):
        Hellbox.info(f"Generating TTF: {file.basename}")

        return file.transform(
            "fontmake -o ttf -u \"{input}\" --output-path \"{output}\"",
            extension="ttf"
        )
