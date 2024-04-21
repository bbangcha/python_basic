import operator

age = int(input('나이 입력 : '))
# vaccin = (age < 20) or (age >= 65)
vaccin = operator.or_(operator.lt(age, 20), operator.ge(age, 65))
print('age : {}, vaccin : {}'.format(age, vaccin))