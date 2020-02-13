
#------------------------------------------------------------------------------
# 1. Oracle12c Instant Client x64 Basic Package Destribution Download & Install
#   a. Download URL: https://www.oracle.com/kr/database/technologies/instant-client/winx64-64-downloads.html
#   b. Install: C:\app\ 폴더 밑에 바로 압축해제 -> 설치완료
#   c. C:\app\instantclient_12_1 폴더 밑에 아래 서브 폴더 생성
#       instantclient_12_1\network\admin 폴더생성
#
# 2. Oracle12c Instant Client 설치폴더를, 시스템 PATH 환경변수에 추가
#
# 3. Oracle Cloud ATP Wallet 압축파일을 아래 폴더에 해제
#      C:\app\instantclient_12_1\network\admin
# 
# 4. 아래 프로그램으로 연결 및 fetch 테스트 수행
#
#------------------------------------------------------------------------------

from __future__ import print_function

import cx_Oracle


connection = cx_Oracle.connect('admin','Love1998!!@@','db202001291844_high')

sql = """
select * from test"""
        

print("* Get all rows via iterator:")

cursor = connection.cursor()

resultSet = cursor.execute(sql)
print('\t+ resultSet:', type(resultSet))
print()

for result in resultSet:
    print(type(result), ':', result)
    pass

print()

# print(dir(cursor))
# print('-'*80)
# print(dir(connection))

cursor.close()
connection.close()