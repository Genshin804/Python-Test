import random

colors = ['red','blue','green','purple','yellow']
luckyColor = random.choice(colors)

for i in range(3):
    print('There ar {} colors'.format(colors))
    guess = input('Guess your lucky color: ')
    if guess != luckyColor:        
        try:
            colors.remove(guess)
        except Exception:
            print('Sorry!No color you entered')
        else:
            print('Semmes like {} is not your lucky color:('.format(guess))
    else:
        break

if guess == luckyColor:
    print('Great! {} is your lucky color!'.format(luckyColor))
else:
    print('Actually,{} is your lucky color!'.format(luckyColor))
