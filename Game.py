import random
class Game:

#     問題のリスト
    noList = []
#     解答のリスト
    inputList = []
#     正解するまでループ
    ans = True
#     答えた回数
    ansCount = 0
    
#     コンストラクタ ここから始まる
    def __init__(self,selectLevel):
#         難易度を数字に変換
        level = int(selectLevel)
    
#         難易度により桁数の変更
        while level+1 > len(self.noList):
            i = random.randint(1,9)
#             重複回避
            if i not in self.noList :
#                 重複しないランダムリストの生成
                self.noList.append(i)
    
        while self.ans:
#         数字の入力を要求
            self.inputNo(level)
#             解答した回数
            self.ansCount += 1
    
#           正解判定
            if level+1 == self.shougou(level):
#               正解の場合このwhileのループを終了
                self.ans = False
    
                print('正解です')
                print(f'{self.ansCount}回で正解しました')
    
    
    
#     入力の要求メソッド
    def inputNo(self, level):
        hantei = True
        while hantei:
#             リストのリセット
            self.inputList.clear()
    
#             文字で入力の要求
            inputNoStr = input(f'1～9数字を{level+1}ケタ入力してください>>')
#             空の判定
            if inputNoStr != '':
#                 数字へ変換
                inputNo = int(inputNoStr)
#                 0のみは行わない
                if inputNo != 0 :
#                     入力リストの生成
                    while inputNo != 0:
                        self.inputList.append(inputNo % 10)
                        inputNo //= 10
                    self.inputList.reverse()
    
#                     0が含まれているか
                    if 0 in self.inputList :
                        print('0が含まれています')
                    else:
#                         入力された数と問題の数が同じか
                        if level+1 == len(self.inputList):
                            hantei = False
                        else:
                            print('入力の桁数が違います')
#                             リストのリセット
                            self.inputList.clear()
    
                else:
                    print('入力してください。')
            else:
                print('入力してください。')
    
    
    def shougou(self,level):
#         部分正解の数
        bingo = 0
    
#         for文でひとつづつ照合
        for num in range(level+1):
            if self.noList[num] == self.inputList[num]:
                    bingo += 1
    
        print(f'部分正解{bingo}')
    
#         部分正解の数を返す
        return bingo




# count() 要素の中にいくつあるか