import operator

passScore1 = 60
passScore2 = 70

korScore = int(input('국어 점수 : '))
engScore = int(input('영어 점수 : '))
matScore = int(input('수학 점수 : '))

scoreAvg = (korScore + engScore + matScore) / 3

print('국어 : pass') if operator.ge(korScore, passScore1) else print('국어 : fail')
print('영어 : pass') if operator.ge(engScore, passScore1) else print('영어 : fail')
print('수학 : pass') if operator.ge(matScore, passScore1) else print('수학 : fail')
print('시험 : pass') if operator.ge(scoreAvg, passScore2) else print('시험 : fail')

print('평균 : %.2f' % scoreAvg)