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
