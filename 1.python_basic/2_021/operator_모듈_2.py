import random
import operator

randomInt = random.randint(10, 100)

num10 = operator.floordiv(randomInt, 10)
num1 = operator.mod(randomInt, 10)

print('난수 : {}'.format(randomInt))
print('십의 자리 : {} '.format(num10))
print('일의 자리 : {}'.format(num1))

print('십의 자리가 3의 배수인지 여부 : {}'.format(operator.mod(num10, 3)==0))
print('일의 자리가 3의 배수인지 여부 : {}'.format(operator.mod(num1, 3)==0))
