# dict型 存在しないキーの扱い

## 実装

```python
# -*- coding: utf-8 -*-

DICT = {
    1:{'Project':'Java', 'LogFilePath':'hogehoge'},
    2:{'Project':'Vue.js', 'LogFilePath':'piyopiyo'}
}

# キーがある
print(DICT.get(1).get('Project'))

# キーがない
print(DICT.get(3, 'NotFound'))

# これはできる
print(DICT.get(1).get('HOGE','NotFound'))

# これはできない
print(DICT.get(3).get('Project', 'NotFound'))
```

実行
```
python3 notFoundKey.py
```

実行結果
```
Java
NotFound
NotFound
Traceback (most recent call last):
  File "notFoundKey.py", line 18, in <module>
    print(DICT.get(3).get('Project', 'NotFound'))
AttributeError: 'NoneType' object has no attribute 'get'
```
