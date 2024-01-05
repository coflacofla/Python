

def errLineFinder(filename):
    f=open(filename,'r',encoding="UTF8")
    f_result=open('result.txt','w')

    data=f.read().split('\n')
    
    people=[]
    name=[]
    age=[]
    home=[]

    error1_message=[]
    error2_message=[]
    error3_message=[]


    global str1, str2, str3

    region=['서울','경기','충청','경상','전라','강원','제주','대전','광주','부산','울산','인천','대구']
    
    for k in data:
        people=k.split('/')
        name.append(people[0])
        age.append(people[1])
        home.append(people[2])

    i=0
    
    while(i<len(data)):
        #name error checking
        
        if 1<len(name[i])<6:
            tmp=0
        else:
            str1="Error1(Line "+str(i+1)+"): 이름 길이가 2~5자리가 아닙니다.\n"
            #error1_message.append(str1)
            f_result.write(str1)

        #age error checking
        if 0<int(age[i])<=150:
            tmp=0

        else:
            str2="Error2(Line "+str(i+1)+"): 유효한 나이 범주가 아닙니다(1~150살).\n"
            #error2_message.append(str2)
            f_result.write(str2)
        
        #home error checking
        for j in region:
            if j==home[i]:
                break
            else:
                if j=='대구':
                    str3="Error3(Line "+str(i+1)+"): 유효한 지역이 아닙니다.\n"
                    #error3_message.append(str3)
                    f_result.write(str3)
        i=i+1

        
        
    

    f.close()
    f_result.close()
    


        
