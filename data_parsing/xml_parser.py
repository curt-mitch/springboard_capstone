import os
import xml.etree.ElementTree as ET
import json

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, './../datasets/japanese_english_bilingual_corpus_wikipedia_kyoto/BDS00389.xml')
tree = ET.parse(filename)
root = tree.getroot()
sentence_pairs = []

# get title values
title_els = root.findall('tit')
title_props = {}
for titles in title_els:
  for child in titles:
    if (child.tag == 'j'):
      title_props['j'] = child.text
    if (child.tag == 'e'):
      attrs = child.attrib
      if (attrs.get('type') == 'trans' and attrs.get('ver') == '2'):
        title_props['e'] = child.text
sentence_pairs.append(title_props)

# get paragraph values
paragraph_els = root.findall('par')
par_props = {}
for paragraph in paragraph_els:
  par_key = 'par-{}'.format(paragraph.attrib['id'])
  par_props[par_key] = {}
  for sentence in paragraph:
    sentence_key = 'sen-{}'.format(sentence.attrib['id'])
    par_props[par_key][sentence_key] = {}
    sentence_example = {}
    for child in sentence:
      if (child.tag == 'j'):
        sentence_example['j'] = child.text
      if (child.tag == 'e'):
        attrs = child.attrib
        if (attrs.get('type') == 'trans' and attrs.get('ver') == '2'):
          sentence_example['e'] = child.text
          sentence_pairs.append(sentence_example)

# get section values
section_els = root.findall('sec')
sec_props = {}
for section in section_els:
  sec_key = 'sec-{}'.format(section.attrib['id'])
  sec_props[sec_key] = {}
  paragraphs = section.findall('par')
  for paragraph in paragraphs:
    par_key = 'par-{}'.format(paragraph.attrib['id'])
    sec_props[sec_key][par_key] = {}
    for sentence in paragraph:
      sentence_key = 'sen-{}'.format(sentence.attrib['id'])
      sec_props[sec_key][par_key][sentence_key] = {}
      sentence_example = {}
      for child in sentence:
        if (child.tag == 'j'):
          sentence_example['j'] = child.text
        if (child.tag == 'e'):
          attrs = child.attrib
          if (attrs.get('type') == 'trans' and attrs.get('ver') == '2'):
            sentence_example['e'] = child.text
            sentence_pairs.append(sentence_example)

with open('sentence_pairs.json', 'w', encoding='utf-8') as f:
    json.dump(sentence_pairs, f, ensure_ascii=False, indent=4)
