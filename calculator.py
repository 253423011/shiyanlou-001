#!/usr/bin/env python3
import sys
StaffDict={}
StaffDict1={}
try:
    for i in range(1,len(sys.argv)):
        tmp=sys.argv[i].split(':')
        key=int(tmp[0])
        value=int(tmp[-1])
        StaffDict[key]=value
except:
    print("Parameter Error")

for key in StaffDict.keys():
    Insurance=StaffDict[key]*0.165
    Tax=StaffDict[key]-Insurance-3500
    if Tax>0 and Tax <=1500:
        Tax1=Tax*0.03
    if Tax>1500 and Tax<=4500:
        Tax1=Tax*0.1-105
    if Tax>4500 and Tax<=9000:
        Tax1=Tax*0.2-555
    if Tax>9000 and Tax<=35000:
        Tax1=Tax*0.25-1005
    if Tax>35000 and Tax<=55000:
        Tax1=Tax*0.3-2755
    if Tax>55000 and Tax<=80000:
        Tax1=Tax*0.35-5505
    if Tax>80000:
        Tax1=Tax*0.45-13505
    if Tax<0:
        Tax1=0
    StaffDict1[key]=StaffDict[key]-Insurance-Tax1

SortedKey=sorted(StaffDict1.keys())
for i in SortedKey:
    print(('{}:{:.2f}').format(i,StaffDict1[i]))

