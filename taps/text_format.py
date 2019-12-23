import colorful
from taps import user_config

def genColorText(text, color):
    # Check color is enabled.
    if user_config["COLORS"]["COLOR"] == "yes":
        try:
            return getattr(colorful, color)(text)
        except:
            print("Invalid color: " + str(color))
            return text
    return text

def printColor(text, color):
    print(genColorText(text, color))
