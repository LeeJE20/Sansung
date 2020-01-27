'''
 <requirements>
 1. python 3.6.9
 2. library :
     os (It is default library, so you do not have to install it.)
     PIL 7.0.0 (If you have trouble installing "PIL", you can install "image" or "pillow" instead. Do not change "from PIL import Image" code.)
        # PIL 라이브러리 install 안 되면 참고 (요약: image 또는 pillow를 install하면 PIL도 같이 install 된다)
        # https://kamang-it.tistory.com/entry/PIL-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-%ED%95%98%EA%B8%B0image-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C-%ED%95%98%EA%B8%B0
        # image나 pillow 설치했다고 from PIL import Image 부분 코드 바꾸지 마세요.


 <프로그램 실행 안내>
 1. 현재 폴더 안에 사진들이 들어있는 폴더가 있어야 합니다.
 2. 지금 보고 있는 이 파이썬 파일(resize.py)은 현재 폴더 안에 있어야 합니다.
 3. 사진들이 들어있는 폴더 이름이 aaa라면, 코드에서 fishCodeList라는 리스트에 "aaa"를 추가해 주세요.
 4. fishCodeList 리스트에 여러 폴더 이름을 넣으면, 그 폴더들 안의 모든 사진들의 size가 바뀝니다.
 5. 사진 폴더 안에 사진이 아닌 다른 파일이나 폴더를 넣지 마세요.
 6. 코드에서 afterWidthSize, afterHeightSize 변수에 원하는 가로, 세로 사이즈를 넣으세요.
 7. 프로그램 실행 후 사이즈가 잘 바뀌었는지 확인하려면 사진 파일 오른쪽 클릭->속성->자세히->스크롤 내려서 "사진 크기"를 확인하세요.

 예)
 현재 폴더 안에 chu라는 폴더를 만들고,
 현재 폴더 안에 resize.py가 있고,
 fishCodeList = ["chu"]이고,
 afterWidthSize = 100이고,
 afterHeightSize = 200이고,
 chu 폴더 안에 물고기1.jpeg와 물고기2.jpg가 있었다면,
 프로그램 실행 후 물고기1.jpeg와 물고기2.jpg의 크기가 가로 100픽셀, 세로 200픽셀로 바뀜.



# 2020.01.21
# 이정은
# 아래 코드 참조
# https://mjdeeplearning.tistory.com/64

 2020.01.27
 이정은
 #requirements 추가
 #프로그램 실행 안내 추가
 #폴더 이름 없을 경우 에러나는 것 수정 -> 어떤 이름을 가진 폴더가 없는지 안내 나옴.
 #사이즈 변경 불가한 경우 에러나는 것 수정 -> 어떤 파일이 변경 불가한지 안내 나옴.
'''

from PIL import Image
from os import listdir
from PIL import UnidentifiedImageError

# fishCode = "chu" #참홍어
# fishCode = "mcg" #문치가자미
# fishCode = "mgt" #명태
# fishCode = "roc" #돌돔
# fishCode = "slm" #연어

# fishCodeList = ["chu", "hwb", "mcg", "mgt", "roc", "slm"]

# 10원, 50원, 100원, 500원
fishCodeList = ["ten", "fft", "hdr", "fhd"]

# 이미지 가로 사이즈
afterWidthSize = 600
# 이미지 세로 사이즈
afterHeightSize = 600

def resizeImage(fishCode):
    # 현재 위치의 파일 목록
    # files = listdir('.')
    try:
        files = listdir('./' + fishCode)
    except:
        print("다음 이름을 가진 폴더가 없습니다: " + fishCode)
        return

    for name in files:
        # 파이썬 실행파일명은 변경하지 않음
        if name.endswith("py"):
            continue
        try:
            path = './' + fishCode + '/' + name
            image = Image.open(path)

            resize_image = image.resize((afterWidthSize, afterHeightSize))

            resize_image.save(path)
        except UnidentifiedImageError as e:
            # print(e)
            print("다음 파일은 이미지 파일이 아닙니다: "+path)

print("폴더 안의 사진 파일 크기를 바꾸는 프로그램입니다.")
for fishCode in fishCodeList:
    resizeImage(fishCode)

# resizeImage("hwb")