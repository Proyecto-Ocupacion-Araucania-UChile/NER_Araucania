from doccano_transformer.datasets import NERDataset
from doccano_transformer.utils import read_jsonl
with open("test.dataset", "w", encoding = "utf-8") as file:
    for entry in read_jsonl(filepath='annot_araucania_maj.jsonl', dataset=NERDataset, encoding='utf-8').to_conll2003(tokenizer=str.split):
        file.write(entry["data"] + "\n")
