import wordcloud
import matplotlib.pyplot as plt

text = ''
with open("C:/Users/mspc/Desktop/KakaoTalk_20221010_1155_03_039_박장훈.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        if '] [' in line:
            text += line.split('] ')[2].replace('ㅋ', '').replace('ㅠ', '').replace('ㅜ', '').replace('사진\n', '').replace(
                '이모티콘\n', '').replace('삭제된 메시지입니다', '')

print(text)

image = wordcloud.WordCloud(font_path='C:/Windows/Fonts/H2MJSM.TTF',width = 1000, height = 700).generate(text)
#wordcloud에서 컨텐츠를 발생시키고 구름형태로 만든다.
#한글깨짐을 해결하기 위해 인자에 font_path항목을 추가하였다
#폰트의 파일명은 속성을 눌러서 확인할 수 있다.



plt.figure(figsize = (40, 30))
#figsize(가로길이,세로길이)
#단위는 inch 입니다.


plt.imshow(image)
#imshow는 원하는 사이즈의 픽셀을 원하는 색으로 채워서 만든 그림입니다.
#쉽게말하면 원하는 크기의 행렬을 만들어서 각 칸을 원하는 색으로 채우는 것입니다.
plt.show() #만들었으면 보여줘!

#카카오톡 대화방으로 워드클라우드 만들기 참고자료
#https://haerong22.tistory.com/70
