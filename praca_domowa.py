# Narysuj piramidę Mario - jako input - wysokość piramidy
# np. piramida wysokości 3 ma wyglądać:
piramida=int(input("podaj wysokość piramidy: "))

for i in range(piramida):
    print(' '*(piramida-i-1) + '*'*(2*i+1))
#
#   #
#  ###
# #####
#
#
# # program, ktory wypisze liczby od 0 do 20 poza liczbami podzielnymi przez 4
# # continue
for i in range(20):
    if i%4==0:
        continue
    print(i)


# program obliczajacy liczbe liter i cyfr w stringu
licznik_string=0
licznik_int=0
string = (input("podaj string"))

for i in string:
    if i in("0","1","2","3","4","5","6","7","8","9"):
        licznik_int=licznik_int+1
    else:
        licznik_string=licznik_string+1

print("liczba int: ",licznik_int)
print("liczbastring: ",licznik_string)


# program wypisujący tabliczkę mnozenia (1 do 10) dla podanej przez użytkownika liczby
# np: 3 x 1 = 3
#     3 x 2 = 6
#     3 x 3 = 9 itp

liczba=int(input("podaj liczbę:"))
for i in range(1,11):
   print(i,'*',liczba,'=',i*liczba)
# oblicz wiek psa z ludzkich lat w psich latach
# przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku
# kolejne lata, psi rok to 4 ludzkie lata
# np. 15 ludzkich lat to 73 psie lata
pies= int(input("ile pies ma lat: "))
if pies<=2:
    print("pies ma: ",pies*10,5)
else:
    print("pies ma: ",21+(pies-2)*4,"lata")
