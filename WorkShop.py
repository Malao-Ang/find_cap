import sys
from tkinter import Tk,simpledialog,messagebox

def read_file():
    with open('contries.txt','r') as contries:
        for name in contries:
            name = name.rstrip('\n')
            contry,capital = name.split('/')
            contry = contry.capitalize()
            capital = capital.capitalize()
            world_capital[contry] = capital
            
def write_file(contries_name,capital_name):
    with open('contries.txt','a') as contries:
        contries.write('\n')
        contries.write(contries_name+'/'+capital_name)
        contries.close

root = Tk()
root.withdraw()
world_capital = {}
while True:
    read_file()
    simpledialog.askstring
    query_contry = ''
    query_contry = simpledialog.askstring('Contry','Type the name of contry : ')
    query_contry = query_contry.capitalize()
    if query_contry in world_capital:
        result = world_capital[query_contry]
        messagebox.showinfo('Answer',"The cap of"+query_contry+' is '+result)
    else:
        new_capital = simpledialog.askstring('Teach me',"I don't know the Answer! of "+query_contry+' :')
        messagebox.showinfo("Thank !!",'Thank you for new knowledge!')
        new_capital = new_capital.capitalize()
        write_file(query_contry,new_capital)
    
    ans = simpledialog.askstring('Continue','Do you want to try again? y/n:')
    if ans =='n':
        messagebox.showinfo("Thank you !!",'Goodluck Bro') 
        root.destroy()
        sys.exit()
    
    
    
    