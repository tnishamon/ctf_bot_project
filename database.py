import sqlite3 

def init_db():
    conn = sqlite3.connect('bot_db.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS ctf_tools
                 (tool_category TEXT PRIMARY KEY, name TEXT, url TEXT)''')
    conn.commit()
    conn.close

def add_tool(tool_category, name, url):
    conn = sqlite3.connect('bot_db.db')
    c = conn.cursor()
    c.execute("INSERT INTO ctf_tools (tool_category, name, url) VALUES (?, ?, ?)", (tool_category, name, url))
    conn.commit()
    conn.close()

def get_user(tool_category):
    conn = sqlite3.connect('bot_db.db')
    c = conn.cursor()
    c.execute("SELECT * FROM ctf_tools WHERE tool_category = ?", (tool_category,))
    tools = c.fetchall()
    conn.close()
    return tools