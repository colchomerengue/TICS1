dia = int(input("Que día es"))
mes = int(input("Y el mes"))
anho = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
tem_anho = anho[mes:12]
res = anho[mes - 1] - dia

for i in tem_anho:
    res = res + i

print(res)
