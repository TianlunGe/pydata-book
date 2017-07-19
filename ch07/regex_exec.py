import re

text = 'foo   bar\n baz  \tqx'
print(text)
print(re.split('\s+', text))

rex = re.compile('\s+')
print(rex.split(text))
print(rex.findall(text))