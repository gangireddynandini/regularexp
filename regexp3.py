import re
txt="life is short enjoy accept yourself.lead a good life"
sd="life"
reg=re.finditer(sd,txt)
print(reg,type(reg))
cnt=0
for a in reg:
    print("start index is{} end index is {} and yhe value is{}".format(a.start(),a.end(),a.group()))
    cnt=cnt+1
print("{} found {} times".format(sd,cnt))

