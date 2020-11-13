név = input('Hogy hívják önt? ')
kor = input('És hány éves maga? ') 
év = input('Melyik évben járunk? ')
év = int(év)
kor = int(kor)
születési_év = év - kor
érettségi = 18
érettségi =int(érettségi)
print(név,születési_év, 'született', érettségi - kor, 'múlva fog érettségizni')