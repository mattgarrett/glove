import gflags
import sys
import os

FLAGS = gflags.FLAGS

gflags.DEFINE_string("sprite_directory", None, "Full path to sprite directory.",
        short_name="d")

SPRITE_FILE_ENDINGS = {
        ".png"
        }

FILE_ENDING_LENGTH = 4

class SpriteHandlerGenerator(object):

    MAIN_TEMPLATE = [
            "import pygame.image",
            "",
            "",
            "class NoSuchSpriteException(Exception):",
            "   pass",
            "",
            "",
            "class SpriteHandler(object):",
            "",
            "   sprites = {}",
            "",
            "   def __init__(self, absSpritePath):",
            "       self.absSpritePath = absSpritePath",
            "",
            "   def getSprite(self, reference):",
            "       if hasattr(Sprites, reference):",
            "           spriteId = getattr(Sprites, reference)",
            "           if spriteId not in self.sprites:",
            ("               self.sprites[spriteId] = "
                "pygame.image.load(self.absSpritePath + self.FILEPATHS[spriteId])"),
            "           return self.sprites[spriteId]",
            "       else:",
            "           raise NoSuchSpriteException()",
            "",
            ""
            ]

    SPRITES_TEMPLATE = [
            "class Sprites:",
            ""
            ]

    FILEPATH_TEMPLATE_START = "   FILEPATHS = {\n"

    FILEPATH_TEMPLATE_END = "   }"

    def __init__(self):
        pass

    def generate(self, spriteFiles):
        references = self.createReferences(spriteFiles)

        generated = "\n".join(self.SPRITES_TEMPLATE)
        generated += self.generateConstants(references)
        generated += "\n"
        generated += "\n"
        generated += "\n"
        generated += "\n".join(self.MAIN_TEMPLATE)
        generated += self.generateFilepaths(references, spriteFiles)
        generated += "\n"

        return generated

    def generateFilepaths(self, references, spriteFiles):
        filePathDict = self.FILEPATH_TEMPLATE_START

        zippedTogether = zip(references, spriteFiles)
        filePathDict += "\n".join(map(
            lambda rf: "        Sprites." + rf[0] + ": \"" + rf[1] + "\",",
            zippedTogether))

        filePathDict += "\n"
        filePathDict += self.FILEPATH_TEMPLATE_END

        return filePathDict

    def generateConstants(self, references):
        definitions = map(lambda r: r + " = \"" + r + "\"", references)
        return "\n    " + "\n    ".join(definitions)

    def createReferences(self, spriteFiles):
        fileNames = map(lambda f: os.path.basename(f), spriteFiles)
        withoutFileEnding = map(lambda f: str(f[:-FILE_ENDING_LENGTH]), fileNames)
        return map(lambda f: f.upper(), withoutFileEnding)
        


def main():
    FLAGS(sys.argv)
    generator = SpriteHandlerGenerator()

    spriteFiles = filter(
            lambda x: str(x[-FILE_ENDING_LENGTH:]) in SPRITE_FILE_ENDINGS,
            os.listdir(FLAGS.sprite_directory))

    print generator.generate(spriteFiles)


if __name__ == "__main__":
    main()
