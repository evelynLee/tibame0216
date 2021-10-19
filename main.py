# 費式數列
import sys

in_txt = sys.stdin.read()

num = int(in_txt) - 1

first_num = 0
second_num = 1

if num == 0:
  print(0)
elif num == 1:
  print(1)
else:
  i = 0
  while i < num - 1:
    # ans = first_num + second_num
    # first_num = second_num
    # second_num = ans
    # print(ans)
    # i += 1

    first_num, second_num = second_num, first_num + second_num
    i += 1
  print(second_num)

# -------------------

# # f = open('file.txt', 'r')

# # print(f.read())

# # f.close() --> 若忘了, 只能重開機關掉

# # 用下面的方法寫, 無論怎樣都會關掉
# # 讀取用 'r'
# # 寫入用 'w', 而且直接寫入到 file.txt 中
# with open('file.txt', 'w', encoding='utf-8') as f:
#   # print(f.read())
#   f.write('Today is a hot day')

# ---------------

# 繼承詳解
# C create
# R read
# U update
# D delete

# class Crud():
#   def get_data(self):
#     return 100

# class MoneyCrud(Crud):
#   def 
# 待完成


# # 物件導向 
# #     駝峰命名法 字母的第一字大寫
# class Chair():

#   def __init__(self, c):
#     self.color = c

#   def seat(self):
#     print(self.color, '的椅子很舒服')
#   # def set_color(self, c):
#   #   self.color = c

# class Sofa(Chair):
#   def lay(self):
#     print('我可以躺喔')

#   def seat(self):
#     super().seat()
#     print('我是沙發我複寫了seat')

# # 變數命名用蛇形 **_***
# a_chair = Chair('Green')
# a_chair.seat()

# a_sofa = Sofa('YellowGreen')
# # a_chair.color = 'Green'
# # a_chair.set_color('Green')
# a_sofa.seat()

# # b_chair = Chair('Yellow')
# # b_chair.seat()
# # b_chair.color = 'Yellow'
# # b_chair.set_color('Yellow')

# # print(a_chair.color)
# # print(b_chair.color)
# # Chair.seat(要執行的物件)
# # Chair.seat(a_chair)
# # -------------------------------------

# def make_drink(product_name='珍奶'):
#   drink = product_name

#   return drink

# # input_product = input('請問要喝什麼飲料? ')

# my_drink = make_drink()

# print(my_drink + '完成了')

# # ---------

# a = make_drink

# b = a('百香綠茶') + '完成了'

# print(b)

# ------------------------------

# std2 = {
#   'name': 'Amy', 
#   'no': 2

# }

# ------------------------------

# std2 = {'name': 'Amy', 'no': 2}
# std3 = {'name': 'John', 'no': 3}

# stds = [std2, std3]

# print(stds)

# for std in stds:
#   # print(std['name'])
#   print(std.get('name'))

# -----------------------------

# id_data = {
#   'A':10,
#   'B':11,
# }

# my_id = 'A123456789'

# print(id_data[my_id[0]])

# -----------------------------

# str_list = ['1', '2', '3']

# # for s in str_list:

# print([str(i) for i in str_list])

# -------------------------------

# 型別轉換

# import sys

# in_txt = sys.stdin.read()

# # 另一個方法
# a_list = in_txt.split()

# ans_list = []

# i = 0
# while i < len(a_list):
#   ans_list.append(str(int(a_list[i]) + 1))
#   i += 1

# print(' '.join(ans_list))

# ------------------------------------
# # 把一組數字切成一組 list
# a_list = in_txt.split()

# # 設定一個空字串
# ans = ""

# # list 中的每一個數字都+1 
# i = 0

# while i < len(a_list):
# #用字串的型別把該組數字加回 list 中 
#   ans += str(int(a_list[i]) + 1) + ' '
#   i += 1

# #移除最後一個空白
# print(ans.strip())

# ---------------------------------

# 指定乘法表

# import sys

# in_txt = sys.stdin.read()

# in_num = in_txt.split()

# in1 = int(in_num[0])
# in2 = int(in_num[1])

# i = 0
# while i < in1:
#   j = 0
#   while j < in2:
#     print(f'{i+1}X{j+1}={(i+1)*(j+1)}')
#     j += 1
#   i += 1

# ----------------------------

# 簡易計算機

# import sys
# in_calcu = sys.stdin.read()

# if '+' in in_calcu:
#   result = in_calcu.split('+')
#   print(int(result[0]) + int(result[1]))
# elif '-' in in_calcu:
#   result = in_calcu.split('-')
#   print(int(result[0]) - int(result[1]))
# elif '*' in in_calcu:
#   result = in_calcu.split('*')
#   print(int(result[0]) * int(result[1]))
# else:
#   result = in_calcu.split('/')
#   print(int(int(result[0]) / int(result[1])))


# 判斷是否為閏年的程式
# import sys
# in_year = int(sys.stdin.read())
# # in_year = int(input('?'))

# if in_year % 4 != 0:
#   print(False)

# if in_year % 4 == 0 and in_year % 100 != 0:
#   print(True)

# if in_year % 100 == 0 and in_year % 400 != 0:
#   print(False)

# if in_year % 400 == 0:
#   print(True)



#--------------------------------

