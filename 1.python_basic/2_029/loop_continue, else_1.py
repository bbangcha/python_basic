# continue

for i in range(100):
    if i % 7 != 0:
        continue
    print('{}는 7의 배수 입니다.'.format(i))

# else

cnt = 0
for i in range(100):
    if i % 7 != 0:
        continue
    print('{}는 7의 배수 입니다.'.format(i))
    cnt += 1
else :
    print('99까지의 배수 중 7의 배수는 {}개 입니다.'.format(cnt))