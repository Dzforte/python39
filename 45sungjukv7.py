# ## sungjukv7lib
#
#
#
#
# def readOneSungJuk():
#
#     conn, cur = db.openConn()
#
#     sql = ' select * from sungjuk ' \
#           ' where name = %s '
#     cur.execute(sql, [name])
#     row = cur.fetchone()
#     db.closeConn(conn, cur)
#
#     result = f'{row[0]}{row[1]}{row[2]}{row[3]}{row[4]}{row[5]}{row[6]:.1f}{row[7]}'
#     print(result)
#
#
# def remove SungJuk()
#     name = input('삭제할 데이터의 학생 이름은?')
#
#     conn, cur = db.openConn()
#     sql = 'delete from sungjuk where name = %s'
#     cur.execute(sql, [name])
#     cnt = cur.rowcount
#     conn.commit()
#
#     db.closeConn()
#
#
# def modifySungJuk():
#     name = input('수정할 학ㄱ생 이름은?')
#
#     conn, cur = db.openConn()
#     sql = 'select from sungjuk where name = %s'
#     cur.execute(sql, [name])
#     sj = cur.fetchone()
#     db.closeConn(conn, cur)