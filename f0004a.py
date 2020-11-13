név = input('Hogy hívják önt? ')
kor = input('És hány éves maga? ') 
kor = int(kor)
év = input('Milyen év van?')
év = int(év)
születési_év = év - kor
print(név, ', ön ', születési_év, '-ban született.', sep='')