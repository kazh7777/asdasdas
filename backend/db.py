import pymysql

def connect_db():
    return pymysql.connect(
        host='project-db-campus.smhrd.com',
        user='campus_23K_AI18_p3_3',
        password='smhrd3',
        db='your_database_name',  
        charset='utf8',
        port=3307
    )

