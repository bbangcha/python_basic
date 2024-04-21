result = 1
num =0

for i in range(1, 11):
    result *= i

    if result >50:
        num = i
        break

print('50을 넘을 때의 숫자 : {}, 그때의 결과값 : {}'.format(num, result))