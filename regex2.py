import re
txt="life is short enjoy accept yourself.lead a good life"
sd="life"
reg=re.findall(sd,txt)
print(reg,type(reg))
