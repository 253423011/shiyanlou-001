#!/usr/bin/env python3
import sys
cfg_dict={}
user_dict={}
try:
    a=sys.argv[2]
    b=sys.argv[4]
    c=sys.argv[6]
except:
    print('Error,e.g. ./calculator.py -c XXX -d XXX -o XXX')
    exit()
try:
    with open(a) as cfg_file:
        count=1
        for line in cfg_file:
            if count%2==0:
                count=count+1
                continue
            tmp=line.replace(' ','').split('=')
            cfg_dict[tmp[0]]=float(tmp[-1].strip('\n'))
            count=count+1
except:
    print("config file doesn't exist")
    exit()
try:
    with open(b) as user_file:
        for line in user_file:
            tmp=line.split(',')
            user_dict[tmp[0]]=int(tmp[-1].strip('\n'))
except:
    print('user file does not  exist')
    exit()


sr=cfg_dict['YangLao']+cfg_dict['YiLiao']+cfg_dict['ShiYe']+cfg_dict['GongShang']+cfg_dict['ShengYu']+cfg_dict['GongJiJin']
sl=sorted(user_dict.keys())
with open(c,'a') as gz:
 for sl1 in sl:
    value=user_dict[sl1]
    if value<cfg_dict['JiShuL']:
        sf=cfg_dict['JiShuL']*sr
    elif value>cfg_dict['JiShuH']:
        sf=cfg_dict['JiShuH']*sr
    else:
        sf=value*sr
    tax=value-sf-3500
    if tax>0 and tax<=1500:
        tax1=tax*0.03
    elif tax>1500 and tax<=4500:
        tax1=tax*0.1-105
    elif tax>4500 and tax<=9000:
        tax1=tax*0.2-555
    elif tax>9000 and tax<=35000:
        tax1=tax*0.25-1005
    elif tax>35000 and tax<=55000:
        tax1=tax*0.3-2755
    elif tax>55000 and tax<=80000:
        tax1=tax*0.35-5505
    elif tax>80000:
        tax1=tax*0.45-13505
    else:
        tax1=0
    fs=value-sf-tax1
    
    wtmp=str(sl1)+','+str(value)+','+str('{:.2f},{:.2f},{:.2f}'.format(sf,tax1,fs))+'\n'
    gz.write(wtmp)
 
