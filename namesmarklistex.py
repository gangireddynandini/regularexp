import re
gd="Rossum got 22 marks , Dennis got 11 marks , Travis got 558 marks ,Kinney got 78 marks"
sd1="\d{2,3}"
sd2="[A-Z][a-z]+"
marks=re.findall(sd1,gd)
names=re.findall(sd2,gd)
print("_"*30)
print("\tNanes\tMarks")
print("_"*30)
for name,mark in zip(names,marks):
    print("\t{}\t{}".format(name,mark))
print()