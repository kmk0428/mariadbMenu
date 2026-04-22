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
        print("---------------------------\n\n\n")
        
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
                print("---<전체 성적 조회>---\n번호 | 이름(id) | 과목명 | 점수 | 학기 | 등록일")
                if result:
                    for row in result:
                        print(f"{row['id_grade']} | {row['name']}({row['id']}) | {row['subject']} | {row['score']} | {row['reg_date']}") 
                else:
                    print("데이터가 없습니다.")

                print("")


        elif choice == '2':
            #select_one()
            with conn.cursor() as cursor:

                # 조회할 학생정보 입력
                seq_input = input("---<학생 성적 조회>---\n조회할 번호를 입력하시오 : ")
                sql = "SELECT m.name, m.id, g.term, g.subject, g.score, g.reg_date FROM member m JOIN grades g ON m.seq = g.member_seq WHERE m.seq = '" + seq_input + "';"
                
                # 쿼리 실행
                cursor.execute(sql)

                # 실행 결과 모두 가져오기 (리스트 내 딕셔너리 형태)
                result = cursor.fetchall()

                # 결과 출력하기
                print(f"\n--[{result[0]['name']} 학생의 성적]--\n\n----------------\nid: {result[0]['id']}\n학기: {result[0]['term']}\n----------------\n\n[____과목____ : _성적_]")
                for row in result:
                    print(f"{row['subject']} : {row['score']}")
                print("")


        elif choice == '3':
            #insert_member()
            with conn.cursor() as cursor:

                # 조회할 학생 번호 입력
                seq_input = input("---<학생 성적 추가>---\n조회할 번호를 입력하시오 : ")
                sql = "SELECT seq, name, id FROM member WHERE seq = '" + seq_input + "';"
                print("")

                # 쿼리 실행
                cursor.execute(sql)
                
                # 실행 결과 모두 가져오기 (리스트 내 딕셔너리 형태)
                result = cursor.fetchall()

                # 조회 성공여부 확인
                if result:
                    print(f"{result[0]['seq']} | {result[0]['name']} | {result[0]['id']}")

                else:
                    print("--[조회한 학생이 없습니다.]--")
                    continue
                
                # 추가할 정보 입력
                print(f"{result[0]['name']} 학생 성적 추가")
                term_input = input("학기 : ")
                subject_input = input("과목 : ")
                score_input = input("성적 : ")

                # 추가한 정보 반영
                sql = "INSERT INTO grades (member_seq, term, subject, score) VALUES ('" + seq_input +"', '" + term_input +"', '" + subject_input +"', '" + score_input +"')"

                # 쿼리 실행
                cursor.execute(sql)

                # 데이터베이스 반영
                conn.commit()

                # 정상적으로 추가 되었는지 확인
                sql = "SELECT m.name, m.id, g.term, g.subject, g.score FROM member m JOIN grades g ON m.seq = g.member_seq WHERE m.seq = '" + seq_input + "';"
                
                # 쿼리 실행
                cursor.execute(sql)
                
                # 실행 결과 모두 가져오기 (리스트 내 딕셔너리 형태)
                result = cursor.fetchall()

                # 결과 출력하기
                print(f"\n--[{result[0]['name']} 학생의 성적]--\n\n----------------\nid: {result[0]['id']}\n학기: {result[0]['term']}\n----------------\n\n[____과목____ : _성적_ | ____추가한_시간____]")
                for row in result:
                    print(f"{row['subject']} : {row['score']} | {row['reg_date']}")
                                
                print("")


            print("")
        elif choice == '4':
            #delete_member()
            with conn.cursor() as cursor:

                # 성적을 삭제할 학생 조회
                seq_input = input("---<학생 성적 삭제>---\n조회할 번호를 입력하시오 : ")
                sql = "SELECT m.name, m.id, g.term, g.id_grade, g.subject, g.score FROM member m JOIN grades g ON m.seq = g.member_seq WHERE m.seq = '" + seq_input + "';"

                # 쿼리 실행
                cursor.execute(sql)

                # 실행 결과 모두 가져오기 (리스트 내 딕셔너리 형태)
                result = cursor.fetchall()

                # 결과 출력하기
                print(f"\n--[{result[0]['name']} 학생의 성적]--\n\n----------------\nid: {result[0]['id']}\n학기: {result[0]['term']}\n----------------\n\n[____과목____ : _성적_]")
                for row in result:
                    print(f"{row['id_grade']}. {row['subject']} : {row['score']}")


                # 삭제할 성적 입력
                id_grade_input = input("\n삭제할 과목번호를 입력하시오 : ")
                valid_ids = [str(row['id_grade']) for row in result]
                if id_grade_input in valid_ids:
                    sql = "DELETE FROM grades WHERE id_grade = '" + id_grade_input + "';"

                else:
                    print("입력한 번호는 없습니다.")
                    continue

                # 쿼리 실행
                cursor.execute(sql)

                # 데이터베이스 반영
                conn.commit()

                # 결과 확인
                sql = "SELECT m.name, m.id, g.term, g.id_grade, g.subject, g.score FROM member m JOIN grades g ON m.seq = g.member_seq WHERE m.seq = '" + seq_input + "';"

                # 쿼리 실행
                cursor.execute(sql)

                # 실행 결과 모두 가져오기 (리스트 내 딕셔너리 형태)
                result = cursor.fetchall()

                # 결과 출력하기
                print(f"\n--[{result[0]['name']} 학생의 성적]--\n\n----------------\nid: {result[0]['id']}\n학기: {result[0]['term']}\n----------------\n\n[____과목____ : _성적_]")
                for row in result:
                    print(f"{row['id_grade']}. {row['subject']} : {row['score']}")


            print("")
        elif choice == '5':
            #update_member()
            with conn.cursor() as cursor:

                # 성적을 수정할 학생 조회
                seq_input = input("---<학생 성적 수정>---\n조회할 번호를 입력하시오 : ")
                sql = "SELECT m.name, m.id, g.term, g.id_grade, g.subject, g.score FROM member m JOIN grades g ON m.seq = g.member_seq WHERE m.seq = '" + seq_input + "';"

                # 쿼리 실행
                cursor.execute(sql)

                # 실행 결과 모두 가져오기 (리스트 내 딕셔너리 형태)
                result = cursor.fetchall()

                # 결과 출력하기
                print(f"\n--[{result[0]['name']} 학생의 성적]--\n\n----------------\nid: {result[0]['id']}\n학기: {result[0]['term']}\n----------------\n\n[____과목____ : _성적_]")
                for row in result:
                    print(f"{row['id_grade']}. {row['subject']} : {row['score']}")

                # 성적 업데이트
                sql = "UPDATE grades SET score = %s WHERE id_grade = %s"

                # 수정할 과목
                id_grade_input = input("\n\n수정할 과목번호를 입력하시오 : ")

                # 새로운 성적
                new_score = input("\n새로운 성적을 입력하시오 : ")

                # 쿼리 실행
                affected_rows = cursor.execute(sql, (new_score, id_grade_input))

                # 데이터베이스 반영
                conn.commit()

                # 결과 조회
                if affected_rows > 0:
                    print("\n[" + f"{result[0]['name']} 학생의 성적이 {new_score}점으로 변경되었습니다.]")
                else:
                    print("\n실패하였습니다.")


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
    finally:
        # 연결 종료
        if 'conn' in locals() and conn.open:
            conn.close()
            print("\n데이터베이스 연결이 안전하게 종료되었습니다.")