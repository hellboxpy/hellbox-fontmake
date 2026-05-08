from hellbox import Chute, Hellbox


class GenerateTtf(Chute):
    def process(self, file):
        Hellbox.info(f"Generating TTF: {file.name}")

        return file.transform(
            "fontmake -o ttf -u \"{input}\" --output-path \"{output}\"",
            suffix=".ttf"
        )
