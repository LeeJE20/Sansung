# 2020.01.21
# 이정은
# Raw 제이슨 파일 전처리하는 코드.
# 같은 폴더에 Raw 파일들 둬 주세요.

def wirteFile(filename, num, annotation):
    # 첫 번째 annotation의 경우
    if num == 0:
        with open(filename, 'w') as f:
            f.write("[\n\t"+annotation)
    else: # annotation이 있는 상태라면 내용 append하기
        with open(filename, 'a') as f:
            f.write(",\n\t"+annotation)


def main():
    fishCodeList = ["chu", "hwb", "mcg", "mgt", "roc", "slm"]
    for fishCode in fishCodeList:
        preprocessJson(fishCode)


def preprocessJson(fishCode):
    # 원본 파일 이름
    # filename = "test.json"
    filename = fishCode+"Raw.json"
    resultFileName = fishCode + ".json"
    print(resultFileName)

    # 파일 열고 json형태로 읽기
    json = openFile(filename)
    length = len(json)
    print(length)

    for num in range(0, length):
        annotation = makeAnnotation(json, num)
        wirteFile(resultFileName, num, annotation)
        
    with open(resultFileName, 'a') as f:
        f.write("\n]")


def openFile(filename):
    text=""
    with open(filename, 'r') as f:
        while True:
            line = f.readline()
            text=text+line
            if not line: break
        # print(text)

        # text= '[{"ID":"ck5n7bcfn70gl0952omu7827x","DataRow ID":"ck5n7adigecxo0doqabayd8jv","Labeled Data":"https://storage.labelbox.com/ck5m7hol2ltok0843iolzs4yv%2F6f3e298f-d6f9-d7df-14e1-16c4373f2015-H1.jpeg?Expires=1580779837867&KeyName=labelbox-assets-key-1&Signature=Peisze9u3kFKiEMe3MhF3oQKy28","Label":{"objects":[{"featureId":"ck5n7bbwb01n80x8zho6n5uws","schemaId":"ck5n7aw5v70a50952jx55h8xq","title":"test","value":"test","color":"#FF0000","bbox":{"top":9,"left":32,"height":179,"width":206}}],"classifications":[]},"Created By":"jokekeh773@etopmail.com","Project Name":"test","Created At":"2020-01-21T01:30:02.000Z","Updated At":"2020-01-21T01:30:02.000Z","Seconds to Label":11.295,"External ID":"H1.jpeg","Agreement":null,"Benchmark Agreement":null,"Benchmark ID":null,"Benchmark Reference ID":null,"Dataset Name":"test","Reviews":[],"View Label":"https://editor.labelbox.com?project=ck5n7al1pyfvl0843renaiyg9&label=ck5n7bcfn70gl0952omu7827x"},{"ID":"ck5n7bjyxyg8b0843dcbcrroa","DataRow ID":"ck5n7adigecxs0doq1j0qh59a","Labeled Data":"https://storage.labelbox.com/ck5m7hol2ltok0843iolzs4yv%2F1bfec423-7fb9-967b-d27f-24c508e44c6c-H2.jpeg?Expires=1580779837867&KeyName=labelbox-assets-key-1&Signature=Uaj_rPK1LW85fy00WXZPIH34fLo","Label":{"objects":[{"featureId":"ck5n7bizb01p70x8raittrqcd","schemaId":"ck5n7aw5v70a50952jx55h8xq","title":"test","value":"test","color":"#FF0000","bbox":{"top":9,"left":8,"height":165,"width":242}}],"classifications":[]},"Created By":"jokekeh773@etopmail.com","Project Name":"test","Created At":"2020-01-21T01:30:12.000Z","Updated At":"2020-01-21T01:30:12.000Z","Seconds to Label":7.187,"External ID":"H2.jpeg","Agreement":null,"Benchmark Agreement":null,"Benchmark ID":null,"Benchmark Reference ID":null,"Dataset Name":"test","Reviews":[],"View Label":"https://editor.labelbox.com?project=ck5n7al1pyfvl0843renaiyg9&label=ck5n7bjyxyg8b0843dcbcrroa"},{"ID":"ck5n7bv7aj2io0770urp4g1hw","DataRow ID":"ck5n7adigecxw0doq0rl6gyuu","Labeled Data":"https://storage.labelbox.com/ck5m7hol2ltok0843iolzs4yv%2F13551a01-8c22-7698-1600-452dfeddf26a-h3.jpeg?Expires=1580779837867&KeyName=labelbox-assets-key-1&Signature=kOXys9oT2Z3PKCAaN63AKoFrB-A","Label":{"objects":[{"featureId":"ck5n7bucd01pl0x75wg2x03ax","schemaId":"ck5n7aw5v70a50952jx55h8xq","title":"test","value":"test","color":"#FF0000","bbox":{"top":13,"left":34,"height":174,"width":181}}],"classifications":[]},"Created By":"jokekeh773@etopmail.com","Project Name":"test","Created At":"2020-01-21T01:30:27.000Z","Updated At":"2020-01-21T01:30:27.000Z","Seconds to Label":12.32,"External ID":"h3.jpeg","Agreement":null,"Benchmark Agreement":null,"Benchmark ID":null,"Benchmark Reference ID":null,"Dataset Name":"test","Reviews":[],"View Label":"https://editor.labelbox.com?project=ck5n7al1pyfvl0843renaiyg9&label=ck5n7bv7aj2io0770urp4g1hw"}]'
        text= text.replace("null", "0")

        json = eval(text)

        # print(json)
        return json


def makeAnnotation(json, num):
    bbox = json[num]['Label']['objects'][0]['bbox']
    # print(bbox)

    top = json[num]['Label']['objects'][0]['bbox']['top']
    left = json[num]['Label']['objects'][0]['bbox']['left']
    height = json[num]['Label']['objects'][0]['bbox']['height']
    width = json[num]['Label']['objects'][0]['bbox']['width']
    # print(top)
    # print(left)
    # print(height)
    # print(width)

    ExternalID = json[num]['External ID']
    # print(ExternalID)

    annotation='''{
        "annotations": [
            {
                "class": "rect",
                "height": '''+str(height)+''',
                "width": '''+str(width)+''',
                "x": '''+str(left)+''',
                "y": '''+str(top)+'''
            }
        ],
        "class": "image",
        "filename": "'''+ExternalID+'''"
    }'''

    return annotation


main()
