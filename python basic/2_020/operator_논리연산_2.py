passScore1 = 60 # 조건 먼저 찾기
passScore2 = 70 # 조건 먼저 찾기


korScore = int(input('국어 점수 : '))               # 국어 점수 입력
engScore = int(input('영어 점수 : '))               # 영어 점수 입력
matScore = int(input('수학 점수 : '))               # 수학 점수 입력
scoreAvg = (korScore + engScore + matScore) / 3   # 각 점수 평균 입력
scoreAvgResult = scoreAvg >= passScore2           # 평균 결과의 합격 조건

korResult = korScore >= passScore1            # 국어 점수의 합격 조건
engResult = engScore >= passScore1            # 영어 점수의 합격 조건
matResult = matScore >= passScore1            # 수학 점수의 합격 조건

subjectResult = korResult and engResult and matResult      # 국어, 영어, 수학 점수의 합격 조건

print('평균 : {}, 결과 : {}'.format(scoreAvg, scoreAvgResult))
print('국어 : {}, 결과 : {}'.format(korScore, korResult))
print('영어 : {}, 결과 : {}'.format(engScore, engResult))
print('수학 : {}, 결과 : {}'.format(matScore, matResult))
print('과락결과 : {}'.format(subjectResult))
print('최종결과 : {}'.format(scoreAvgResult and subjectResult))
