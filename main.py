import pyodbc
conn=pyodbc.connect('Driver={SQL Server};'
                    'Server=LAPTOP-4Q8IGU5U;'
                    'Database=nadzor_sprzedarzy_kamil;'
                    'Trusted_Connection=yes;')
cursor=conn.cursor()
cursor.execute('SELECT * FROM nadzor_sprzedarzy_kamil.dbo.Klient_Kamil')
for row in cursor:
    print(row)
