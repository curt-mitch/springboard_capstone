"""
Uses Google's translation API to create a benchmark for the Japanese-English
translation Capstone project.
"""
import os
import json
import random
import six
from google.cloud import translate_v2 as translate

# open JSON file of sentence pairs
current_dir = os.path.dirname(__file__)
root_dir = os.path.join(current_dir, './..')
credentials_file_path = os.path.join(root_dir, 'credentials/Google-Cloud-a8fd3d0a789d.json')
sentences_file = open(os.path.join(root_dir, 'sentence_pairs.json'))
data = json.load(sentences_file)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_file_path
translate_client = translate.Client()

# grab 20 random sentence pairs
num_sentences = len(data) - 1
random.seed(42)
selected_sentence_pairs = []
for _ in range(20):
  i = random.randrange(0, num_sentences)
  selected_sentence_pairs.append(data[i])

# method for retrieving individual translations
def retrieve_google_translation(text):
  if isinstance(text, six.binary_type):
      text = text.decode('utf-8')

  # Text can also be a sequence of strings, in which case this method
  # will return a sequence of results for each text.
  result = translate_client.translate(
      text,
      source_language = 'ja',
      target_language='en')

  # print(u'Text: {}'.format(result['input']))
  # print(u'Translation: {}'.format(result['translatedText']))
  return result['translatedText']

benchmark_translations = []

for sentence_pair in selected_sentence_pairs:
  ja_text = sentence_pair['j']
  sentence_pair['gc_result'] = retrieve_google_translation(ja_text)
  benchmark_translations.append(sentence_pair)

with open('./benchmark/benchmark_translations.json', 'w', encoding='utf-8') as f:
    json.dump(benchmark_translations, f, ensure_ascii=False, indent=4)
