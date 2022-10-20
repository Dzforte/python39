
def checkchinaZodiac(year):
    baseYear = 1444
    ten = ('갑', '을', '병', '정', '무'
           '기', '경', '신', '임', '계')
    twelve = ('자''축''인''묘''진''사''오''미''신''유''술''해')
    animal = ('쥐''소''호랑이''토끼''용''뱀''말''양''원숭이''닭''개''돼지')

    t10idx = (year - baseYear) % 10
    t12idx = (year - baseYear) % 12


    print(f'{year}년은 {ten[t10idx]}{twelve[t12idx]}년' f'({animal[t12idx]})의 해입니다')

year = int(input('년도는?'))

checkchinaZodiac(year)
