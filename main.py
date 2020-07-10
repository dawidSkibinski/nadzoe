import pyodbc
conn=pyodbc.connect('Driver={SQL Server};'
                    'Server=LAPTOP-4Q8IGU5U;'
                    'Database=nadzor_sprzedarzy_kamil;'
                    'Trusted_Connection=yes;')
cursor=conn.cursor()

def wyciaganie():
    cursor.execute('SELECT * FROM nadzor_sprzedarzy_kamil.dbo.klient')
    for list_database in cursor:
        print(list_database)
wyciaganie()


def dodawanie(imie1, nazwisko1):
    cursor.execute(f"INSERT INTO klient (imie, nazwisko) values ('{imie1}','{nazwisko1}')")
    conn.commit()
dodawanie("Pawelek","Kuzniak")
wyciaganie()










