import pandas as pd
from Tkinter import *
from tkMessageBox import showinfo


def valor_alvo(val_ini,qt,tx,ct=12.0):
    val_ini = qt * val_ini
    val_exp = val_ini*(1+tx)
    val_exp = val_exp+(ct*2)
    val_exp = val_exp/qt
    return val_exp
    

class GuiApp(object):
    def __init__(self, master):
        self.master = master
        self.master.title("Get Valor Futuro")
        self.master.focus_force()
        
        # labels
        
        Label(master, text="Valor").grid(row=0,column=0,sticky=W,padx=10)
        Label(master, text="Qtde").grid(row=1,column=0,sticky=W,padx=10)
        Label(master, text="TIR (%)").grid(row=2,column=0,sticky=W,padx=10)
        
        # entrys
        
        self.entry_valor_ini = Entry(master,width=10)
        self.entry_valor_ini.grid(column=1,row=0,sticky=W,padx=10)
        
        self.entry_qtde = Entry(master,width=10)
        self.entry_qtde.grid(column=1,row=1,sticky=W,padx=10)
        
        self.entry_tir = Entry(master,width=10)
        self.entry_tir.grid(column=1,row=2,sticky=W,padx=10)
        
        # buttons

        self.cancel_button = Button(master, text="Cancel", command=self.cancel,width=10)
        self.cancel_button.grid(column=0,row=3)
        
        self.run_button = Button(master, text="Run", command=self.run,width=10)
        self.run_button.grid(column=1,row=3)
    
    def cancel(self):
        self.master.destroy()
    
    def run(self):
        
        # capture entrys values
        
        valor_inicial = float(self.entry_valor_ini.get().replace(',','.'))
        quantidade = float(self.entry_qtde.get().replace(',','.'))
        tir = float(self.entry_tir.get().replace(',','.'))/100
        
        result = valor_alvo(valor_inicial,quantidade,tir)
        result_str = 'Venda sugerida no valor:\n{:.2f}'.format(result).replace(".",',')
        
        showinfo('SUCESS',result_str)
        
    def start(self):
        self.master.mainloop()
        
# parte de inicializacao do programa (nao mexer)

def main():

	master = Tk()
	app = GuiApp(master)
	app.start()

	exit()

if __name__ == '__main__':
	main()
