#
# 파이썬기초 코딩
# Print 구문의 이해

print("안녕하세요")
print("VS Code 테마 변경입니다.")

# 기본출력
print('hello pyhon!')
print("hello python!!")
print("""hello pyhon!""")
print('''hello pyhon!''')

#Separator 옵션 사용
print('T','E','S','T',sep='')
print('2019','02','19','T',sep='-')
print('niceman','goole.com',sep='@')

#end 옵션 사용
print("welcome TO ",end=" ")
print('the black parade',end='')
print('piano notes')

#format 사용 [], {} , ()
print('{} and {}'.format('You','Me'))
print("{0} and {1} and {0}".format('You','Me'))
print("{a} are {b}".format(a='You', b='Me'))

 # %s : 문자 , %d : 정수, %f : 실수
print("%s's faverite number is %d" %('Eunki',7))
print("Test1: %5d, Price:  %4.2f" %(776,6534.123))
print("Test1: {0: 5d}, price: {1: 4.2f}".format(776,6534.123))
print("Test1: {a: 5d}, price: {b: 4.2f}".format(a= 776,b =6534.123))