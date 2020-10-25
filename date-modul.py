from datetime import datetime
from datetime import timedelta
simdi = datetime.today()
# result = datetime.strftime(simdi,"%d %m %Y %a")
# print(result)
# t = "21 November 2001"
# gun, ay, yil = t.split()
# print(gun)
# print(ay)
# print(yil)
# kacyil = int(datetime.strftime(simdi,"%Y")) - int(yil)
# print(kacyil)
# result = datetime.strptime(t,"%d %B %Y")
# print(result.year)
# birthday = datetime(2001,11,21)
# sonuc = datetime.timestamp(birthday)
# kacgun = simdi - birthday
# print(kacgun)
# print(kacgun.seconds)
# print(kacgun)
# result = simdi + timedelta(milliseconds=150000000)


result = simdi - timedelta(days=6823)




print(simdi)
print(result)