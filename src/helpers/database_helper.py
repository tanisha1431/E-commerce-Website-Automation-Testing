import pymysql

def read_from_db(sql):
    connection=pymysql.connect(host='127.0.0.1' ,port=8889 ,user='root' ,password='root')
    cursor=connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    db_data=cursor.fetchall()
    cursor.close()
    connection.close()
    return db_data

def get_order_number(order_id):
    sql=f"SELECT * FROM test_site_db.wp_posts where ID={order_id};"
    db_order=read_from_db(sql)
    return db_order



