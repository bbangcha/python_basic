fNum = int(input('정수 입력 : '))

addSum = 0
for i in range(1, (fNum + 1)):
    addSum += i

addSumFormated = format(addSum, ',')
print('합 결과 : {}'.format(addSumFormated))

oddSum = 0
for i in range(1, (fNum + 1)):
    if i % 2 != 0:
        oddSum += i

oddSumFormated = format(oddSum, ',')
print('홀수 합 결과 : {}'.format(oddSumFormated))

evenSum = 0
for i in range(1, (fNum + 1)):
    if i % 2 == 0:
        evenSum += i

evenSumFormated = format(evenSum, ',')
print('짝수 합 결과 : {}'.format(evenSumFormated))

factorialResult = 1 # "0"으로 두고 팩토리얼의 경우 곱할 시 영원히 "0" 값이므로 "1"로 입력
for i in range(1, (fNum + 1)):
        factorialResult *= i

factorialResultFormated = format(factorialResult, ',')
print('팩토리얼 결과 : {}'.format(factorialResultFormated))