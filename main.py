import sqlite3, sys, colorama


conn = sqlite3.connect("notes.db")
c = conn.cursor() 



class Colors:
    def __init__(self):
        self.colors = ['BLACK', 'BLUE', 'CYAN', 'GREEN', 'MAGENTA', 'RED', 'WHITE', 'YELLOW']
        self.codes = {color: getattr(colorama.Fore, color) for color in self.colors}

    def __getattr__(self, name):
        if name.upper() in self.codes:
            return self.codes[name.upper()]
        else:
            return ''


color = Colors()


def getnotes(name):
    c.execute("SELECT name, desc FROM notes WHERE name=?",(name,))
    rows = c.fetchone()
    if rows is not None:
        notename, notedesc = rows
        return [notename, notedesc]
    else:
        print(color.red + "No notes found")
        


def display():
  c.execute("SELECT * FROM notes")
  rows = c.fetchall()
  for row in rows:
      name = row[1]
      print(color.black + f"note: {name}")
      
      

def addnotes(name, desc):
    c.execute("INSERT INTO notes (name, desc) VALUES (?, ?)", (name, desc))
    conn.commit()
    


def delnotes(name):
    c.execute("DELETE FROM notes WHERE name=?", (name,))
    conn.commit()

def main():
    print(color.yellow + """ 
1. Display notes
2. View note
3. Add notes
4. Delete notes
5. Exit
""")
    
    prompt = input(color.cyan + "[choose]> ")
    if prompt == "1":
        display() 
    elif prompt == "2":
        name = input(color.cyan + "name: ")
        note = getnotes(name)
        print(f""" 
Name: {note[0]}
Note: {note[1]} 
""")
    elif prompt == "3":
        name = input(color.cyan + "name: ")
        desc = input (color.cyan + "note: ")
        addnotes(name, desc)
        print(color.green + "Notes added")
    elif prompt == "4":
        name = input("name: ")
        delnotes(name)
        print(color.red + "Notes deleted")
    elif prompt == "5":
        sys.exit()
    else:
        print(color.red + "404")
        



while True:
   main()


