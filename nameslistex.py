import re
gd="Rossum got 22 marks , Dennis got 56 marks , Travis got 67 marks and James got 88 marks"
sp="[A-z][a-z]+"
print("by using findall")
nameslist=re.findall(sp,gd)
print("names of student")
for name in nameslist:
    print("\t{}".format(name))
print("by using finditer")
match=re.finditer(sp,gd)
print("names of student")
for name in match:
    print("start index:{} end index:{} name:{}".format(name.start(),name.end(),name.group()))

