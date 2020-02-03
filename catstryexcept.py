def cats(num):
 try:
     if (int(num))>10:
         print('Whoa that is ' + str(int(num)-10) + ' cats more than me \n')
     else:
        print('Man you do not have a lot of cats, I am sorry!')
 except:
     print('Yo! Man, enter a number please')


print('How many cats you got homeboy? \n')
num = input()
cats(num)
           
