import time
import pyodbc

print('Entrez le nom:  ')
x = input()

print('Entrez le prénom:  ')
y = input()

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=F:\carte.accdb;')

cursor = conn.cursor()
cursor.execute('select nom_f, pren_f, d_nais, l_nais, annee, nord, ncni, d_etab  from pers where nom_f = ? and pren_f '
               '= ?', x, y)
for row in cursor.fetchall():
    print(row)

cursor2 = conn.cursor()
cursor2.execute('select nom_f, pren_f, d_nais, l_nais, annee, nord, ncni, d_etab  from pers where nom_f = ? and pren_f '
                '= ?', x, y)
rows = cursor2.fetchall()
print('Le nombre de personnes trouvées est:')
print(len(rows))


print('*****************************************************')
print('Cliquez sur une touche pour quitter')
time.sleep(59)
print('Terminé')

