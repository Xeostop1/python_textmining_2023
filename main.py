import re

# for 문을 사용 1~100까지 숫자 출력
# +1기억
# for i in range(1,101):
#     print(i)


#b.txt 파일 생성 adcd 내용 쓰기
#b.txt읽어서 출력
# str="abcd"
# f=open("b.text","w")
# f.write(str)
# f=open("b.text","r")
# print(f.read())
#
# #여러줄 추가하기
# str_list=["abc", "efg", "fij", "lnop"]
# f=open("sample.text","w")
# for i in str_list:
#     f.write(i+"\n")
# #여기까지는 되는데~ 왜~~


# 별찍기 js랑 비슷하게 만들어야 되네~
# num=input("별을 추가할 숫자를 입력해 주세요")
# star=""
# for i in range(int(num)):
#     star+="*"
#     print(star)
#
# num=input("별을 추가할 숫자를 입력해 주세요")
# num=int(num)
# #
# # for i in range(1,num+1):
# #     print("*"*num)
#
# #======선생님 코드======
# # num=int(num)
# # for를 중첩으로 건 이유
# for i in range(num):
#     for j in range(num):
#         print("*", end="")
#     print()

# stars = "*" * num  # 초기에는 num 개의 별로 이루어진 문자열을 생성합니다.
# # range(시작, 종료(최대 한계치), 증감(프리퀀시))
# # 그래서 시작을 받은 숫자부터 시작 줄여갈 수있게 세팅
#
# for i in range(num, 0, -1):
#     print(stars)
#     #마지막을 줄일려고 사용
#     stars = stars[:-1]

#====선생님 코드======
# for i in range(num):
#     for j in range(num):


#==========정규표현식===========
#특정한 규칙을 가진 문자열의 집합을 표현하는데 사용하는 형식언어
#복잡한 문자열의 검색과 치환을 위해 사용
#정규표현식 테스트 사이트
#https://regexr.com/
#([A-Z])\w+ 에 있는 것을 모두 추출해라(로그인 하면 사전도 만들 수 있데)
#메타문자 : 원래 그 문자가 지닌 뜻이 아닌 특별한 용도로 사용하는 문자 의미
#[]사이의 문자들과 매치
#[abc] a,b,c 한개의 문자와 매치
#[a-c] 범위 추출
# [0-5] 숫자 사이의 범위
#[a-zA-Z]알파벳 전부
#[0-9]숫자 모두 추출
#[^0-9]^ not 의미 숫자가 아닌 문자만 매칭
# \d = [0-9] 숫자와 매치
# \D 숫자가 아닌 것과 매치
# \s 공백(띄어쓰기와 엔터, 탭) 매치
# \S 공백(띄어쓰기와 엔터, 탭) 매치 제외 나머지 추출
# \w 문자+숫자 [a-zA-Z0-9] 모두 추출
# \ㅉ 문자+숫자 [a-zA-Z0-9] 모두 추출 제외 모두 추출
# . 줄바꿈 문자를 제외한 모든 문자와 매치
# a[.]b : str안에 들어가면 amazon.com 의 .을 추출가능
# * 반복 ca*t a문자가 반복되는 문자를 추출 ct 추출가능
# + 최소 1이상 반복될때 사용함 ct는 안됨
# {m,n} 원하는 반복횟수를 지정할 수 있음
# {3,} 3이상
# {,3} 3이하
# ca{2}t caat 만 출력
# ca{2.5}t 출력
# 2~5까지 출력
# {0,1} → ?의 동일한 기능을 수행 b 문자가 최소 0회 최대 1회는 있어야 함
# # import  re → 정규표현식 임포트
# p=re.compile("ab*")
# 2개 많이 사용
# 매치가 되는 경우 객체를 반환 없으면 none 반환
# **p.match()
# **p.search()
# p.findall()
# p.finditer()



#모든알파벳 최소 1회 반복
p=re.compile('[a-z]+')
m=p.match("python")
print(m)
m=p.match("3 python")
print(m)

#문자열 추출 group()을 통해 매치된 값을 출력할 수 있음
if m:
    print("match found: ", m.group())
else:
    print("no match")

print("="*20)
#======매치와 서치의 차이첨======
# 매치 함수는 1문자열 부터 매칭되는지 확인하기 때문에 매칭되지 않음
# 1부터 *******문자열******부터 확인!!!!
m1=p.match("123 python")
# 문자열 전체를 찾아봄
m2=p.search("123 python")
if m1:
    print("매칭1 단어 찾음", m1.group())
else:
    print("m1 매칭 불가")

if m2:
    print("매칭1 단어 찾음", m2.group())
else:
    print("매칭불가 m2")

print("="*20)
# 컴파일 옵션
# 1. 닷올
p=re.compile('a.b',re.DOTALL)
m=p.match('a\nb')
print(m)

print("="*20)
#대소문자 없이 매칭 re.I
p=re.compile('[a-z]',re.I)
m=p.match("python")
print(m)
m=p.match("python")
print(m)
m=p.match("PYTHON")
print(m)

print("="*20)

#======M 처음부터 마지막 까지
# 파이선으로 시작하고 공백문자를 가지고 있고 문자와 숫자가 매칭되는것  개행하고 1회이상 반복
# 파이선으로 시작하고 공백문자를 가지고 있고 문자와 숫자가 매칭되는것  개행하고 **1회이상 반복** 이부분이 틀렸음
# ^는 문자열 처음, $는 마지막
p=re.compile("^python\s\w+")
data="""python one
life is too short 
python two
you need python
python there"""
#그룹으로 묶으면 str형태 그대로 반환되네
print(p.match(data).group())
print(p.search(data))
print(p.findall(data))
