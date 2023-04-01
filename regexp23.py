import re
m=re.finditer('k*','kkkkvvrkkrrkkk')
for j in m:
    print(j)