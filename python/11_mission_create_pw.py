
url = input('사이트:')

rule1 = url[8:]
rule2 = rule1[0:5]
rule3 = rule2[:3]


str1 = len(rule2)
str2 = url.count('e')



a=rule3
b=str1
c=str2

print(f"{a}{b}{c}!")
