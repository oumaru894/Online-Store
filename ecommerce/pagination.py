from cs50 import SQL

#db = SQL("sqlite:///items.db")

#m = db.execute("select * from items limit 5")
#print(m,'\n\n\n\n')
#print(len(m),'\n\n\n\n')

#print(m[1]['name'],'\n\n\n\n')

db = SQL("sqlite:///items.db")
#printing the next or prevous page

        
def page(page, m):
    # Next page
    if page == 1:
        n = m[-1]["id"]
        data = db.execute("select * from items where id > ? limit 16", n)
        return data
    
    # Previous page
    elif page == -1:
        n = m[-1]["id"]
        data = db.execute("select * from items where id < ? limit 16", n)
        return data
    
    return
        


