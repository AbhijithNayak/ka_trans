import requests
import csv
from collections import defaultdict, namedtuple

r = requests.get("https://raw.githubusercontent.com/avinash311/itrans/master/js/data/DEFAULT.tsv")
print(r.headers['Content-Type'])
with open('full_itrans_map.tsv', 'w') as f:
    f.write(r.text)

UNICODE_KA_CODEBLOCK_START = 0xc80
UNICODE_KA_CODEBLOCK_END = 0xcf2

codepoint_dict = defaultdict(tuple)
AsciiGlyphMap = namedtuple('AsciiGlyphMap', ['ascii_letters', 'glyphs'])

with open('full_itrans_map.tsv', 'rt', errors='ignore', newline='') as f:
    table = csv.DictReader(f, delimiter='\t')
    for row in table:
        try:
            input_representation = row['INPUT']
            codepoint = int(row['#kannada'].rsplit('+')[-1], base=16)
            ka_letter = chr(codepoint)
        except ValueError:
            continue
        else:
            if UNICODE_KA_CODEBLOCK_START <= codepoint <= UNICODE_KA_CODEBLOCK_END:
                print(input_representation, codepoint, ka_letter, sep='\t')
