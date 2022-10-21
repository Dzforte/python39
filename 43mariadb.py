# mariaDB로 데이터 다루기 - select
# pymysql 모듈을 먼저 설치 :

import pymysql

url = 'bigdatadb.....~~~~ ap.nort...~~~~~'
userid = 'admin'
passwd = 'bigdata_2022'
dbname = 'bigdata'

conn = pymysql.connect(host=url, user=userid,
                       passwd=passwd, database=dbname,
                       charset='utf8') # 접속

cur = conn.cursor()
sql = 'select userid, passwd, name, email from member'
cur.execute(sql)

result=''
rows = cur.fetchall()
for row in rows:
    result += f'{row[0], row[1], row[2], row[3]} \n'

cur.close()
conn.close() # 접속 종료

print(result)

#############################

# MariaDB 데이터 입력하기
uid = input('아이디는?')
pwd = input('비밀번호는?')
name = input('이름은?')
email = input('이메일은>')

conn = pymysql.connect(host=url, user=userid,
                       passwd=passwd, database=dbname,
                       charset='utf8') # 접속
cur = conn.cursor()

sql = f' insert into member values (userid, passwd, name, email) values(%s,%s,%s,%s) '
params = (uid, pwd, name, email)

cur.execute(sql, params)
conn.commit()  # 테이블에 값 저장
print(cur.rowcount, '행이 추가됨!')

cur.close()
conn.close()
