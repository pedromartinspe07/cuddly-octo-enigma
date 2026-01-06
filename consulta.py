import sqlite3

conn = sqlite3.connect("elementos_ficticios.db")
cursor = conn.cursor()

# Buscar todos os metais da Marvel
cursor.execute("""
SELECT nome, descricao FROM elementos_ficticios
WHERE universo = 'Marvel' AND tipo = 'Metal'
""")

resultados = cursor.fetchall()

for nome, descricao in resultados:
    print(f"{nome} → {descricao}")

conn.close()