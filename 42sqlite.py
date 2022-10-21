# 파이썬으로 데이터 다루기 2 - insert

import sqlite3

# 회원정보 입력받기
userid = input('아이디는?')
passwd = input('비밀번호는?')
name = input('이름은?')
email = input('이메일은>')

conn = sqlite3.connect('c:/Java/bigdata.db')
cur = conn.cursor()

# 아래 방식은 비추 (해킹 위험)
# sql = 'insert into member values ('+userid+', '+passwd+', '+name+', '+email+')'
# sql = f'insert into member values ({userid}, {passwd}, {name}, {email})'

# 매개변수 placeholder를 이용해서 실제 값 지정
sql = f'insert into member values (?, ?, ?, ?)'
params = (userid, passwd, name, email)
cur.execute(sql, params)
conn.commit()  # 테이블에 값 저장
print(cur.rowcount, '행이 추가됨!')

cur.close()
conn.close()


# 파이썬으로 데이터 다루기 3 - update
# 수정할 회원의 아이디를 입력받아 회원 정보 수정



import sqlite3

# 수정할 아이디 입력 후 회원정보 수정하기
userid = input(' 수정할 아이디는? ')
passwd = input(' 새로운 비밀번호는? ')
name = input(' 새로운 이름은? ')
email = input(' 새로운 이메일은? ')

conn = sqlite3.connect('c:/Java/bigdata.db')
cur = conn.cursor()

sql = f' update member set passwd = :pwd, name = :name, email = :eml where userid = :uid '
params = {'pwd':passwd, 'name':name, 'eml':email, 'uid':userid}
cur.execute(sql, params)
conn.commit()
print(cur.rowcount, '행이 수정됨!')

cur.close()
conn.close()


# 파이썬으로 데이터 다루기 4 - delete
# 삭제할 회원의 아이디를 입력받아 회원 정보 수정

userid = input(' 삭제할 아이디는? ')

conn = sqlite3.connect('c:/Java/bigdata.db')
cur = conn.cursor()

sql = f' delete from member where userid = :uid '
params = {'uid':userid}
cur.execute(sql, params)
conn.commit()
print(cur.rowcount, '행이 삭제됨!')

cur.close()
conn.close()