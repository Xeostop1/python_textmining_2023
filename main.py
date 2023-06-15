
# for 문을 사용 1~100까지 숫자 출력
# +1기억
for i in range(1,101):
    print(i)


#b.txt 파일 생성 adcd 내용 쓰기
#b.txt읽어서 출력
str="abcd"
f=open("b.text","w")
f.write(str)
f=open("b.text","r")
print(f.read())



