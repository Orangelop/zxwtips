#get_stulist 获取指定班级学生名单并输出至output文件夹（.csv格式）
#pip3 install zhixuewang
from zhixuewang import *
import csv, time, os, sys

#use account and passwd
user = input("输入用户名: ")
passwd = input("输入密码: ")

#or use login_student_id()
get = login(user,passwd)

print("//////////打印班级列表//////////")
class_list = get.get_clazzs()
for aclass in class_list:
    print("class-id:",aclass.id,"class-name:",aclass.name)
print("//////////班级列表结束//////////")

print("//////////打印学生列表//////////")
student_list = get.get_classmates(input("Input class-id: "))
output = []
for student in student_list:
    print("person-id:",student.id,"name:",student.name,"class:",student.clazz.name,"gender:",student.gender)
    output.append((student.name, student.gender, student.id, student.clazz.name))
print("//////////学生列表结束//////////")

# Export
exp_choice = int(input('是否导出为.csv表格文件? 是 - 输入1: '))
if exp_choice == 1:
    # Configure output style
    dir_name, script_name = os.path.split(os.path.abspath(sys.argv[0])) 
    file_name = dir_name + '\output\output_' + time.strftime('%Y%m%d_%H_%M_%S') + '.csv'
    header_1 = ['Output of zxwtips, date: ' + time.strftime('%Y%m%d_%H_%M_%S')] 
    header_2 = ['姓名', '性别', 'stu-id', '班级']

    # ANSI encoding
    with open(file_name, 'w', encoding='ANSI', newline='') as csv_output:
        writer = csv.writer(csv_output)
        writer.writerow(header_1)
        writer.writerow(header_2)
        for person in output:
            writer.writerow(person)
    print('成功导出至：{}'.format(file_name))
