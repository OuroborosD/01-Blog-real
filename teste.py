import datetime

data = datetime.date.today()
d2 = data.strftime("%d %B, %Y")

print(data)# 2021-09-21
print(d2)# 21 September, 2021


date_time = datetime.datetime.now()
dt_string = date_time.strftime("%d %B, %Y %H:%M:%S")
print(dt_string)# 21 September, 2021 22:33:26


tamanho = 'REGOBT031278ORIM5ETSSSXJX298'

print(len(tamanho))