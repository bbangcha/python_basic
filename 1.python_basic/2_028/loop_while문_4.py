import random

sum = 0
date = 0
flag = True

while flag:
    patientCount = random.randint(50, 100)
    sum += patientCount
    date += 1
    print('날짜 : {}, \t 오늘 환자수 : {}, \t 누적 환자수 : {}'.format(date, patientCount, sum))

    if sum >= 10000:
        flag = False