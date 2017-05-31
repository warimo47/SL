from tkinter import *
from tkinter import font

import urllib.request
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree

window = Tk()
window.title("관광지 정보 조회 서비스")
window.geometry("900x470+100+10")
DataList = []

def InitTopText():
	TempFont = font.Font(window, size = 20, weight = 'bold', family = 'Consolas')
	MainText = Label(window, font = TempFont, text = "[관광지 정보 조회 서비스 App]")
	MainText.place(x = 250)

def InitBtn관광지():
    global Btn관광지

    TempFont = font.Font(window, size = 12, weight = 'bold', family = 'Consolas')

    Btn관광지 = Button(window, font = TempFont, text = "관광지",  command = PutBtn관광지)
    Btn관광지.place(x = 10, y = 50, width = 200, height = 200)

def InitBtn문화시설():
    global Btn문화시설

    TempFont = font.Font(window, size = 12, weight = 'bold', family = 'Consolas')
    Btn문화시설 = Button(window, font = TempFont, text = "문화시설", command = PutBtn문화시설)
    Btn문화시설.place(x = 220, y = 50, width = 200, height = 200)

def InitBtn행공축():
    global Btn행공축

    TempFont = font.Font(window, size = 12, weight = 'bold', family = 'Consolas')
    Btn행공축 = Button(window, font = TempFont, text = "행사 / 공연 / 축제", command = PutBtn행공축)
    Btn행공축.place(x = 10, y = 260, width = 200, height = 200)

def InitBtn여행코스():
    global Btn여행코스

    TempFont = font.Font(window, size = 12, weight = 'bold', family = 'Consolas')
    Btn여행코스 = Button(window, font = TempFont, text = "여행코스", command = PutBtn여행코스)
    Btn여행코스.place(x = 220, y = 260, width = 200, height = 200)

def InitBtn레포츠():
    global Btn레포츠

    TempFont = font.Font(window, size = 12, weight = 'bold', family = 'Consolas')

    Btn레포츠 = Button(window, font = TempFont, text = "레포츠",  command = PutBtn레포츠)
    Btn레포츠.place(x = 430, y = 50, width = 200, height = 200)

def InitBtn숙박():
    global Btn숙박

    TempFont = font.Font(window, size = 12, weight = 'bold', family = 'Consolas')
    Btn숙박 = Button(window, font = TempFont, text = "숙박", command = PutBtn숙박)
    Btn숙박.place(x = 640, y = 50, width = 200, height = 200)

def InitBtn쇼핑():
    global Btn쇼핑

    TempFont = font.Font(window, size = 12, weight = 'bold', family = 'Consolas')
    Btn쇼핑 = Button(window, font = TempFont, text = "쇼핑", command = PutBtn쇼핑)
    Btn쇼핑.place(x = 430, y = 260, width = 200, height = 200)

def InitBtn음식점():
    global Btn음식점

    TempFont = font.Font(window, size = 12, weight = 'bold', family = 'Consolas')
    Btn음식점 = Button(window, font = TempFont, text = "음식점", command = PutBtn음식점)
    Btn음식점.place(x = 640, y = 260, width = 200, height = 200)

def InitBtn이전():
    global Btn이전

    TempFont = font.Font(window, size = 12, weight = 'bold', family = 'Consolas')
    Btn이전 = Button(window, font = TempFont, text = "이전", command = PutBtn이전)
    Btn이전.place(x = 10, y = 500, width = 100, height = 50)

def InitInputLabel():
    global InputLabel
    TempFont = font.Font(window, size = 15, weight = 'bold', family = 'Consolas')
    InputLabel = Entry(window, font = TempFont, width = 26, borderwidth = 12, relief = 'ridge')
    InputLabel.place(x = 10, y = 105)

def MoveBtns():
    RenderText.place(y = 110)
    Btn관광지.place(y = 500)
    Btn문화시설.place(y = 500)
    Btn행공축.place(y = 500)
    Btn여행코스.place(y = 500)
    Btn레포츠.place(y = 500)
    Btn숙박.place(y = 500)
    Btn쇼핑.place(y = 500)
    Btn음식점.place(y = 500)
    Btn이전.place(y = 50)

def MoveBtnsBack():
    RenderText.place(y = 500)
    Btn관광지.place(y = 50)
    Btn문화시설.place(y = 50)
    Btn행공축.place(y = 260)
    Btn여행코스.place(y = 260)
    Btn레포츠.place(y = 50)
    Btn숙박.place(y = 50)
    Btn쇼핑.place(y = 260)
    Btn음식점.place(y = 260)
    Btn이전.place(y = 500)

