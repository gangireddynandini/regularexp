import re

reg=re.finditer("\s","NaNaaNNNaddddduuuu")
print(reg,type(reg))
cnt=0
for a in reg:
    print("start index is{} \tend index is {}\t  the value is {}".format(a.start(),a.end(),a.group()))
    cnt=cnt+1
print("count of special symbols",cnt)


