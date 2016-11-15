'''코바야카와 사에와 함께하는 즐거운 숫자 맞추기 게임 v1.1
'''
import random

guessesTaken = 0

print('안녕하시와요? 프로듀서항의 성함은 무엇이온지요?')
myName = input()
myNamep = myName + 'P'
number = random.randint(1,20)
print('그러면, ' + myNamep + '항, 저는 하나부터 스물까지의 숫자를 하나 생각하고 있사와요.')

while guessesTaken < 6:
    print('맞추어 보시겠사온지요?')
    guess = input()
    while guess not in {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'}:
        print('장난은 싫사와요. 하나와 스물 사이의 아라비아 숫자로 대답해주시어요.')
        guess = input()
    else:

        guess = int(guess)

        guessesTaken = guessesTaken + 1

    if guess < number:
        print(('정답보다 낮사와요', '좀 더 높여보시어요', '땡~이어요. 더 큰 숫자를 불러보시어요',
                '더 큰 숫자랍니다~', '그보다 크답니다~')[random.randint(0,4)])

    if guess > number:
        print(('정답보다 높사와요', '좀 더 낮춰보시어요', '땡~이어요. 더 작은 숫자를 불러보시어요',
               '더 작은 숫자랍니다~', '그보다 작답니다~')[random.randint(0, 4)])

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('정답이와요, ' + myNamep + '항! '+ myNamep + '항은 ' + guessesTaken + '번만에 맞추셨사와요!')

if guess != number:
    number = str(number)
    print(myNamep + '항이 졌사와요. 제가 생각한 숫자는 ' + number + '였사와요.')
