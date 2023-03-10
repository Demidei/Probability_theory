def Factorial(N):
    if N==0:
        return 1
    else:
        return N*Factorial(N-1)

def Socetaniya(N,K):
    return Factorial(N)/(Factorial(K)*Factorial(N-K))

def SocetaniyaSPovtorom(N,K):
    return  Socetaniya(N+K-1,K)

def Razmescheniya(N,K):
    return Factorial(N)/(Factorial(N-K))

def RazmescheniyaSPovtorom(N,K):
    C=1
    i=1
    while i <= K:
        C =C*N
        i += 1
    return C

def Perestanovki(N):
    return Factorial(N)

def PerestanovkiSPovtorom(N,K):
    C=1
    i=1

    while i <= K:
        C =C*Factorial(i)
        i += 1
    
    return Factorial(N)/C

#Из колоды в 52 карты извлекаются случайным образом 4 карты. a) Найти вероятность того, что все карты – крести.

# Я рассуждал так, что нам нужно найти отношение количества сочетаний четырех карт из тринадцати треф к количеству сочетаний четырех карт из всех

print(Socetaniya(13,4)/Socetaniya(52,4))

#Из колоды в 52 карты извлекаются случайным образом 4 карты. б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

# Я начал с довольно громоздкого поиска веротяности выбрать все возможные варинты тузов

print((Socetaniya(4,4)+Socetaniya(4,3)*Socetaniya(48,1)+Socetaniya(4,2)*Socetaniya(48,2)+Socetaniya(4,1)*Socetaniya(48,3))/Socetaniya(52,4))

# Но после вашей подсказки смог найти гораздо более удобный способ поиска обратной вероятности

print(1-(Socetaniya(48,4)/Socetaniya(52,4)))

# На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9. Код содержит три цифры, которые нужно нажать одновременно. Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?

# Я исходил из того, что у нас ровно один код, который нужно угадать. А всего вариантов - сочетания трех из десяти. Сочетания т.к. мы нажимаем кнопки одновременно, таким образом их порядок не важен и каждая цифра встречается не более одного раза

print(1/Socetaniya(10,3))

#В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали. Какова вероятность того, что все извлеченные детали окрашены?

# Эту задачу я решил решить (ох) так, как решал их в школе. Пусть детали выбираются последовательно. Тогда для первой попытки вероятность вынуть искомую деталь 9/15, далее для второй 8/14 и для третьей 7/13. Осталось умножить вероятности.
# Возможно я ошибаюсь в чем-то, но ответ вроде сходится с вычислением при решении через поиск сочетаний

print((9/15)*(8/14)*(7/13))

#В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

# Я решил эту задачу по аналогии с третьей задачей

print(1/Socetaniya(100,2))
