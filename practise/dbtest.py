import cx_Oracle

#한글 지원 방법
import os

#연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
connection = cx_Oracle.connect('admin','Love1998!!@@','db202001291844_high')

cursor = connection.cursor()

cursor.execute(
   """
   select col1
   from test
   """
)


# cursor.execute(
#    """
#    select c_id
#    from company
#    where text = :texting
#    """,
#    texting = str
# )

for co_id in cursor:
   print("테스트 이름 리스트 : ",co_id[0])
 