def PutBtn관광지():
    global 장소
    print("관광지 눌림")
    MoveBtns()
    오퍼레이션 = "areaBasedList?contentTypeId=12&arrange=B&numOfRows=10000"
    관광지정보조회(오퍼레이션, "관광지")

def PutBtn문화시설():
    global 장소
    print("문화시설 눌림")
    MoveBtns()
    오퍼레이션 = "areaBasedList?contentTypeId=14&arrange=B&numOfRows=10000"
    관광지정보조회(오퍼레이션, "문화시설")

def PutBtn행공축():
    print("행사/공연/축제 눌림")
    MoveBtns()
    오퍼레이션 = "areaBasedList?contentTypeId=15&arrange=B&numOfRows=10000"
    관광지정보조회(오퍼레이션, "행사/공연/축제 장소")

def PutBtn여행코스():
    print("여행코스 눌림")
    MoveBtns()
    오퍼레이션 = "areaBasedList?contentTypeId=25&arrange=B&numOfRows=10000"
    관광지정보조회(오퍼레이션, "여행코스")

def PutBtn레포츠():
    print("레포츠 눌림")
    MoveBtns()
    오퍼레이션 = "areaBasedList?contentTypeId=28&arrange=B&numOfRows=10000"
    관광지정보조회(오퍼레이션, "레포츠 장소")

def PutBtn숙박():
    print("숙박 눌림")
    MoveBtns()
    오퍼레이션 = "areaBasedList?contentTypeId=32&arrange=B&numOfRows=10000"
    관광지정보조회(오퍼레이션, "숙박 장소")

def PutBtn쇼핑():
    print("쇼핑 눌림")
    MoveBtns()
    오퍼레이션 = "areaBasedList?contentTypeId=38&arrange=B&numOfRows=10000"
    관광지정보조회(오퍼레이션, "쇼핑 장소")

def PutBtn음식점():
    print("음식점 눌림")
    MoveBtns()
    오퍼레이션 = "areaBasedList?contentTypeId=39&arrange=B&numOfRows=10000"
    관광지정보조회(오퍼레이션, "음식점")

def PutBtn이전():
    print("이전 눌림")
    MoveBtnsBack()

def InitRenderText():
    global RenderText, RenderTextScrollbar

    RenderTextScrollbar = Scrollbar(window)
    RenderTextScrollbar.pack()

    TempFont = font.Font(window, size = 10, family = 'Consolas')
    RenderText = Text(window, width = 120, height = 25, borderwidth = 5, relief = 'ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.place(x = 10, y = 470)

    # RenderTextScrollbar.place(x = 10, y = 105)
    RenderTextScrollbar.config(command = RenderText.yview)
    RenderTextScrollbar.pack(side = RIGHT, fill = BOTH)

    # RenderText.configure(state = 'disabled')

def InitLabelFrame():
	pass

def 관광지정보조회(오퍼레이션, 장소):
    global dom, items

    MyKey = "zF0nGrq%2Fzgij4X82J6L0R%2Fq67SaZUP4Nh1tkRu5QB3bYKse0i5qxEaVQxnlNHTmq4tu%2FemPqgC80sZRjRvbOCw%3D%3D"
    MyUrl = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/%s&ServiceKey=%s&MobileOS=AND&MobileApp=appName" % (오퍼레이션, MyKey)
    dom = parse(urllib.request.urlopen(MyUrl))
    items = dom.getElementsByTagName("item")

    number = 1
    RenderText.delete("1.0", END)

    for item in items:
        for node in item.childNodes:
            if node.nodeName == "title":
                # print(node.childNodes[0].nodeValue)
                순서이전 = "%d]" % number
                순서 = 순서이전.rjust(5)
                출력문자열 = "[" + 순서 + " %s 이름 : " % 장소 + node.childNodes[0].nodeValue + "\n"
                RenderText.insert(str(number) + ".0", 출력문자열)
                number  = number + 1

def PrintDOMtoXML():
    print(dom.toxml())

InitTopText()

InitBtn관광지()
InitBtn문화시설()
InitBtn행공축()
InitBtn여행코스()
InitBtn레포츠()
InitBtn숙박()
InitBtn쇼핑()
InitBtn음식점()

InitBtn이전()
InitRenderText()

window.mainloop()