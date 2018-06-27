def bmi_app():
    height = input('How tall are you? ')
    weight = input('How much do you weight? ')
    bmi = int(weight)/(int(height)/100)**2
    print('You BMI is {}'.format(round(bmi,2)))
                   
    if bmi < 18.5:
        print('You\'d better eat more!')
    elif bmi >= 18.5 and bmi <=24:
        print('Good job!')
    else:
        print('You\'d better do some exercises')

bmi_app()
