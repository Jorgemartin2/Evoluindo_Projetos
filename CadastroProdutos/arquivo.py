from tkinter import *
from tkinter import ttk
import mysql.connector


tela=Tk()

class Funcs():
    def limpa_produtos(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.quant_entry.delete(0, END)
        self.values_praz_entry.delete(0, END)
        self.values_entry.delete(0, END)

    def conecta_bd(self):
        self.conn=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='produtos.bd'
        )
        self.cursor=self.conn.cursor(); print('conectando ao banco de dados')

    def desconecta_bd(self):
        self.conn.close(); print('desconectando do banco de dados')

    def monta_tabela(self):
        self.conecta_bd()
        self.cursor.execute("""
            create table if not exists produtos(
                cod int primary key,
                produto varchar(40) not null,
                quantidade int,
                valorPrazo decimal(7,2),
                valorVista decimal(7,2)                  
            );
        """)
        self.conn.commit(); print('Banco de dados criado')
        self.desconecta_bd()

    def variaveis(self):
        self.cod=self.codigo_entry.get()
        self.nome_produto=self.nome_entry.get()
        self.quantidade=self.quant_entry.get()
        self.valor_prazo=self.values_praz_entry.get()
        self.valor_vista=self.values_entry.get()

    def add_produto(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" insert into produtos (cod, produto, quantidade, valorPrazo, valorVista) 
            values (%s,%s,%s,%s,%s)""", (self.cod, self.nome_produto, self.quantidade, self.valor_prazo, self.valor_vista))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_produtos()

    def update_lista(self, lista):
        self.listaProd.delete(*self.listaProd.get_children())
        for i in lista:
            self.listaProd.insert("", END, values=i)

    def select_lista(self):
        self.conecta_bd()
        query=("""select cod, produto, quantidade, valorPrazo, valorVista from produtos
            order by produto asc;""")
        self.cursor.execute(query)
        lista=self.cursor.fetchall()
        self.update_lista(lista)

        self.desconecta_bd()

    def OnDoubleClick(self, event):
        self.limpa_produtos()
        self.listaProd.selection()

        for n in self.listaProd.selection():
            col1, col2, col3, col4, col5=self.listaProd.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.quant_entry.insert(END, col3)
            self.values_praz_entry.insert(END, col4)
            self.values_entry.insert(END, col5)

    def deleta_produto(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""delete from produtos where cod = %s """, [self.cod])
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_produtos()
        self.select_lista()

    def alterar_produto(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""update produtos set produto= %s, quantidade= %s, valorPrazo= %s, valorVista= %s where cod= %s """, (self.nome_produto, self.quantidade, self.valor_prazo, self.valor_vista, self.cod))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_produtos()

    def busca_produto(self):
        self.conecta_bd()
        self.listaProd.delete(*self.listaProd.get_children())
        self.nome_entry.insert(END,'%')
        nome=self.nome_entry.get()
        self.cursor.execute("""select cod, produto, quantidade, valorPrazo, valorVista from produtos where produto like %s order by produto asc; """, [nome])
        buscanomeProd=self.cursor.fetchall()
        for i in buscanomeProd:
            self.listaProd.insert("", END, values=i)
        self.limpa_produtos()
        self.desconecta_bd()


class Application(Funcs):
    def __init__(self):
        self.tela=tela
        self.config_tela()
        self.frames_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.monta_tabela()
        self.select_lista()
        self.menus()
        tela.mainloop()

    def config_tela(self):
        self.tela.title("Cadastro de produtos")
        self.tela.configure(background='DarkSlateGrey')
        self.tela.geometry("700x500")
        self.tela.resizable(True, True)
        self.tela.maxsize(1500, 700)
        self.tela.minsize(700, 600)

    def frames_tela(self):
        self.frame1=Frame(self.tela, bd=4, bg='white', highlightbackground='MediumSlateBlue', highlightthickness=2)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame2=Frame(self.tela, bd=4, bg='white', highlightbackground='MediumSlateBlue', highlightthickness=2)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):
        self.bot_limpar=Button(self.frame1, text="Limpar", bd=3, bg="DodgerBlue", fg='white', font=('verdana', 8, 'bold'), command=self.limpa_produtos)
        self.bot_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bot_buscar=Button(self.frame1, text="Buscar", bd=3, bg="DodgerBlue", fg='white', font=('verdana', 8, 'bold'), command=self.busca_produto)
        self.bot_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bot_novo=Button(self.frame1, text="Novo", bd=3, bg="DodgerBlue", fg='white', font=('verdana', 8, 'bold'), command=self.add_produto)
        self.bot_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bot_alterar=Button(self.frame1, text="Alterar", bd=3, bg="DodgerBlue", fg='white', font=('verdana', 8, 'bold'), command=self.alterar_produto)
        self.bot_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bot_apagar=Button(self.frame1, text="Apagar", bd=3, bg="DodgerBlue", fg='white', font=('verdana', 8, 'bold'), command=self.deleta_produto)
        self.bot_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        self.lb_codigo=Label(self.frame1, text="Código", bg='white')
        self.lb_codigo.place(relx=0.05, rely=0.05)
        self.codigo_entry=Entry(self.frame1, bg='Lightgray')
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        self.lb_nome=Label(self.frame1, text="Nome Do Produto", bg='white')
        self.lb_nome.place(relx=0.05, rely=0.35)
        self.nome_entry=Entry(self.frame1, bg='Lightgray')
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.75)

        self.lb_quant=Label(self.frame1, text="Qtde", bg='white')
        self.lb_quant.place(relx=0.05, rely=0.6)
        self.quant_entry=Entry(self.frame1, bg='Lightgray')
        self.quant_entry.place(relx=0.05, rely=0.7, relwidth=0.1)

        self.lb_values_praz=Label(self.frame1, text="Preço á prazo", bg='white')
        self.lb_values_praz.place(relx=0.25, rely=0.6)
        self.values_praz_entry=Entry(self.frame1, bg='Lightgray')
        self.values_praz_entry.place(relx=0.25, rely=0.7, relwidth=0.25)

        self.lb_values=Label(self.frame1, text="Preço á vista", bg='white')
        self.lb_values.place(relx=0.55, rely=0.6)
        self.values_entry=Entry(self.frame1, bg='Lightgray')
        self.values_entry.place(relx=0.55, rely=0.7, relwidth=0.25)
        
    def lista_frame2(self):
        self.listaProd=ttk.Treeview(self.frame2, height=3, column=("col1", "col2", "col3", "col4", "col5"))
        self.listaProd.heading("#0", text="")
        self.listaProd.heading("#1", text="Código")
        self.listaProd.heading("#2", text="Nome")
        self.listaProd.heading("#3", text="Qtde")
        self.listaProd.heading("#4", text="Preço á prazo")
        self.listaProd.heading("#5", text="Preço á vista")

        self.listaProd.column("#0", width=1)
        self.listaProd.column("#1", width=50)
        self.listaProd.column("#2", width=200)
        self.listaProd.column("#3", width=100)
        self.listaProd.column("#4", width=125)
        self.listaProd.column("#5", width=125)

        self.listaProd.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista=Scrollbar(self.frame2, orient="vertical", command=self.listaProd.yview)
        self.listaProd.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listaProd.bind("<Double-1>", self.OnDoubleClick)

    def menus(self):
        menubar=Menu(self.tela)
        self.tela.config(menu=menubar)
        filemenu=Menu(menubar)
        filemenu2=Menu(menubar)

        def quit(): self.tela.destroy()

        menubar.add_cascade(label="Opções", menu=filemenu)
        menubar.add_cascade(label="Sobre", menu=filemenu2)

        filemenu.add_command(label="Sair", command=quit)
        filemenu2.add_command(label="Limpa Produto", command=self.limpa_produtos)


Application()