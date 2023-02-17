string1, string2= input().split(' ')



minlength=min((len(string1),len(string2)))






while True:
    change=False
    minlength=min((len(string1),len(string2)))
    string1=[s for s in string1]
    string2=[s for s in string2]

    for i in range(minlength):
        if string1[i]==string2[i]:
            string1[i]=''
            string2[i]=''
            minlength-=1
            change=True
    
    for i in range(minlength):
        if len(string2)-1>i:
            if string1[i]==string2[i+1]:
                string2[i]=''

                change=True
                break
                
        if len(string1)-1>i:
            if string2[i]==string1[i+1]:
                string1[i]=''

                change=True
                break
    string1=''.join(string1)
    string2=''.join(string2)

    if not change:
        break

    
minlength=min((len(string1),len(string2)))
ASF=0
for i in range(minlength):
    ASF+= ord(string1[i])-ord(string2[i])
ASF+=len(string1)+len(string2)-2*minlength
print(ASF)

