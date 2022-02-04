import tkinter


def addComent():
    coment = inputComent.get()
    comentsList.insert(0, coment)
    inputComent.delete(0, tkinter.END)

def delcoment():
    comentsList.delete(comentsList.curselection()[0])

root = tkinter.Tk()
root.geometry("400x400+300+300")
root.wm_title("Meu programa")


comentsFrame = tkinter.LabelFrame(root, text="Comentarios")
comentsFrame.place(relwidth=1,relheight=0.5)
comentsList = tkinter.Listbox(comentsFrame)
comentsList.place(relwidth=1, relheight=1)

optionsFrame = tkinter.LabelFrame(root, text="Opções")
optionsFrame.place(relwidth=1, relheight=0.5, rely=0.5)

inputComentFrame = tkinter.LabelFrame(optionsFrame, text="Novo comentário")
inputComentFrame.place(relheight=0.4,relwidth=1)

inputComent = tkinter.Entry(inputComentFrame)
inputComent.place(relwidth=0.75, relheight=1)

btnComent = tkinter.Button(inputComentFrame, text="Enviar", command=addComent)
btnComent.place(relwidth=0.25, relheight=1, relx=0.75)

btnDelete = tkinter.Button(optionsFrame, text="Remover", command=delcoment)
btnDelete.place(relwidth=0.5,relheight=0.2, relx=0.25, rely=0.6)

root.mainloop()
