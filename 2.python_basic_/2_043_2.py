midtermExamScore = input('중간고사 점수 : ')
finalExamScore = input('기말고사 점수 : ')

if midtermExamScore.isdigit() and finalExamScore.isdigit():
    midtermExamScore = int(midtermExamScore)
    finalExamScore = int(finalExamScore)

    totalScore = midtermExamScore + finalExamScore
    avgScore = totalScore / 2

    print('총점 : {}, 평균 : {}'.format(totalScore, avgScore))

else:
    print('잘못 입력하였습니다')
