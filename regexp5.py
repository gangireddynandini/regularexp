import re

reg=re.finditer("[yugs]","life is short enjoy accept yourself.lead a good life")
print(reg,type(reg))

for a in reg:
    print("start index is{} \tend index is {}\t  the value is {}".format(a.start(),a.end(),a.group()))



