import sqlite3 

def init_db():
    conn = sqlite3.connect('bot_db.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS ctf_tools
                 (category TEXT, name TEXT PRIMARY KEY, url TEXT)''')
    conn.commit()
    conn.close()

def del_db():
    conn = sqlite3.connect('bot_db.db')
    c = conn.cursor()
    c.execute('''DROP TABLE ctf_tools''')
    conn.commit()
    conn.close()

def add_tool(category, name, url):
    conn = sqlite3.connect('bot_db.db')
    c = conn.cursor()
    c.execute("INSERT INTO ctf_tools (category, name, url) VALUES (?, ?, ?)", (category, name, url))
    conn.commit()
    conn.close()

def get_tools(category):
    conn = sqlite3.connect('bot_db.db')
    c = conn.cursor()
    c.execute("SELECT * FROM ctf_tools WHERE category = ?", (category,))
    tools = c.fetchall()
    conn.close()
    return tools 
