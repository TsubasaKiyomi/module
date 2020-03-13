
# import say_twiceはファンクションだけをimportする。
# from lesson_package.utils import say_twice
# from lesson_package import utils
# from lesson_package.__pycache__.talk import human
# from lesson_package.__pycache__.talk import animal
# from lesson_package.__pycache__.talk import *
# as 「　」　を使うとutilsの部分が略せる。
# importでlesson_packageというフォルダからディレクトリは「.ドット」で、モジュールはutilsを呼び出す。
# import lesson_package.utils
# utilsファイルの関数say_twice引数（'hello'）を入れて出力すると
# r = lesson_package.utils.say_twice('hello')
# hello! hello!が出力される。
# print(r)

# fromにlesson_packageを入れるのでここには記入しない。
# r = utils.say_twice('hello')

# print(r)


# r = say_twice('hello')

# print(r)


# print(animal.sing())
# print(animal.cry())
# print(human.sing())
# print(human.cry())

# tryのimportが成功すれば次にいくが、utilsを移動し他ので、エラーとなる。
# try:
#     from lesson_package import utils
# exceptのimportが読み込まれ、成功して次の行へいく。
# except ImportError:
#     from lesson_package.tools import utils

# utils.say_twice('word')


