cena_ziemniakow = float(input("Podaj ile kosztuje kilo ziemniaków: "))
wynik = cena_ziemniakow * 5
print("Za pięć kilo ziemniaków zapłacisz: ", wynik, "zł.")
#Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków i ile kilo chce kupić.
# Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki.
cena_ziemniakow = float(input("Podaj cenę ziemniaków za kilogram (w zł): "))
ilosc = float(input("Ile kg chciałbyś kupic? "))
naleznosc = cena_ziemniakow * ilosc
print("Za", ilosc, "kg ziemniaków zapłacisz", naleznosc, "zl.")