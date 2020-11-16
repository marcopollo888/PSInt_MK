import math
import file_manager as fm

a_list = [1, 4, 5, 6]
b_list = [3, 7, 2, 9, 8]

def listy(a_list, b_list):
    c_list = []
    for i in range(0, len(a_list)-1, 2):
            c_list.append(a_list[i])
    for i in range(1, len(b_list), 2):
            c_list.append(b_list[i])
    return c_list

c_list = listy(a_list, b_list)
print(c_list)

def znaki(data_text):
    big_l = []
    small_l = []
    for i in data_text:
        if i.isupper():
            big_l.append(i)
        else:
            small_l.append(i)
    information = {'length':len(data_text),'letters':list(data_text),'big_letters':big_l,'small_letters':small_l}
    return information
print(znaki("HIDBYBkdwadjiWDDADHwiiqmiqj"))

def tekst(text, letter):
    return text.replace(letter,"")
print(tekst("Test", "t"))

def temperatura(temperature_C, temperature_type):
    if temperature_type == 'K':
        print("Kelvin:{0}".format(temperature_C + 273.15))
    elif temperature_type == 'F':
        print("Fahrenheit:{0}".format(temperature_C * 1.8 + 32))
    elif temperature_type == 'R':
        print("Rankine:{0}".format((temperature_C + 273.15) * 1.8))
    else:
        print("Nieprawidłowe dane wejściowe")
temperatura(100, 'R')

class Calculator:
    def __init__(self, f, s):
        self.x = f
        self.y = s
    def add(self):
        return self.x + self.y
    def difference(self):
        return self.x - self.y
    def multiply(self):
        return self.x * self.y
    def divide(self):
        return self.x / self.y
Calculator1 = Calculator(3, 3)
print(Calculator1.add())
print(Calculator1.difference())
print(Calculator1.multiply())
print(Calculator1.divide())

class ScienceCalculator(Calculator):
    def __init__(self, f, s):
        self.x = f
        self.y = s
    def exponentiation(self):
        return pow(self.x, self.y)
Calculator2 = ScienceCalculator(3, 2)
print(Calculator2.exponentiation())

def wspak(text):
    print(text[::-1])
wspak("Jedenaście")

plik=fm.FileManager("plik1.txt")
plik.update_file("update")
plik.read_file()


