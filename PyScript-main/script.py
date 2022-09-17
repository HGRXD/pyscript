import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://www.instagram.com/rlaxd_08/" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["red", "blue"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "김태우")
write("description", "중학교2학년")
write("button", "link to instagram")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "학교": "선인국제중학교",
  "나이": "15",
  "폰번호": "010-4890-1466",
  "이메일": "tw080401@naver.com"
}
information(informations)
