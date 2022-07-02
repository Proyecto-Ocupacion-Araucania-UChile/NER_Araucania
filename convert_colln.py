import sys

from doccano_transformer.datasets import NERDataset
from doccano_transformer.utils import read_jsonl

filename = sys.argv[1]
mode = sys.argv[2]

#Need to find and replace label to change with labels !

with open(f"{mode}.conll", "w", encoding = "utf-8") as file:
	for entry in read_jsonl(filepath=f"{filename}", dataset=NERDataset, encoding='utf-8').to_conll2003(tokenizer=str.split):
		file.write(entry["data"] + "\n")
