# -*- coding:UTF-8 -*-
import MySQLdb
print "Content-Type:text/html"
print
print "<html><head><title>书本</title></head>"
print "<body>"
print "<h1>书本</h1>"
print "<ul>"
connection=MySQLdb.connect(user='root',passwd='root',db='hello')
cursor=connection.cursor()
cursor.execute('select name from student order by age DESC limit 2 ')
for row in cursor.fetchall():
    print "<li>%s</li>" %row[0]
print "</ul>"
print "</body></html>"