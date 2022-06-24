import csv
import re
import string
from collections import defaultdict
from itertools import chain

UNICODE_KA_CODEBLOCK_START = 0xc80
UNICODE_KA_CODEBLOCK_END = 0xcf2

codepoint_ascii_map = defaultdict(list)
codepoint_glyph_map = defaultdict(list)

def split_alt_input_reps(s):
    """Split multiple allowed input representations into a list."""
    regex_pattern = re.compile(r'[^\w\^~\.]', flags=re.ASCII)
    return [_ for _ in re.split(regex_pattern, s) if _]

def add_implicit_a(input_reps):
    """Add the implicit a to consonants - e.g. k to ka."""
    vowel_set = set('aeiou')
    ascii_lowercase_set = set(string.ascii_lowercase)
    dot_input = any([s.lower().startswith(".") for s in input_reps])
    if dot_input:
        return input_reps
    else:
        output_reps = []
        for input_rep in input_reps:
            test_set = set(input_rep.lower())
            if not test_set.isdisjoint(ascii_lowercase_set): # Has some ascii letters
                if test_set.isdisjoint(vowel_set): # No vowels
                    output_reps.append(f'{input_rep}a')
            else:
                output_reps.append(input_rep)
        return output_reps


with open('full_itrans_map.tsv', 'rt', errors='ignore', newline='') as f:
    table = csv.DictReader(f, delimiter='\t')
    for row in table:
        try:
            input_rep = row['INPUT']
            codepoint = int(row['#kannada'].rsplit('+')[-1], base=16)
            ka_letter = chr(codepoint)
        except ValueError:
            continue
        else:
            if UNICODE_KA_CODEBLOCK_START <= codepoint <= UNICODE_KA_CODEBLOCK_END:
                input_reps = split_alt_input_reps(input_rep)
                codepoint_ascii_map[codepoint] += input_reps
                codepoint_glyph_map[codepoint] += ka_letter

codepoint_ascii_map = {k: add_implicit_a(v) for k, v in codepoint_ascii_map.items()}
print(codepoint_ascii_map)
print("\n"*2)
print(codepoint_glyph_map)