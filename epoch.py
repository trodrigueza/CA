import time
import datetime

d = open('epochdata.txt')
data = []

for i in d:
    n = [str(x) for x in i.replace('/n', '').replace(',','').replace(' ','/').replace('Jan','01').replace('Dec', '12').replace('Nov', '11').replace('Oct', '10').replace('Sep', '09').replace('Aug', '08').replace('Jul', '07').replace('Jun', '06').replace('May', '05').replace('Apr', '04').replace('Mar', '03').replace('Feb', '02').split()]
    data.append(n)

datao = []
for i in data:
    ts = time.mktime(datetime.datetime.strptime(i[0], "%m/%d/%Y").timetuple())
    datao.append(ts)

for i in datao:
    with open('epoch.txt', 'a') as f:
        f.write(str(i).replace('.0', '\n'))
