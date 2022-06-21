import numpy as np
import pandas as pd
import requests

if __name__ == "__main__":
    r = requests.get("https://raw.github.com/avinash311/itrans/blob/master/js/data/DEFAULT.tsv")
    print(r.headers['Content-Type'])
    print(r.text)