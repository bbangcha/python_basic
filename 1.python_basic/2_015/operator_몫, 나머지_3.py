allStuCnt = int(input('전체 학생 수 : '))
stuCntOfGroup = int(input('한 모둠 학생 수 : '))
groupCnt = allStuCnt // stuCntOfGroup
overStuCnt = allStuCnt % stuCntOfGroup
reslut = divmod(allStuCnt, stuCntOfGroup)

print('전체 학생 수 : {}'.format(allStuCnt))
print('한 모둠 학생 수 : {}'.format(stuCntOfGroup))
print('모둠 수 : {}'.format(groupCnt))
print('남은 학생수 : {}'.format(overStuCnt))
print('모둠 수 : {}'.format(reslut[0]))
print('남은 학생 수 : {}'.format(reslut[1]))

