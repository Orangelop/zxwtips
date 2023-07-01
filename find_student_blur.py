#find_stu 在本年级年级中利用学生姓名查询所在班级、性别、person-id(支持简易模糊查找)
#调用api次数会很多，一次查询调用约20次，慎用，建议在每次调用后sleep5s
#pip3 install zhixuewang

from zhixuewang import *
#import time

#use account and passwd
user=input("输入用户名: ")
passwd=input("输入密码: ")

#or use login_student_id()
get = login(user,passwd)

to_be_queried_student = str(input("输入要查询的学生姓名(支持简易模糊查找): "))
class_list = get.get_clazzs()
result = 0
for aclass in class_list:
    class_id = aclass.id
    student_list = get.get_classmates(aclass.id)
    print("在{}中查找. ".format(aclass.name))
    for student in student_list:
        if to_be_queried_student in student.name:
            print("一个结果. ", "person-id:", student.id, "name:", student.name, "class:", student.clazz.name, "gender:", student.gender)
            result += 1
    #time.sleep(5)
    #休眠5s
print("查询结束. 共找到{}个结果".format(result))