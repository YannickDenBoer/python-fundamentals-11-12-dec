voetbal_spelers = {"Eva", "Thom", "Richard", "Peter"}
volleybal_spelers = {"Jantje", "Sara", "Peter", "Sam"}
basketbal_spelers = {"Eva", "Richard", "Jessica", "Sam", "Thomas"}
[voetbal_spelers, volleybal_spelers, basketbal_spelers]

x = voetbal_spelers
y = volleybal_spelers
z = basketbal_spelers

alle_spelers = x.union(y).union(z)
meer_dan_een_sport = x.intersection(y).union(y.intersection(z)).union(x.intersection(z))
alleen_basketbal = z.difference(x.union(y))

print(alle_spelers)
print(meer_dan_een_sport)
print(alleen_basketbal)