# zxwtips

A advanced tool for zhixue.com.

## Introduction

几个常用的智学网脚本

## Features

* 获取学生本人任意一次考试成绩以及排名
* 在本年级年级中利用学生姓名查询所在班级、性别、person-id
* 获取指定班级学生名单并输出至output文件夹（.csv格式）

## Update logs

1.0.0a1 - 2023/03/12:
* find_student, get_ranks, get_stulist 3个功能
* pip module - zhixuewang 安装脚本
* ! zhixuewang 模块默认bug未修复

1.0.0b1 - 2023/03/25:
* Python 自动安装脚本
* 教师账号功能get_scores
* get_stulist 支持导出为.csv表格文件
* ! zhixuewang 模块默认bug未修复
* ! get_ranks_leak 签注识别

1.0.0rc1 - 2023/04/15:
* 自动更新脚本

1.0.0rc2 - 2023/05/07:
* 无人值守安装脚本
* √ HOTFIX 修复zhixuewang module的bug，未来将使用branch直接构建
* ! GUI界面
* ! 自动安装程序