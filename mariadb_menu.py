import pymysql
import sys

# 메인 메뉴 루프
def main_menu():
    while True:
        print("\n--- [ 성적 관리 시스템 ] ---")
        print("1. 전체조회")
        print("2. 번호조회")
        print("3. 성적 추가")
        print("4. 성적 삭제")
        print("5. 성적 수정")
        print("6. 종료")
        print("---------------------------")
        
        choice = input("메뉴 선택: ")
        
        if choice == '1':
            #select_all()
            with conn.cursor() as cursor:
                # 전체 성적의 데이터를 조회하는 SQL 쿼리
                sql = "SELECT g.id_grade, m.name, m.id, g.subject, g.score, g.term, g.reg_date FROM member m JOIN grades g ON m.seq = g.member_seq;"
                # print(sql)
        
                # 쿼리 실행
                cursor.execute(sql)

                # 실행 결과 모두 가져오기 (리스트 내 딕셔너리 형태)
                result = cursor.fetchall()

                # 결과 출력하기
                print("\n\n---<전체 성적>---\n번호 | 이름(id) | 과목명 | 점수 | 학기 | 등록일")
                if result:
                    for row in result:
                        print(f"{row['id_grade']} | {row['name']}({row['id']}) | {row['subject']} | {row['score']} | {row['reg_date']}") 
                else:
                    print("데이터가 없습니다.")

                print("\n")

        elif choice == '2':
            #select_one()
            with conn.cursor() as cursor:
                seq_input = input("조회할 번호를 입력하시오 : ")
                sql = "SELECT m.name, m.id, g.term, g.subject, g.score FROM member m JOIN grades g ON m.seq = g.member_seq WHERE m.seq = '" + seq_input + "';"
                # 쿼리 실행
                cursor.execute(sql)

                # 실행 결과 모두 가져오기 (리스트 내 딕셔너리 형태)
                result = cursor.fetchall()
                print(f"\n\n--[{result[0]['name']} 학생의 성적]--\nid: {result[0]['id']}\n학기: {result[0]['term']}\n과목 : 성적")
                for row in result:
                    print(f"{row['subject']} : {row['score']}")
        elif choice == '3':
            #insert_member()
            print("")
        elif choice == '4':
            #delete_member()
            print("")
        elif choice == '5':
            #update_member()
            print("")
        elif choice == '6':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    
    DB_HOST = "192.168.100.20"
    DB_USER = "cjulib"
    DB_PASS = "security"
    DB_PORT = 3306
    DB_NAME = "cju"

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

        main_menu()

    except pymysql.MySQLError as e:
        print(f"데이터베이스 접속 또는 쿼리 실행 중 오류가 발생했습니다: {e}")
        sys.exit(1)
