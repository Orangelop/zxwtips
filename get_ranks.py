#get_ranks 获取学生本人任意一次考试成绩以及排名
#pip3 install zhixuewang
from zhixuewang import *

user = input("输入用户名: ")
passwd = input("输入密码: ")

get = login(user,passwd)

print("//////////打印考试列表//////////")
exams_list = get.get_exams()
for aexam in exams_list:
    print("考试id: {}, 考试名称: {}".format(aexam.id, aexam.name))
print("//////////考试列表结束//////////")

print("//////////打印考试成绩//////////")
grades = get.get_self_mark(input("输入考试id: "))
# debug
# print(list(grades))#['subject'])
for grade in grades:
    # check availability
    if grade.grade_rank == 0:
        grade.grade_rank = "Not availavable"
    if grade.class_rank == 0:
        grade.class_rank = "Not availavable"
    if grade.score == 0:
        grade.score = "Not availavable"
    print('科目:',grade.subject.name,";",'成绩:',grade.score,";",'班级排名:',grade.class_rank,";",'年级排名:',grade.grade_rank,";")
print("//////////考试成绩结束//////////")