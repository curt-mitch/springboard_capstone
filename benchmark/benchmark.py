"""
Uses Google's translation API to create a benchmark for the Japanese-English
translation Capstone project.
"""
import os
import json
import random
from google.cloud import translate_v2 as translate

# open JSON file of sentence pairs
current_dir = os.path.dirname(__file__)
root_dir = os.path.join(current_dir, './..')
f = open(os.path.join(root_dir, 'sentence_pairs.json'))
data = json.load(f)

# grab 20 random sentence pairs
num_sentences = len(data) - 1
random.seed(42)
benchmark_sentence_pairs = []
for _ in range(20):
  i = random.randrange(0, num_sentences)

  benchmark_sentence_pairs.append(data[i])


translate_client = translate.Client()
text = benchmark_sentence_pairs[0]
if isinstance(text, six.binary_type):
    text = text.decode('utf-8')

# Text can also be a sequence of strings, in which case this method
# will return a sequence of results for each text.
result = translate_client.translate(
    text,
    source_language = 'jp',
    target_language='en')

print(u'Text: {}'.format(result['input']))
print(u'Translation: {}'.format(result['translatedText']))
print(u'Detected source language: {}'.format(
    result['detectedSourceLanguage']))
