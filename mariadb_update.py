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
        # 1. 수정할 SQL 쿼리 (SET은 변경할 컬럼, WHERE는 대상 조건)
        sql = "UPDATE member SET name = %s WHERE seq = %s"
        target_seq = input("변경할 id를 선택: ")
        new_name = input("새 이름: ")
        
        # 2. 쿼리 실행
        affected_rows = cursor.execute(sql, (new_name, target_seq))
        
        # 3. 변경 사항 반영 (필수!)
        conn.commit()
        
        if affected_rows > 0:
            print(f"성공: ID가 '{target_seq}'인 사용자의 이름을 '{new_name}'으로 수정했습니다.")
        else:
            print(f"알림: ID가 '{target_seq}'인 사용자를 찾을 수 없어 수정되지 않았습니다.")

except pymysql.MySQLError as e:
    if 'conn' in locals():
        conn.rollback()
    print(f"오류 발생: {e}")
    sys.exit(1)

finally:
    if 'conn' in locals() and conn.open:
        conn.close()
