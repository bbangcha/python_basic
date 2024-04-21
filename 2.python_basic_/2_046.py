korScore = int(input('국어 점수 : '))
engScore = int(input('영어 점수 : '))
matScore = int(input('수학 점수 : '))

totalScore = korScore + engScore + matScore
avgScore = (korScore + engScore + matScore) / 3
print('총점 : %.f' % totalScore)
print('평균 : %.2f' % avgScore)

maxScore = korScore
maxSubject = '국어'
if  engScore > maxScore:
    maxScore = engScore
    maxSubject = '영어'

if  matScore > maxScore:
    maxScore = matScore
    maxSubject = '수학'

minScore = korScore
minSubject = '국어'
if engScore < minScore:
    minScore = engScore
    minSubject = '영어'

if matScore < minScore:
    minScore = matScore
    minSubject = '수학'

difScore = maxScore - minScore

print('-' * 25)
print('최고 점수 과목(점수) : {}({})'.format(maxScore, maxSubject))
print('최저 점수 과목(점수) : {}({})'.format(minScore, minSubject))
print('최고, 최저 점수 차이 : {}'.format(difScore))
print('-' * 25)
