url = input("")

url = url.split('//')[1].split('.')[0]


cnt = 0
for i in range(len(url)):
    if (url[i] == 'e'):
        cnt += 1

output = url[:3] + str(len(url)) + str(cnt) + '!'
print(output)
