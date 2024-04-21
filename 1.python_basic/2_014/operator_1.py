kor = int(input('국어 점수 : '))
eng = int(input('영어 점수 : '))
mat = int(input('수학 점수 : '))

total = kor + eng + mat
avgScore = total/3

print('국어 점수 : {}'.format(kor))
print('영어 점수 : {}'.format(eng))
print('수학 점수 : {}'.format(mat))
print('합계 {}'.format(total))
print('평균 %.2f' %(avgScore))
print('평균 %.2f' % (total/3))