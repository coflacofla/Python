def star():

    

    mode = int(input("원하는 모드를 입력해주세요(1~5): "))

    line = int(input("원하는 줄 수를 입력해주세요:"))

    mylist = []

    for i in range(line):

        if mode == 1:

            print('*'*(i+1))

        elif mode == 2:

            print('*'*(line-i))

        elif mode == 3:

            print(' '*(line-i-1)+'*'*(i+1))

        elif mode == 4:

            print(' '*(line-i-1)+'*'*(2*i+1))

        else:

            if i <= ((line-1)/2):

                mylist.append(' '*(line-i-1)+'*'*(2*i+1))

                print(mylist[i])

            else:

                print(mylist[line-i-1])

        

    print('-------------')

star()

star()

star()

star()

star()
