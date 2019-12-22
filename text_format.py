import colorful
import config

def genColorText(text, color):
    # Check color is enabled.
    if config.COLOR:
        return getattr(colorful, color)(text)
    return text

def printColor(text, color):
    print(genColorText(text, color))
