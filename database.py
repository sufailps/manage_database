import MySQLdb as mysql

print("Database")
db = mysql.connect(host='localhost', user='root',
                   password='root', db="INFORMATION_SCHEMA")
cur = db.cursor()
cur.execute('SHOW STATUS')
res = cur.fetchall()
r = dict(res)
print( f"Uptime => {r['Uptime']}")
print(f"Threads_created => {r['Threads_created']}")
print(f"Threads_connected => {r['Threads_connected']}")
print(f"Threads_running => {r['Threads_running']}")
print(f"Queries => {r['Queries']}")
print(f"Max_used_connections => {r['Max_used_connections']}")
print("Process List")
cur.execute("select * from PROCESSLIST")
res1=cur.fetchall()
#print(res1)
for i in res1:
	print(f"Id : {i[0]} | User info : {i[1]} | Host : {i[2]} | DB : {i[3]} | Command : {i[4]} | Time : {i[5]} | State : {i[6]} | Info : {i[7]}")

cur.close()
