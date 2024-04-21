userInputAlphabet = input('알파벳 입력 : ')
print('{} : {}'.format(userInputAlphabet, ord(userInputAlphabet)))

userInputASCII = int(input('아스키 코드 입력 : '))
print('{} : {}'.format(userInputASCII, chr(userInputASCII)))

systemID = 'administrator@gmail.com'
sysoutPW = '!@#$%qwertyQWERTY'

userInputID = input('아이디 입력 : ')
userInputPW = input('비밀번호 입력 : ')

print('아이디 비교 결과 : {}'.format(systemID == userInputID))
print('비밀번호 비교 결과 : {}'.format(sysoutPW == userInputPW))