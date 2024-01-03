web1 = 'http://naver.com'
web2 = 'http://google.com'
web3 = 'http://daum.com'
web = input("Put the URL : ")

def web2pw(web):
    web = web[web.find('//')+2:web.find('.')] # Extract only domian, like "naver.com" and extract until find "."
    pw = web[:3] + str(len(web)) + str(web.count('e')) + '!' # Concatenate whole things
    return pw

print(web2pw(web1))
print(web2pw(web2))
print(web2pw(web3))
print(web2pw(web))
    
