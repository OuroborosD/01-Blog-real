import datetime
from  calendar import monthrange  # para ver o primeiro e ultimo dia do mes.

data = datetime.date.today()
d2 = data.strftime("%d %B, %Y")

print(data)# 2021-09-21
print(d2)# 21 September, 2021


date_time = datetime.datetime.now()
dt_string = date_time.strftime("%d %B, %Y %H:%M:%S")
print(dt_string)# 21 September, 2021 22:33:26


tamanho = 'REGOBT031278ORIM5ETSSSXJX298'

print(len(tamanho))

data2 = datetime.date.today()
print(data2)# ve o dia
print(data2.day)# ve o dia
print(data2.month)# ve o mes

#monthrange (ano, mês)
ultimo_dia_mes = monthrange(data2.year, data2.month)
print(ultimo_dia_mes) #retorno tupla:( não sei, ultimo dia do mes) (02,30)
print(ultimo_dia_mes[1])# 30
