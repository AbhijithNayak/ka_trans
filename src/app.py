import requests
import csv

r = requests.get("https://raw.githubusercontent.com/avinash311/itrans/master/js/data/DEFAULT.tsv")
print(r.headers['Content-Type'])
with open('full_itrans_map.tsv', 'w') as f:
    f.write(r.text)

with open('full_itrans_map.tsv', 'rt', errors='ignore', newline='') as f:
    table = csv.DictReader(f, delimiter='\t')
    for row in table:
        ka_info = (row['INPUT'], row['CODE-NAME'], row['#kannada'])
        if all(ka_info):
            try:
                ascii_letter, code_name, ka_letter = (row['INPUT'], row['CODE-NAME'], chr(int(row['#kannada'].rsplit('+')[-1], base=16)))
            except ValueError:
                continue
            else:
                print(ascii_letter, ka_letter, sep='\t')
