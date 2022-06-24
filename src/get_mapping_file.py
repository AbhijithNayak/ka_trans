import requests

r = requests.get("https://raw.githubusercontent.com/avinash311/itrans/master/js/data/DEFAULT.tsv")
with open('full_itrans_map.tsv', 'w') as f:
    f.write(r.text)