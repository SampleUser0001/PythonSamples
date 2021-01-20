# -*- encoding: utf-8 -*- 

DICT = {
    1:['Java', 'hoge'],
    2:['Vue.js', 'piyo']
}

DICT_KEY_LIST = [1,2]

INDEX_PROJECT = 0
INDEX_LOG_FILE_PATH = 1

for i in range(0, len(DICT_KEY_LIST)):
    key = DICT_KEY_LIST[i]
    project = DICT[key][INDEX_PROJECT]
    logFilePath = DICT[key][INDEX_LOG_FILE_PATH]
    print('KEY:{}, Project:{}, LogFilePath:{}'.format(key,project,logFilePath))

