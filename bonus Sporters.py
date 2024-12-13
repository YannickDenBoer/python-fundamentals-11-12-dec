voetbal_spelers = {"Eva", "Thom", "Richard", "Peter"}
volleybal_spelers = {"Jantje", "Sara", "Peter", "Sam"}
basketbal_spelers = {"Eva", "Richard", "Jessica", "Sam", "Thomas"}
[voetbal_spelers, volleybal_spelers, basketbal_spelers]

alle_spelers = voetbal_spelers | volleybal_spelers | basketbal_spelers
print(alle_spelers)

meer_dan_een_sport = (voetbal_spelers & volleybal_spelers) | (volleybal_spelers & basketbal_spelers) | (voetbal_spelers & basketbal_spelers)
print(meer_dan_een_sport)

alleen_basketbal = basketbal_spelers - (voetbal_spelers | volleybal_spelers)
print(alleen_basketbal)