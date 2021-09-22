a=[2000, 3500, 7000, 1700, 4000, 5500, 3000]
b=['Luni','Marti','Miercuri','Joi','Vineri','Sambata','Duminica']
print('Venitul saptaminal al intreprinderii este=',sum(a), "€")
print('Media venitului zilnic este=',sum(a)/7, "€")
max=a.index(max(a))
print('Ziua in care s a obtinut cel mei mare venit este=',b[max])
min=a.index(min(a))
print('Ziua cu venitul cel mai mic este=',b[min])