# dict型に配列をもたせる

## ソース

```python
# -*- coding: utf-8 -*-

DICT = {
    1:['Java', 'hoge'],
    2:['Vue.js', 'piyo']
}

INDEX_PROJECT = 0
INDEX_LOG_FILE_PATH = 1

for i in range(0, len(DICT.keys())):
    key = DICT.keys()[i]
    project = DICT[key][INDEX_PROJECT]
    logFilePath = DICT[key][INDEX_LOG_FILE_PATH]
    print('KEY:{}, Project:{}, LogFilePath:{}'.format(key,project,logFilePath))

```

## コマンド

```
python3 dict_arrays.py
```

## 実行結果

```
KEY:1, Project:Java, LogFilePath:hoge
KEY:2, Project:Vue.js, LogFilePath:piyo
```

## 参考

- [Qiita:Pythonの辞書型を使ってみる](https://qiita.com/hz1_d/items/407dd13f90a8a4533d23)
