import sqlite3

# Conectar ao banco (cria se não existir)
conn = sqlite3.connect("elementos_ficticios.db")
cursor = conn.cursor()

# Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS elementos_ficticios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    universo TEXT NOT NULL,
    tipo TEXT NOT NULL,
    descricao TEXT,
    origem TEXT
)
""")

# Lista de elementos fictícios
elementos = [

    # ================= MARVEL =================
    ("Adamantium", "Marvel", "Metal",
     "Liga metálica praticamente indestrutível",
     "Projeto Arma X"),

    ("Vibranium", "Marvel", "Metal",
     "Metal que absorve e redistribui energia",
     "Wakanda"),

    ("Uru", "Marvel", "Metal",
     "Metal místico asgardiano encantável",
     "Asgard"),

    ("Terrigen Mist", "Marvel", "Químico",
     "Névoa que ativa genes Inumanos",
     "Attilan"),

    ("Pym Particles", "Marvel", "Químico",
     "Partículas que alteram tamanho e massa",
     "Hank Pym"),

    ("Extremis", "Marvel", "Biológico",
     "Nanotecnologia que melhora o corpo humano",
     "A.I.M."),

    ("Darkforce", "Marvel", "Energia",
     "Energia de uma dimensão paralela",
     "Dark Dimension"),

    ("Power Cosmic", "Marvel", "Energia",
     "Energia cósmica de Galactus",
     "Galactus"),

    # ================= DC =================
    ("Kryptonita Verde", "DC", "Mineral",
     "Mineral radioativo que enfraquece kryptonianos",
     "Planeta Krypton"),

    ("Nth Metal", "DC", "Metal",
     "Metal que desafia gravidade e tempo",
     "Thanagar"),

    ("Promethium", "DC", "Metal",
     "Metal radioativo extremamente instável",
     "DC Earth"),

    ("Venom", "DC", "Químico",
     "Soro que aumenta força física",
     "Bane"),

    ("Joker Toxin", "DC", "Químico",
     "Gás neurotóxico que causa riso incontrolável",
     "Coringa"),

    ("Lazarus Pit Fluid", "DC", "Biológico",
     "Substância regenerativa que revive mortos",
     "Ra's al Ghul"),

    ("Speed Force", "DC", "Energia",
     "Campo energético que permite supervelocidade",
     "Multiverso DC"),

    ("Omega Effect", "DC", "Energia",
     "Energia destrutiva controlada por Darkseid",
     "Apokolips")
]

# Inserir dados
cursor.executemany("""
INSERT INTO elementos_ficticios (nome, universo, tipo, descricao, origem)
VALUES (?, ?, ?, ?, ?)
""", elementos)

conn.commit()
conn.close()

print("Banco de dados criado e populado com sucesso!")