from work.Game import Game
# import random
# print(random.randint(1,9))

print('数あてゲーム')


select = True
while select:
    level = input('難易度を選択してください（1:EASY 2:NORMAL 3:HERD）>>')
#     未入力でないかつ、4以下かつ、0でない数字
    if level != '' and int(level) < 4 and int(level) != 0:
        game = Game(level)
        select = False
    else:
        print('入力してください')

