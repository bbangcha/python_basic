message = input('메세지 입력 : ')
lenMessage = len(message)
msgPrice = 50

if lenMessage <= 50:
    msgPrice = 50
    print('SMS발송!!')

if lenMessage > 50:
    msgPrice = 100
    print('MMS발송!!')

print('메시지 길이 : {}'.format(lenMessage))
print('메시지 발송 요금 : {}'.format(msgPrice))