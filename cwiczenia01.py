lipsum = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
imie = "Marek"
nazwisko = "Karłowicz"
litera_1 = imie[2]
litera_2 = nazwisko[3]
liczba_liter_1 = lipsum.count(litera_1)
liczba_liter_2 = lipsum.count(litera_2)

print("W tekście jest %i liter %s oraz %i liter %s" %(liczba_liter_1,litera_1,liczba_liter_2,litera_2))

cztery = "Ad augusta per angusta"

print(dir(cztery))
help(cztery.center)

print(imie[::-1])
print(nazwisko[::-1])

lista1 = [1,2,3,4,5,6,7,8,9,10]
lista_1 = lista1[0:5]
lista2 = lista1[5:10]
lista1 = lista_1
print(lista1, lista2)
pierwotna = lista1+lista2
print(pierwotna)
pierwotna.insert(0,0)
pierwotna.sort()
kopia_pierwotna = pierwotna
kopia_pierwotna.reverse()
print(kopia_pierwotna)

studenci = (
    (123321,"Antoni Kacperski"),
    (363531,"Barbara Adamczyk"),
    (773552,"Andrzej Tumulec"),
    (888331,"Tomasz Jonasz")
)

studenci_s1 = dict(studenci)
print(studenci_s1)

#9 ; 10 ; 13

a11 = range(1,10,1)
a12 = range(100, 20, -5)
for a11 in range(1,11,1):
    print(a11)

for a12 in range(100, 20, -5):
    print(a12)