# 把 list 中的每個數字 + 1
# a = [1, 2, 3, 4, 5]

# i = 0

# ans = ''
# while i < len(a):
#   ans += str(a[i] + 1) + ' '
#   i += 1
# print(ans.strip())

# ------------------------------------------

# 佚代加總

# import sys

# in_txt = sys.stdin.read()

# total = 0
# i = 1
# while i <= int(in_txt):
#   total += i
#   i += 1
# print(total)


# ---------------------------------------

# i = 0

# while i < 13:
#   print(i+1)

#   j = 0
  
#   while j < 15:
#     print(f'{i + 1}X{j + 1} = {(i + 1) * (j + 1)}')
#     j += 1


#   i += 1

# -------------------------------------

# i = 0

# j = int(input('?'))

# while i <= j:
#   print(f'Hello {i + 1}')
#   i += 1

# ----------------------------------
# import sys

# in_ID = sys.stdin.read()

# check_ID = 0

# if in_ID[0] == "A":
#   check_ID += 1 + 0 * 9
# elif in_ID[0] == "B":
#   check_ID += 1 + 1 * 9
# elif in_ID[0] == "C":
#   check_ID += 1 + 2 * 9
# elif in_ID[0] == "D":
#   check_ID += 1 + 3 * 9
# elif in_ID[0] == "E":
#   check_ID += 1 + 4 * 9
# elif in_ID[0] == "F":
#   check_ID += 1 + 5 * 9
# elif in_ID[0] == "G":
#   check_ID += 1 + 6 * 9
# elif in_ID[0] == "H":
#   check_ID += 1 + 7 * 9
# elif in_ID[0] == "I":
#   check_ID += 3 + 4 * 9
# elif in_ID[0] == "J":
#   check_ID += 1 + 8 * 9
# elif in_ID[0] == "K":
#   check_ID += 1 + 9 * 9
# elif in_ID[0] == "L":
#   check_ID += 2 + 0 * 9
# elif in_ID[0] == "M":
#   check_ID += 2 + 1 * 9
# elif in_ID[0] == "N":
#   check_ID += 2 + 2 * 9
# elif in_ID[0] == "O":
#   check_ID += 3 + 5 * 9
# elif in_ID[0] == "P":
#   check_ID += 2 + 3 * 9
# elif in_ID[0] == "Q":
#   check_ID += 2 + 4 * 9
# elif in_ID[0] == "R":
#   check_ID += 2 + 5 * 9
# elif in_ID[0] == "S":
#   check_ID += 2 + 6 * 9
# elif in_ID[0] == "T":
#   check_ID += 2 + 7 * 9
# elif in_ID[0] == "U":
#   check_ID += 2 + 8 * 9
# elif in_ID[0] == "V":
#   check_ID += 2 + 9 * 9
# elif in_ID[0] == "W":
#   check_ID += 3 + 2 * 9
# elif in_ID[0] == "X":
#   check_ID += 3 + 0 * 9
# elif in_ID[0] == "Y":
#   check_ID += 3 + 1 * 9
# else:
#   check_ID += 3 + 3 * 9

# check_ID +=  int(in_ID[1]) * 8
# check_ID +=  int(in_ID[2]) * 7
# check_ID +=  int(in_ID[3]) * 6
# check_ID +=  int(in_ID[4]) * 5
# check_ID +=  int(in_ID[5]) * 4
# check_ID +=  int(in_ID[6]) * 3
# check_ID +=  int(in_ID[7]) * 2
# check_ID +=  int(in_ID[8]) * 1
# check_ID +=  int(in_ID[9]) * 1

# if check_ID % 10 == 0:
#   print('合法')
# else:
#   print('不合法')


# ---------------------------------------------

# import sys

# in_num = sys.stdin.read()

# in_1list = in_num.split(',')

# my_list = in_1list[0].split()

# AI_list = in_1list[1].split()

# print(in_1list)
# print(my_list)
# print(AI_list)

# bingo = 0

# if my_list[0] in AI_list:
#   bingo = bingo + 1

# if my_list[1] in AI_list:
#   bingo = bingo + 1 

# if my_list[2] in AI_list:
#   bingo = bingo + 1

# if my_list[3] in AI_list:
#   bingo = bingo + 1

# if my_list[4] in AI_list:
#   bingo = bingo + 1

# if bingo < 3:
#   print(0)
# elif bingo == 3 :
#   print(100)
# elif bingo == 4 :
#   print(1000)
# else:
#   print(10000)

# ------------------------------------------------
# import sys

# in_txt = sys.stdin.read()

# no_open = ['星期五', '星期六', '星期日']

# stock1_list = in_txt.split()

# a = stock1_list[0]
# b = int(stock1_list[1])
# c = int(stock1_list[2])

# if a in no_open:
#   print('不開市')
# else:
#   print(b * c)


#-------------------------------------------------
# import random

# key_word = ['剪刀','石頭','布']

# user = int(input('[0]剪刀, [1]石頭, [2]布:'))

# ran_num = random.randint(0, 2)

# print('你出了: ', key_word[user])
# print('電腦出了: ', key_word[ran_num])

# if user == ran_num:
#   print ('平手')
# elif user == (ran_num +1) % 3:
#   print ('You win')
# else:
#   print ('You lose')