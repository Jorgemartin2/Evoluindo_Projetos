from módulos import *
from validates import Validate

class Functions():    
    def delete_entry(self):
        self.entry_id.delete(0, END)
        self.entry_name.delete(0, END)
        self.entry_birth.delete(0, END)
        self.entry_telephone.delete(0, END)
        self.entry_email.delete(0, END)
        self.entry_cel.delete(0, END)
        self.entry_address.delete(0, END)
        self.entry_number.delete(0, END)
        self.entry_cep.delete(0, END)
        self.entry_city.delete(0, END)
        self.entry_uf.delete(0, END)
        self.entry_complement.delete(0, END)
        self.entry_obs.delete(0, END)
    
    def conect_db(self):
        self.conn=sqlite3.connect('sistema.db')
        self.cursor=self.conn.cursor()

    def desconect_db(self):
        self.conn.close()

    def create_table(self):
        self.conect_db()
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(45) NOT NULL,
                birth DATE NOT NULL,
                telephone BIGINT(14) NOT NULL,
                cel BIGINT(14) NOT NULL,
                email VARCHAR(100) NULL DEFAULT 'Sem email',
                address VARCHAR(100) NOT NULL,
                number VARCHAR(10) NOT NULL,
                cep INT(8) NOT NULL,
                city VARCHAR(30) NOT NULL,
                uf CHAR(2) NOT NULL,
                complement VARCHAR(10) NOT NULL,
                obs TEXT(100) NULL DEFAULT 'Sem descrição'
            );
        """)
        self.conn.commit()
        self.desconect_db()

    def variables(self):
        self.name1=self.entry_name.get().title()
        self.birth1=self.entry_birth.get()
        self.telephone1=self.entry_telephone.get()
        self.cel1=self.entry_cel.get()
        self.email1=self.entry_email.get()
        self.address1=self.entry_address.get().title()
        self.number1=self.entry_number.get()
        self.cep1=self.entry_cep.get()
        self.city1=self.entry_city.get().title()
        self.uf1=self.entry_uf.get().upper()
        self.complement1=self.entry_complement.get().title()
        self.obs1=self.entry_obs.get().capitalize()
             
    def add_customers(self):
        self.variables()
        if self.validate_birth()==False:
            CTkMessagebox(title="ERRO", message="Data inválida, insira no formato (dd/mm/aaaa)", icon="cancel", option_1="Fechar")
        elif self.name1 == "":
            CTkMessagebox(title='ERRO', message='Preencha os campos obrigatórios')
        elif self.birth1 == "":
            CTkMessagebox(title='ERRO', message='Preencha os campos obrigatórios')
        elif self.cel1 == "":
            CTkMessagebox(title='ERRO', message='Preencha os campos obrigatórios')
        elif self.address1 == "":
            CTkMessagebox(title='ERRO', message='Preencha os campos obrigatórios')
        elif self.number1 == "":
            CTkMessagebox(title='ERRO', message='Preencha os campos obrigatórios')
        elif self.cep1 == "":
            CTkMessagebox(title='ERRO', message='Preencha os campos obrigatórios')
        elif self.city1 == "":
            CTkMessagebox(title='ERRO', message='Preencha os campos obrigatórios')
        elif self.uf1 == "":
            CTkMessagebox(title='ERRO', message='Preencha os campos obrigatórios')
        else:
            self.conect_db()
            self.cursor.execute("""INSERT INTO clientes(name, birth, telephone, cel, email, address, number, cep, city, uf, complement, obs) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", (self.name1, self.birth1, self.telephone1, self.cel1, self.email1, self.address1, self.number1, self.cep1, self.city1, self.uf1, self.complement1, self.obs1))
            self.conn.commit(); CTkMessagebox(title="SUCESSO", message="Cliente cadastrado com sucesso!", icon="check", option_1="Ok")
            self.desconect_db()
            self.delete_entry()

    def select_customers(self):
        self.conect_db()
        self.list_customers.delete(*self.list_customers.get_children())
        vquery="""SELECT id, name, birth, telephone, cel, email, address, number, cep, city, uf, complement, obs FROM clientes ORDER BY name ASC;"""
        self.cursor.execute(vquery)
        lista=self.cursor.fetchall()
        for i in lista:
            self.list_customers.insert("", END, values=i)
        self.desconect_db()

    def delete_customers(self):
        self.variables()
        self.conect_db()
        id_customers=self.entry_customers.get()
        self.cursor.execute("""DELETE FROM clientes WHERE id=?""", [id_customers])
        self.yesno=CTkMessagebox(title="CUIDADO", message="Deseja realmente apagar esse registro?", icon="warning", option_1="Não", option_2="Sim")
        if self.yesno.get()=="Sim":
            self.conn.commit()
        self.desconect_db()
        self.entry_customers.delete(0, END)
        self.select_customers()

    def update_customers(self):
        self.variables()
        self.id1=self.entry_id.get()
        self.conect_db()
        self.cursor.execute("""UPDATE clientes SET name=?, birth=?, telephone=?, cel=?, email=?, address=?, number=?, cep=?, city=?, uf=?, complement=?, obs=? WHERE id=?""",(self.name1, self.birth1, self.telephone1, self.cel1, self.email1, self.address1, self.number1, self.cep1, self.city1, self.uf1, self.complement1, self.obs1, self.id1))
        self.conn.commit(); CTkMessagebox(title="INFO",message="Dados alterados com sucesso!", icon="check", option_1="Ok")
        self.desconect_db()
        self.delete_entry()

    def OnDoubleClick(self, event):
        self.delete_entry()
        self.list_customers.selection()

        for n in self.list_customers.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13=self.list_customers.item(n, 'values')
            self.entry_id.insert(END, col1)
            self.entry_name.insert(END, col2)
            self.entry_birth.insert(END, col3)
            self.entry_telephone.insert(END, col4)
            self.entry_cel.insert(END, col5)
            self.entry_email.insert(END, col6)
            self.entry_address.insert(END, col7)
            self.entry_number.insert(END, col8)
            self.entry_cep.insert(END, col9)
            self.entry_city.insert(END, col10)
            self.entry_uf.insert(END, col11)
            self.entry_complement.insert(END, col12)
            self.entry_obs.insert(END, col13)

        self.newroot.destroy()

    def get_customers(self):
        self.conect_db()
        self.list_customers.delete(*self.list_customers.get_children())
        self.entry_customers.insert(END, '%')
        name=self.entry_customers.get()
        self.cursor.execute("""SELECT id, name, birth, telephone, cel, email, address, number, cep, city, uf, complement, obs FROM clientes WHERE name LIKE '%s' ORDER BY name ASC; """%name)
        get_customers=self.cursor.fetchall()
        for i in get_customers:
            self.list_customers.insert("", END, values=i)
        self.entry_customers.delete(0, END)
        self.desconect_db()