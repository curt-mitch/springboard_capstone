import os, json

current_dir = os.path.dirname(__file__)
data_path = os.path.join(current_dir, './../datasets/jesc-corpus.txt')

sentence_pairs = []
with open(data_path, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')
for line in lines:
    pair = {}
    split = line.split('\t')
    if len(split) == 2:
      english_text, japanese_text = split
      pair['e'] = english_text
      pair['j'] = japanese_text
      sentence_pairs.append(pair)

with open('subtitle_corpus.json', 'w', encoding='utf-8') as f:
    json.dump(sentence_pairs, f, ensure_ascii=False, separators=(',', ":"))
