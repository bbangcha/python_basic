maxlength = 5200
maxWidth = 1985

myCarLength = int(input('전장 길이 : '))
myCarWidth = int(input('전폭 길이 : '))

print('전장 세차 가능 여부 : {}'.format(myCarLength <= maxlength))
print('전폭 세차 가능 여부 : {}'.format(myCarWidth <=maxWidth))