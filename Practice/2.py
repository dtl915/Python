# f_in=open("i.txt","r",encoding="utf8")
# f_ot=open("1.txt","w",encoding="utf8")
# lines=f_in.readlines()
# s_lines=[]
# final={}
# ss=[]
# index1=0
# sc_line=0
# findex=0
# index2=0
# for i in lines:
#     if i != "\n":
#         s=i.strip()
#         ss.append(s.split(":"))
# for i in ss:
#     x=i[0]
#     if not x.isdigit():
#         s_lines.append(index2)
#     index2+=1
# for i in range(len(ss)):
#     if i == s_lines[sc_line]:
#         index1=i
#         if sc_line < len(s_lines)-1:
#             sc_line+=1
#     else:
#         final[findex]=str(ss[index1][2]+ " "+ss[index1][0]+" "+ ss[index1][1]+" "+ ss[index1][3]+ " "+ss[i][3]+ " "+ss[i][1]+ " "+ss[i][0]+ " "+ss[i][2])+"\n"
#         findex+=1
# for i in range(findex):
#     f_ot.writelines(final[i])
# print(s_lines)
# print(final)
# f_ot.close()

# # def adjust(string,wid):
# #     ascii=0
# #     uni=0
# #     for a in string:
# #         if a.isascii(): ascii +=1
# #         else: uni +=1
# #     curr_len=2*uni+ascii
# #     if curr_len>=wid: return string
# #     return string+" "*(wid-curr_len)

# colleges={}
# addr={"xijing":"西京",'lushan':'鲁山','pingyang':'平阳','danling':'丹凌','xinyua':'新元'}
# students=[]
# f_in=open("i.txt",encoding="UTF-8")
# data=f_in.readlines()
# f_in.close()
# f_out=open('d:\\out.txt',encoding="GB2312",mode='w')
# curr_college=None
# for line in data:
#     fields=line.strip().split(':')
#     if len(fields) <4: continue
#     if not fields[0].isdigit() or not int(fields[0]) <=100 or not int(fields[0])>=0:
#         if fields[3] in addr.keys():
#             fields[3]=addr[fields[3]]
#         curr_college=adjust(fields[2],6)+adjust(fields[0],30)+adjust(fields[1],16)+adjust(fields[3],8)
#         continue
#     output=curr_college+adjust(fields[3],12)+adjust(fields[1],10)+adjust(fields[0],4)+adjust(fields[2],16)+"\n"
#     print(output)
#     f_out.writelines(output)
# f_out.close()

# import math as m
# pi=m.pi
# def a_cylinder(radius,height):

#     return radius*radius*height * pi
# print(a_cylinder(radius=4,height=6))

'''
# 1. 
# st=input()
# a=dict()
# for i in st:
#     if i in a:
#         a[i]+=1
#     else:
#         a[i]=1
# print(a)
# '''

# sc={'alen':[99,94,86,92], 'cathy':[78,94,93,99],'duke':[65,78,79,69]}
# a=input()
# def ave(dic,key):
#     if not key in dic:
#         return 'no'
#     x=0
#     y=100
#     for i in dic[key]:
#         x+=i
#         if i < y:
#             y=i
#     x=x/4
#     if x>90 and y>80:
#         return 'A+'
#     elif x>90 and y<80:
#         return'A'
#     elif 80<x<90:
#         return 'B'
#     elif 70<x<80:
#         return 'C'
#     elif 60<x<70:
#         return 'D'
#     elif x<60:
#         return 'E'
# print(ave(sc,a))

import csv
try:
    f=open('20210616当日a委托查询.txt','r')
    f1=open('output.csv','w',encoding='utf8')
    fin=[]
    csv_reader = csv.reader(f,delimiter=' ',skipinitialspace=True)
    csv_writer = csv.writer(f1)
    for row in csv_reader:
        fin.append(row)
    for row in range(2,len(fin)-1):
        csv_writer.writerow(fin[row])
    f.close()
    f1.close()
except FileNotFoundError:
    print('no file')
finally:
    print('the end')