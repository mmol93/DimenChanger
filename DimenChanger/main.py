import getpass

# 현재 컴퓨터의 유저명 들고오기
userName = getpass.getuser()

filePath = "C:/Users/" + userName + "/OneDrive/dimen.txt"

f = open(filePath, 'r')

# 첫 번째 라인부터 읽기 시작
line = f.readline()

# 모드 선택(xxhdpi가 1 = 기준)
ldpi = 4
mdpi = 3
hdpi = 1.5
xhdpi = 1.5
xxxhdpi = 0.75

changedLine = ""

while line:
    # 한 줄 텍스트에서 dp를 찾는다
    text = line

    # index는 0부터 카운팅한다
    # index1에는 dp, sp 숫자의 직전 인덱스 넘버가 들어있다
    # index2에는 dp, sp의 인덱스 넘버가 들어가 있다
    index1 = text.find(">")
    index2 = text.find("</")
    if index1 != -1 and index2 != -1:
        # dp, sp를 없애고 숫자 부분만 남긴다
        dimension = text[index1 + 1:index2 - 2]

        # 숫자 시작 직전까지의 텍스트 들어있음
        text1 = text[0:index1 + 1]

        # 마지막에서 숫자 직전까지 텍스트 들어있음(예: ~~dp</dimen>)
        text2 = text[-11:]

        # 해상도에 맞게 숫자 부분만 변경
        changedDimension = round(int(dimension) / hdpi)

        # 텍스트 조합을 하여 환성된 문장을 생성
        changedLine = text1 + str(changedDimension) + text2

        # 에러가 난 부분을 제외하고 복사하여 원하는 곳에 해상도 xml 파일에 붙여넣으면된다
        print(changedLine)
    line = f.readline()

f.close()