#IMPORTANDO O MÓDULO
import DataBaser
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#--- Craindo janela
janela = Tk()
janela.title("Sys Login Python")
janela.geometry("600x300") #--Tamanho da Janela em pixels
janela.resizable(width=False, height=False) #--Trava formato da janela
janela.configure(background="white")

#--- Carregando imagens
logo = PhotoImage(file="img/login.png")

#--- Frame esquerdo
LeftFrame = Frame(janela, width=200, height=300, bg="#121149", relief="raise")
LeftFrame.pack(side=LEFT)

#--- Frame da direita
RightFrame = Frame(janela, width=400, height=300, bg="#5F9EA0", relief="raise")
RightFrame.pack(side=RIGHT)

#--- Inserindo imagem
LogoLabel = Label(LeftFrame, image=logo, bg="#121149")
LogoLabel.place(x=25, y=80) #--posiciona a imagem

#--- Inserirndo textos
UserLabel = Label(RightFrame, text="Usuário",font=("Verdana",15), bg="#5F9EA0", fg="#fff")
UserLabel.place(x=60, y=50)

PassLabel = Label(RightFrame, text="Senha", font=("Verdana", 15), bg="#5F9EA0", fg="#fff")
PassLabel.place(x=60, y=120)

#--- Entrada de dados
UserEntry = ttk.Entry(RightFrame, width=35)
UserEntry.place(x=60, y=80)

PassEntry = ttk.Entry(RightFrame, width=35, show="*") #-- usa "show" para esconder os caracteres
PassEntry.place(x=60, y=150)

#--- Criando Função Registrar
def Register():
    #--- Escondendo Login e Registro
    LoginButton.place(x=1000)
    RegisterButton.place(x=1000)

    #--- Adicionando campos
    NomeLabel = Label(RightFrame, text='Nome', font=("Verdana", 15), bg="#5F9EA0", fg="#fff")
    NomeLabel.place(x=60, y=10)
    NomeEntry = ttk.Entry(RightFrame, width=35)
    NomeEntry.place(x=60, y=40)

    EmailLabel = Label(RightFrame, text="e-mail", font=("Verdana", 15), bg="#5F9EA0", fg="#fff")
    EmailLabel.place(x=60, y=70)
    EmailEntry = ttk.Entry(RightFrame, width=35)
    EmailEntry.place(x=60, y=100)

    UserLabel.place(x=60, y=130)
    UserEntry.place(x=60, y=160)
    PassLabel.place(x=60, y=190)
    PassEntry.place(x=60, y=220)

    #--- Função Salva BD
    def SalvaDataBase():
        #--- Pegar valores
        Nome = NomeEntry.get()
        Email = EmailEntry.get()
        Usuario = UserEntry.get()
        Senha = PassEntry.get()

        #--- Confirmar se campo está vazio
        if (Nome == "" and Email == "" and Usuario == "" and Senha == ""):
            messagebox.showerror(title="Register error", message="Erro de Registro!\nPreencha Todos os Campos!")
        else:
            #--- Acessa BD
            DataBaser.cur.execute("""
            SELECT * FROM User
            WHERE (Usuario = ? and Senha = ?)
            """,(Usuario, Senha))
            #--- Verificando no BD
            try:
                VerifyLogin = DataBaser.cur.fetchone()
                if (Usuario in VerifyLogin or Email in VerifyLogin):
                    messagebox.showinfo(title="Login Info", message="Usuário já está cadastrado!\nInforme usuário e e-mail diferentes!")
            except:
                DataBaser.cur.execute("""
                INSERT INTO User(Nome, Email, Usuario, Senha) VALUES(?,?,?,?)
                """, (Nome, Email, Usuario, Senha))

                #--- Salva dados no BD
                DataBaser.conn.commit()

                #--- Mensagem de SUCESSO
                messagebox.showinfo(title="Register Info", message="Registro Criado com Sucesso!")
    #--- Botão Registrar
    RegisButton = ttk.Button(RightFrame, text="Salvar", width=10, command=SalvaDataBase)
    RegisButton.place(x=100, y=260)

    #--- Cria Funcção Voltar 
    def BackLogin():
        #--- Remove intens não usasdo
        NomeEntry.place(x=1000)
        NomeLabel.place(x=1000)
        EmailEntry.place(x=1000)
        EmailLabel.place(x=1000)
        RegisButton.place(x=1000)
        BackButton.place(x=1000)

        #--- Reposiciona itens do login
        UserLabel.place(x=60, y=50)
        UserEntry.place(x=60, y=80)
        PassLabel.place(x=60, y=120)
        PassEntry.place(x=60, y=150)
        LoginButton.place(x=100, y=200)
        RegisterButton.place(x=200, y=200)

    #--- Botão Voltar
    BackButton = ttk.Button(RightFrame, text="Voltar", width=10, command=BackLogin)
    BackButton.place(x=200, y=260)



#--- Função LOGIN
def Login():
    #--- Pega dados
    Usuario = UserEntry.get()
    Senha = PassEntry.get()

    #--- Acessa BD
    DataBaser.cur.execute("""
    SELECT * FROM User
    WHERE (Usuario = ? and Senha = ?)
    """,(Usuario, Senha))

    #--- Verificando no BD
    VerifyLogin = DataBaser.cur.fetchone()
    try:
        if (Usuario in VerifyLogin and Senha in VerifyLogin):
            messagebox.showinfo(title="Login Info", message="Acesso Confirmado!\nBem Vindo!")
    except:
        messagebox.showerror(title="Login Error", message="Acesso Negado!\nUsuário não cadastrado!")

#--- Botão LOGIN
LoginButton = ttk.Button(RightFrame, text="Login", width=10, command=Login)
LoginButton.place(x=100, y=200)

#--- Botão Registro
RegisterButton = ttk.Button(RightFrame, text="Registrar", width=10, command=Register)
RegisterButton.place(x=200, y=200)


janela.mainloop()
