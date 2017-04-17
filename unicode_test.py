import re

s = u'\u2019 sddfsfsdfsfsd'
s = s.encode('ascii', 'ignore')
match = re.findall(r'u2019', s)
print match