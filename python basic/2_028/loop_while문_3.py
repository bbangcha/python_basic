currentThickness = 30
rotationCount = 0
removeThickness = 0.15

while currentThickness >=20:
    rotationCount += 1
    currentThickness -= removeThickness

safeRotationCount = rotationCount - 1
print('운행 가능 횟수 : {}'.format(safeRotationCount))