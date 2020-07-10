# Benchmark Code
The file ``benchmark.py`` grabs 20 random sentence pairs from the sentence pairs JSON file.
It then submits the original Japanese sentence to Google Cloud's Translation API, and the
response is stored with the original sentence pairs as ``gc_result``. These sentences are
stored in the ``benchmark_translations`` JSON file.
