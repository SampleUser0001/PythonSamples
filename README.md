# PythonSamples
Pythonのサンプル集

- [PythonSamples](#pythonsamples)
  - [一覧](#一覧)
    - [tsv読み込み](#tsv読み込み)
  - [参考](#参考)

## 一覧

| タイトル | 概要 | リンク |
| :-- | :-- | :-- |
| tsv読み込み | - | [readtsv.py](./001_readtsv/readtsv.py) |
| classの宣言と使用 | - | [README.md](./002_class/README.md) |

### tsv読み込み

```tsv:file.tsv
key	value	int
hoge	aaa	001
piyo	bbb	002
fuga	ccc	003
```

実行コマンド
```
python3 readtsv.py
```

実行結果
```
OrderedDict([('key', 'hoge'), ('value', 'aaa'), ('int', '001')])
key:hoge
value:aaa
int:001

OrderedDict([('key', 'piyo'), ('value', 'bbb'), ('int', '002')])
key:piyo
value:bbb
int:002

OrderedDict([('key', 'fuga'), ('value', 'ccc'), ('int', '003')])
key:fuga
value:ccc
int:003
```
## 参考

- [Pythonドキュメント](https://docs.python.org/ja/3/)
- [Qiita:pythonでのcsvファイルの読み込み](https://qiita.com/motoki1990/items/0274d8bcf1a97fe4a869)