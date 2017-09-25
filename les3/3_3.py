leeftijd=eval(input('Enter your age: '))
paspoort=(input('Do you have a passport: '))
if leeftijd >= 18 and paspoort == 'ja':
    print('Gefeliciteerd, ' 'je mag stemmen!')
else:
    print('Je mag niet stemmen')