from taps.text_format import printColor
from taps import user_config
import requests

def fetchSecJson(addr):
    try:
        response = requests.get(addr)
        return response.json()
    except Exception as e:
        printColor("Fatal error while fetching data from " + addr + ":", user_config["COLORS"]["Red"])
        printColor(e, user_config["COLORS"]["Red"])
        exit()

