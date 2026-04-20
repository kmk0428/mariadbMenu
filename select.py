import pymysql
import sys

# MariaDB 접속 정보
DB_HOST = "192.168.100.20"
DB_USER = "cjulib"
DB_PASS = "security"
DB_PORT = 3306
DB_NAME = "cju"  # 접속할 데이터베이스 지정

try:
    # 데이터베이스 연결
    conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT,
        database=DB_NAME,  # cju 데이터베이스로 연결
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    
    print(f"성공적으로 '{DB_NAME}' 데이터베이스에 접속했습니다!\n")
    
    # 커서 생성
    with conn.cursor() as cursor:
        # member 테이블의 모든 데이터를 조회하는 SQL 쿼리
        sql = "SELECT seq, id, NAME FROM member;"
        
        # 쿼리 실행
        cursor.execute(sql)
        
        # 실행 결과 모두 가져오기 (리스트 내 딕셔너리 형태)
        result = cursor.fetchall()
        
        # 결과 출력하기
        print(f"--- member 테이블 조회 결과 (총 {len(result)}건) ---")
        if result:
            print("id name")
            for row in result:
                #print(row)
                # 예: 특정 컬럼만 출력하고 싶다면 아래와 같이 사용할 수 있습니다.
                print(f"{row['id']}, {row['NAME']}") 
        else:
            print("데이터가 없습니다.")

except pymysql.MySQLError as e:
    print(f"데이터베이스 접속 또는 쿼리 실행 중 오류가 발생했습니다: {e}")
    sys.exit(1)

finally:
    # 연결 종료
    if 'conn' in locals() and conn.open:
        conn.close()
        print("\n데이터베이스 연결이 안전하게 종료되었습니다.")