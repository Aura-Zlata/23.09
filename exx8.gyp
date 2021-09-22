ora=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
grade=[9,9,9,9,10,10,10,10,15,15,15,15,8,8,8,8,12,12,12,12,16,16,16,16]
print('Temperatura medie este=',sum(grade)/24)
max=grade.index(max(grade))
print('Temperatura maxima este=',grade[max])
min=grade.index(min(grade))
print('Temperatura minima este=',grade[min])

print('Ora cu temp maxima=',ora[max])
print('Ora cu temp minima=',ora[min])