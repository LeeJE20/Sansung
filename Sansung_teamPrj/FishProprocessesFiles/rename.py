'''
 <requirements>
 1. python 3.6.9
 2. library : os (It is default library, so you do not have to install it.)


 <프로그램 실행 안내>
 1. 현재 폴더 안에 사진들이 들어있는 폴더가 있어야 합니다.
 2. 지금 보고 있는 이 파이썬 파일(rename.py)은 현재 폴더 안에 있어야 합니다.
 3. 자기가 원하는 이름으로 폴더를 만들고 그 안에 이름을 바꿀 사진들을 넣으세요. (사진 말고 다른 파일이나 폴더는 넣지 마세요.)
 4. 폴더 이름과 바뀌는 사진 이름은 같게 됩니다. 바뀔 이름으로 폴더 이름을 정해주세요.
 5. 사진은 999장까지만 넣을 수 있습니다. 더 넣고 싶으면 코드에서 새로운 이름 만드는 부분을 고치세요.
 6. 코드에서 fishCodeList라는 리스트 안에 사진이 들어 있는 폴더 이름들을 넣어 두어야 합니다.
 7. 사진은 무조건 .jpg로 바뀝니다. 오류가 생기면 사진을 바꾸세요.

 예)
 현재 폴더 안에 chu라는 폴더를 만들고,
 현재 폴더 안에 rename.py가 있고,
 fishCodeList = ["chu"]이고,
 chu 폴더 안에 물고기1.jpeg와 물고기2.jpg가 있었다면,
 프로그램 실행 후 파일이 이름이 chu001.jpg와 chu002.jpg로 바뀜


 2020.01.21
 이정은
 # 최초 작성
 아래 코드 참조
 https://gist.github.com/developer-sdk/f604e250c6550070bb984b1dd28098fd


 2020.01.27
 이정은
 #requirements 추가
 #프로그램 실행 안내 추가
 #폴더 이름 없을 경우 에러나는 것 수정 -> 어떤 이름을 가진 폴더가 없는지 안내 나옴.
 #같은 이름을 가진 파일이 이미 존재하는 경우 에러나는 것 수정
'''
# -*- coding: utf-8 -*-
from os import rename, listdir

# fishCode = "chu" #참홍어
# fishCode = "mcg" #문치가자미
# fishCode = "mgt" #명태
# fishCode = "roc" #돌돔
# fishCode = "slm" #연어

# fishCodeList = ["chu", "hwb", "mcg", "mgt", "roc", "slm"]

# 10원, 50원, 100원, 500원
fishCodeList = ["ten", "fft", "hdr", "fhd"]


def renameImage(fishCode, makeDefault):
    # 현재 위치의 파일 목록
    # files = listdir('.')
    try:
        files = listdir('./' + fishCode)
    except:
        if makeDefault == True:
            print("다음 이름을 가진 폴더가 없습니다: "+fishCode)
        return
    # 파일명에 번호 추가하기. 1부터 시작.
    count = 1
    for name in files:

        # 안 돌아가는 부분이라 주석 처리
        # 파이썬 실행파일명은 변경하지 않음
        # if sys.argv[0].split("\\")[-1] == name:
        #     continue

        # 파이썬 실행파일명은 변경하지 않음
        if name.endswith("py"):
            continue

        # 파일 확장자가 (jpeg)인 것만 처리
        # if name.endswith("jpeg") or name.endswith("JPEG"):
        #     new_name = fishCode + "{0:03d}.".format(count)+"jpeg"
        #
        # else:
        #     new_name = fishCode + "{0:03d}.".format(count)+"jpg"

        # 나중에 이름 겹칠 것을 대비하여 새 이름 만들어주는 부분.
        if makeDefault == True:
            new_name = "bXdLh3LcZmSASbc6" + "{0:03d}.".format(count) + "jpg"

        if makeDefault == False:
            # 확장자는 jpg만 사용. 새로 이름 만들어주는 부분.
            new_name = fishCode + "{0:03d}.".format(count) + "jpg"

        try:
            rename('./' + fishCode +'/'+ name, './' + fishCode +'/'+new_name)
        except FileExistsError as e:
            # 같은 이름을 가진 파일이 이미 존재하는 경우
            print(e)


        count += 1


print("폴더 안의 사진 파일 이름을 바꾸는 프로그램입니다.")
for fishCode in fishCodeList:
    renameImage(fishCode, True)
    renameImage(fishCode, False)

# renameImage("hwb")