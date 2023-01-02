def basen(num,base):
    outp=''
    letters={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
    while True:
        if num==0:
            break
        if num%base>9:
            outp=letters[num%base]+outp
        else:
            outp=str(num%base)+outp
        num=num//base
    return outp
    
n=int(input())#length of sequence
b=int(input())#base of number
s=int(input(),b)#starting number
lst=[]
diction={}
for i in range(n):
    lst.append(basen(s+i,b))
for i in lst:
    for j in i:
        diction.setdefault(j,0)
        diction[j]+=1
maximum=[None,0]

for i in diction:
    if diction[i]>=maximum[1]:
        maximum=[i,diction[i]]
print(maximum[1])
    
