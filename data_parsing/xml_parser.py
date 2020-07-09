import os
import xml.etree.ElementTree as ET
import json

def parse_file(filename):
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
  return sentence_pairs

# with open('sentence_pairs.json', 'w', encoding='utf-8') as f:
#     json.dump(sentence_pairs, f, ensure_ascii=False, indent=4)

current_dir = os.path.dirname(__file__)
datasets_dir = os.path.join(current_dir, './../datasets/japanese_english_bilingual_corpus_wikipedia_kyoto/wiki_corpus_2.01')
bds_dir = os.path.join(datasets_dir, 'BDS')
bld_dir = os.path.join(datasets_dir, 'BLD')
clt_dir = os.path.join(datasets_dir, 'CLT')
epr_dir = os.path.join(datasets_dir, 'EPR')
fml_dir = os.path.join(datasets_dir, 'FML')
gnm_dir = os.path.join(datasets_dir, 'GNM')
hst_dir = os.path.join(datasets_dir, 'HST')
ltt_dir = os.path.join(datasets_dir, 'LTT')
pnm_dir = os.path.join(datasets_dir, 'PNM')
rlw_dir = os.path.join(datasets_dir, 'RLW')
rod_dir = os.path.join(datasets_dir, 'ROD')
sat_dir = os.path.join(datasets_dir, 'SAT')
scl_dir = os.path.join(datasets_dir, 'SCL')
snt_dir = os.path.join(datasets_dir, 'SNT')
ttl_dir = os.path.join(datasets_dir, 'TTL')

dir_list = [bds_dir, bld_dir, clt_dir, epr_dir, fml_dir, gnm_dir, hst_dir, ltt_dir,
            pnm_dir, rlw_dir, rod_dir, sat_dir, scl_dir, snt_dir, ttl_dir]

for data_dir in dir_list:
  directory_sentence_list = []
  for subdir, dirs, files in os.walk(data_dir):
    for file in files:
      file_sentences = parse_file(os.path.join(subdir, file))
      directory_sentence_list = directory_sentence_list + file_sentences
  print(len(directory_sentence_list))
