# -*- encoding: utf-8 -*-
import csv

with open('file.tsv', mode='r', newline='', encoding='utf-8') as f:
    # csvと同じ方法で読み込む。デリミタが違う。
    tsv_reader = csv.DictReader(f, delimiter='\t')
    for row in tsv_reader:
        print(row)
        print("key:" + row["key"])
        print("value:" + row["value"])
        print("int:" + row["int"])
        print()