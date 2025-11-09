import sqlite3 

# Initialize table if it does not exist with schema that gives ID, Category of Tools (which is what we search for),
# the name of the tool, and URL of the tool
def init_db():
    # Connect to DB file
    conn = sqlite3.connect('bot_db.db')
    # Idk what this does
    c = conn.cursor()
    # Execute create table with SQL statement
    c.execute('''CREATE TABLE IF NOT EXISTS ctf_tools
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, name TEXT, url TEXT)''')
    # Commits changes
    conn.commit()
    # Close connection
    conn.close()

# Delete the table in our DB
def del_db():
    # Connect to file
    conn = sqlite3.connect('bot_db.db')
    # Idk 
    c = conn.cursor()
    # Drop whole table to get rid of it
    c.execute('''DROP TABLE ctf_tools''')
    # Commit changes to table
    conn.commit()
    # Close connection
    conn.close()

# Add tool to our database with schema #, Category, Name, URL 
def add_tool(category, name, url):
    # Connect to file
    conn = sqlite3.connect('bot_db.db')
    # Yeah
    c = conn.cursor()
    # Insert new tools with their category and link
    c.execute("INSERT INTO ctf_tools (category, name, url) VALUES (?, ?, ?)", (category, name, url))
    # Commit to table
    conn.commit()
    # Close connection
    conn.close()

# Get all tools from table in a category (returned as list of tuples)
def get_tools(category):
    # Connect to file
    conn = sqlite3.connect('bot_db.db')
    # idk
    c = conn.cursor()
    # Select from the category we pass 
    c.execute("SELECT * FROM ctf_tools WHERE category = ?", (category,))
    # Fetch all from our select statement
    tools = c.fetchall()
    # Close 
    conn.close()
    # Return our list of tools
    return tools
