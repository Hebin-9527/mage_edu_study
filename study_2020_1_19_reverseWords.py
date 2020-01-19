#！/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020/1/19 16:32
# @Author : David_9527
# @File : study_2020_1_19_reverseWords.py
#输入一个列表，将其反转输出
def reverseWords(input):
    inputWords = input.split(" ")
    inputWords = inputWords[-1::-1]
    outputWords = ' '.join(inputWords)

    return outputWords