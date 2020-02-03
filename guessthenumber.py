#guess the nummber game\
import random
n = 0
print('Enter the name of the participant')
name = input()
print('Hello ' + name + '\n')


def inputnumber():
    print('Enter the number')
    n = input()
    guess(n)

def guess(n):
    try:
        a = random.randint(1, 5)
        if int(n)==a:
                print('Congratulations! ' + name + '! You guessed the number')
        else:
                print('Nope, wrong guess, wanna try again?')
                inputnumber()
    except:
        print('Enter a numeric number please')
    
inputnumber()

