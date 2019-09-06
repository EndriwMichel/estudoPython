# Datetime
import datetime

agora = datetime.datetime.now()

print(agora)

print(agora.hour)
print(agora.minute)
print(agora.second)
print(agora.microsecond)

print('')
print('ctime', agora.ctime())
print('ctime', agora.year)
print('ctime', agora.month)
print('ctime', agora.day)

# Criando sua propria data
date = datetime.date(2015, 4, 28)
print('')
print(date)

# Calculos com datas
print('')
print(date.replace(year=2016))

# Diferença entre datas
print(agora.date() - date)