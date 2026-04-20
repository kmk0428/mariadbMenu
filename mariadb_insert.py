import pymysql
import sys

# MariaDB 접속 정보
DB_HOST = "192.168.100.20"
DB_USER = "cjulib"
DB_PASS = "security"
DB_PORT = 3306
DB_NAME = "cju"

try:
    conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT,
        database=DB_NAME,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    
    with conn.cursor() as cursor:
        # 1. 추가할 데이터 입력 받기
        new_id = input("아이디: ")
        new_pass = input("비밀번호: ")
        new_name = input("이름: ")
        
        # 2. 문자열 합치기 방식으로 쿼리 생성
        # 중요: 문자열 컬럼(VARCHAR)에 값을 넣을 때는 반드시 값 앞뒤에 "'"를 붙여야 합니다.
        sql = "INSERT INTO member (id, pass, name) VALUES ('" + new_id + "', '" + new_pass + "', '" + new_name + "')"
        
        #print(f"\n[실행될 쿼리]: {sql}")
        
        # 3. 쿼리 실행
        cursor.execute(sql)
        
        # 4. 데이터베이스 반영 (INSERT/UPDATE/DELETE 작업 시 필수!)
        conn.commit()
        
        print(f"\n성공적으로 '{new_name}'님의 정보를 추가했습니다.")

except pymysql.MySQLError as e:
    # 에러 발생 시 진행 중인 작업 취소
    if 'conn' in locals():
        conn.rollback()
    print(f"오류 발생: {e}")
    sys.exit(1)

finally:
    if 'conn' in locals() and conn.open:
        conn.close()
        print("연결 종료.")