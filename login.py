import tkinter

r = tkinter.Tk()

r.geometry("400x400")

r.wm_title("Login")

def apagar():

    inputUser.delete(0,"end")

    inputPass.delete(0,"end")

def validacao():
    pu = str(inputUser.get())
    ps = inputPass.get()
    val = 0
    
    arq = open("t.txt","r")
    for line in arq:
        if(line == pu+"\n"):
            print("User válidado")
            val = 1
        if(line == ps+"\n"):
            print("Senha válida")
            val += 1
    arq.close()
    if(val == 2):
        print("Acesso confirmado")
    else:
        print("Acesso negado")
    
           
            

def increvase():

    def ap():

        inputlog.delete(0,"end")

        inputp.delete(0,"end")
    
    def enviar():

        pw = str(inputp.get())

        user = str(inputlog.get())

        arquivo = open("t.txt","a")

        arquivo.write(user+"\n")
        arquivo.write(pw+"\n")
        
        arquivo.close()
       
                

        

    

    st = tkinter.Tk()

    st.geometry("400x400")

    st.wm_title("Inscreva-se")

    partlogin = tkinter.LabelFrame(st, text="USERNAME", foreground='BLACK')

    partlogin.place(relheight=0.5, relwidth=1)

    partpass = tkinter.LabelFrame(st, text="PASSWORD", foreground='BLACK')

    partpass.place(relheight=0.5, relwidth=1, rely=0.5)

    inputlog = tkinter.Entry(partlogin, bg='grey')

    inputlog.place(relwidth=0.7, relheight=0.2, relx=0.15, rely= 0.15)

    inputp = tkinter.Entry(partpass, bg='grey')

    inputp.place(relwidth=0.7, relheight=0.2, relx=0.15, rely= 0.15)

    btnsalvar = tkinter.Button(partpass, text="Salvar", bg='grey',foreground='white', command=enviar)

    btnsalvar.place(relwidth=0.25,relheight=0.1, relx=0.60, rely=0.8)

    btnap = tkinter.Button(partpass, text="Apagar", bg='grey',foreground='white', command=ap)

    btnap.place(relwidth=0.25,relheight=0.1, relx=0.30, rely=0.8)

    st.mainloop()





frame1 = tkinter.LabelFrame( r , text = "USER", foreground='white')

frame1.place(relheight=0.5, relwidth=1)

frame1.configure(bg='black')

frame2 = tkinter.LabelFrame( r , text = "PASSWORD", foreground='white' )

frame2.place(relheight=0.5, relwidth=1, rely=0.5)

frame2.configure(bg='black')

userframe = tkinter.LabelFrame(r)

userframe.place(relheight=0.2, relwidth=1, rely=0.05)

userframe.configure(bg='black')

inputUser = tkinter.Entry(userframe, bg='grey')

inputUser.place(relwidth=0.5, relheight=0.5, relx=0.25, rely= 0.25)

passframe = tkinter.LabelFrame(r)

passframe.place(relheight=0.2, relwidth=1, rely=0.55)

passframe.configure(bg='black')

inputPass = tkinter.Entry(passframe, bg='grey')

inputPass.place(relwidth=0.5, relheight=0.5, relx= 0.25, rely=0.25)

btnEnvia = tkinter.Button(frame2, text="Login", bg ='grey',foreground='white', command=validacao)

btnEnvia.place(relwidth=0.25, relheight=0.1, relx=0.15, rely=0.6)

btnDelete = tkinter.Button(frame2, text="Apagar", bg='grey',foreground='white', command = apagar)

btnDelete.place(relwidth=0.25,relheight=0.1, relx=0.65, rely=0.6)

btnDelete = tkinter.Button(frame2, text="Inscreva-se", bg='grey',foreground='white', command = increvase)

btnDelete.place(relwidth=0.25, relheight=0.1, relx=0.65, rely=0.8)

r.mainloop()


