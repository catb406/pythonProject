flag=True
op=['(','[','{']
cl=[')', ']', '}']
test=input()
q=[]
for i in test:
    if i in op:
        q.append(i)
    elif i in cl:
        if q==[]:
            flag=False
            break
        elif op.index(q.pop())!=cl.index(i):
            flag=False
            break
if q != []:
    flag=False
print(flag)