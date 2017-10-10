import MySQLdb
conn=MySQLdb.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='root',
    db='jeesite',
    charset='utf8'
)
cursor=conn.cursor()
sql="select * from sys_user"
cursor.execute(sql)
rs=cursor.fetchone()
print rs
cursor.close()
conn.close()