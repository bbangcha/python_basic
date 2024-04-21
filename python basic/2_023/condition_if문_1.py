korScore = int(input('국어 점수 : '))
engScore = int(input('영어 점수 : '))
matScore = int(input('수학 점수 : '))

scoreAvg = (korScore + engScore + matScore) / 3
print('평균 : {}'.format(scoreAvg))

if scoreAvg >= 90:
    print('참 잘했어요~')

