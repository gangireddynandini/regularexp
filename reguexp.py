import re
des=re.finditer("lilly","lilly is a good girl and lilly has a beautiful doll")
for d in des:
    print(d)