import pymysql
import os

def connect_db():
    try:
        return pymysql.connect(
            host=os.getenv('DB_HOST', 'project-db-campus.smhrd.com'),
            user=os.getenv('DB_USER', 'campus_23K_AI18_p3_3'),
            password=os.getenv('DB_PASSWORD', 'smhrd3'),
            db=os.getenv('DB_NAME', 'your_database_name'),  
            charset='utf8',
            port=int(os.getenv('DB_PORT', 3307))
        )
    except pymysql.MySQLError as e:
        print(f"데이터베이스 연결 실패: {e}")
        raise e

