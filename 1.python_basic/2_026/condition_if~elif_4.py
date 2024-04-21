selctNum = int(input('출퇴근 대상자 인가? 1. YES \t 2. No'))

if selctNum == 1:
    print('교통수단은? ')
    trans = int(input('1. 도보, 자전거 \t 2. 버스, 지하철 \t 3. 자가용'))
    if trans == 1:
        print('세금 감면 5%')
    elif trans == 2:
        print('세금 감면 3%')
    elif trans == 3:
        print('세금 감면 1%')
elif selctNum == 2:
    print('세금 변동 없습니다')
else:
    print('절못 입력하셨습니다')
