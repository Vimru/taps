from text_format import printColor
from config import *
import requests

def fetchSecJson(addr):
    try:
        response = requests.get(addr)
        return response.json()
    except Exception as e:
        printColor("Fatal error while fetching data from " + addr + ":", RED)
        printColor(e, RED)
        exit()

