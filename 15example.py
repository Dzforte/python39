#48 지금 현재 수지의 통장잔액이 25,000원이다. 은행이자가 연 6%라 가정할 때,
# 몇 년이 지나야 통장잔액이 지금의 2배를 넘는지 알아보는 프로그램을 아래 그림을 참고하여 작성하여라. (ComputeInvestment)

money = int(input('잔액을 입력하세요'))
money2 = money*2
year = 0

while True :
    j = 0
    if money > money2 :
        break
    else :
        money += money*0.06
        year += 1
print(f'{money:.0f} 원, {year} 년')


#51
print(f'''
            Multiplication Table
--------------------------------------------''')
for i in range (1,10):
    print(f'{i} {i*2} {i*3} {i*4} {i*5} {i*6} {i*7} {i*8} {i*9} ')





#53
# ( (년도-1)*365 + (년도-1)/4 - (년도-1)/100 + (년도-1)/400) % 7) + 1)
# 0 : 일, 1 : 월, 2 : 화, … … , 6 : 토

year = int(input('연도를 입력하세요'))
exyear31 = (((year-1)*365 + (year-1)/4 - (year-1)/100 + (year-1)/400) % 7)

# 0 = 일, 1 = 월 .....
print(exyear31) ## 입력한 년도의 12월 31일의 요일  *마지막날

