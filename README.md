# BETO NET Araucania

## Summary

Repository containing the production elements of a NER model with pre-training of the [BETO: Spanish BERT](https://github.com/dccuchile/beto) model.

`colab/` contains the notebooks used for the development

`data/` contains annotated terrain data (MISC, LOC, DATE, PERS, ORG) in CoNLL or JSONL format (from the Doccano platform)

`convert_colln.py` -- conversion of JSONL data via Doccano-transformers

`convert_json.py` -- convert JSONL data to [BILOU annotation](https://github.com/abtExp/doccano_to_bilou)
