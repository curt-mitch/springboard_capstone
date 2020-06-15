import os
import xml.etree.ElementTree as ET

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, './../datasets/japanese_english_bilingual_corpus_wikipedia_kyoto/BDS00389.xml')
tree = ET.parse(filename)
root = tree.getroot()

# get title values
title_el = root.find('tit')
title_props = {}
for child in title_el:
  if (child.tag == 'j'):
    title_props['j'] = child.text
  if (child.tag == 'e'):
    attrs = child.attrib
    if (attrs.get('type') == 'trans' and attrs.get('ver') == '2'):
      title_props['e'] = child.text

print(title_props)
