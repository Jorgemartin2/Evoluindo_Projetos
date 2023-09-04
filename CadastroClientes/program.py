from módulos import *
from functions import Functions
from validates import Validate
from reports import Reports

root=ctk.CTk()

class App(Functions, Validate, Reports):
    def __init__(self):
        self.root=root
        self.config_root()
        self.add_image()
        self.appearence()
        self.frame_root()
        self.validate_entry()
        self.widgets_root()
        self.create_table()
        self.menus()
        root.mainloop()
        

    def config_root(self):
        self.root.title("Cadastro de Clientes")
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        self.root.minsize(1000, 600)

    def appearence(self):
        self.label_apm=ctk.CTkLabel(self.root, text="Tema", bg_color="transparent", text_color=['#000', '#fff'])
        self.label_apm.place(x=30, y=440)
        self.opt_apm=ctk.CTkOptionMenu(self.root, values=["Light", "Dark", "System"], width=80, command=self.change_apm)
        self.opt_apm.place(x=30, y=470)

    def change_apm(self, new_appearence):
        ctk.set_appearance_mode(new_appearence)

    def frame_root(self):
        self.frame=ctk.CTkFrame(self.root, width=1500, height=50, corner_radius=0, bg_color='#00008B', fg_color='#00008B').place(x=0, y=10)

    def add_image(self):
        current_path=os.path.dirname(os.path.realpath(__file__))
        self.bg_image=ctk.CTkImage(Image.open(current_path+"/fog.png"), size=(300, 500))
        self.label_bg_image=ctk.CTkLabel(self.root, text=None, image=self.bg_image).place(x=700, y=70)

    def widgets_root(self):
        self.entry_id=ctk.CTkEntry(self.root, width=50, font=("Century Gothic bold", 16), border_color="#aaa",border_width=2, fg_color="transparent", placeholder_text="ID")
        self.entry_id.place(x=610, y=70)

        self.label_title=ctk.CTkLabel(self.frame, text="Sistema de Gestão de Clientes", font=("Century Gothic bold", 24), text_color="#FFFFFF", bg_color="#00008B").pack(expand=False, pady=22)

        self.label_span=ctk.CTkLabel(self.root, text="Por favor, preencha todos os campos obrigatórios!", font=("Century Gothic bold", 16), text_color="#FF0000", bg_color="transparent").place(x=30, y=70)

        self.label_name=ctk.CTkLabel(self.root, text="Nome Completo*", font=("Century Gothic bold", 16), bg_color="transparent").place(x=30, y=110)
        self.entry_name=ctk.CTkEntry(self.root, width=315, font=("Century Gothic bold", 16), border_color="#aaa",border_width=2, fg_color="transparent")
        self.entry_name.place(x=30, y=140)

        self.label_birth=ctk.CTkLabel(self.root, text="Data de Nascimento*", font=("Century Gothic bold", 16), bg_color="transparent").place(x=360, y=110)
        self.entry_birth=ctk.CTkEntry(self.root, width=300, font=("Century Gothic bold", 16), border_color="#aaa",border_width=2, fg_color="transparent")
        self.entry_birth.place(x=360, y=140)

        self.label_telephone=ctk.CTkLabel(self.root, text="Telefone", font=("Century Gothic bold", 16), bg_color="transparent").place(x=30, y=180)
        self.entry_telephone=ctk.CTkEntry(self.root, width=200, font=("Century Gothic bold", 16), border_color="#aaa",border_width=2, fg_color="transparent", validate="key", validatecommand=self.validate_telephone)
        self.entry_telephone.place(x=30, y=210)

        self.label_cel=ctk.CTkLabel(self.root, text="Celular*", font=("Century Gothic bold", 16), bg_color="transparent").place(x=245, y=180)
        self.entry_cel=ctk.CTkEntry(self.root, width=200, font=("Century Gothic bold", 16), border_color="#aaa",border_width=2, fg_color="transparent", validate="key", validatecommand=self.validate_cel)
        self.entry_cel.place(x=245, y=210)

        self.label_email=ctk.CTkLabel(self.root, text="Email", font=("Century Gothic bold", 16), bg_color="transparent").place(x=460, y=180)
        self.entry_email=ctk.CTkEntry(self.root, width=200, font=("Century Gothic bold", 16), border_color="#aaa",border_width=2,fg_color="transparent")
        self.entry_email.place(x=460, y=210)

        self.label_address=ctk.CTkLabel(self.root, text="Logradouro*", font=("Century Gothic bold", 16), bg_color="transparent").place(x=30, y=250)
        self.entry_address=ctk.CTkEntry(self.root, width=415, font=("Century Gothic bold", 16), border_color="#aaa",border_width=2, fg_color="transparent")
        self.entry_address.place(x=30, y=280)

        self.label_number=ctk.CTkLabel(self.root, text="Número*", font=("Century Gothic bold", 16), bg_color="transparent").place(x=460, y=250)
        self.entry_number=ctk.CTkEntry(self.root, width=200, font=("Century Gothic bold", 16), border_color="#aaa",border_width=2, fg_color="transparent")
        self.entry_number.place(x=460, y=280)

        self.label_cep=ctk.CTkLabel(self.root, text="CEP*", font=("Century Gothic bold", 16), bg_color="transparent").place(x=30, y=320)
        self.entry_cep=ctk.CTkEntry(self.root, width=130, font=("Century Gothic bold", 16), border_color="#aaa",border_width=2, fg_color="transparent")
        self.entry_cep.place(x=30, y=350)
        
        self.label_city=ctk.CTkLabel(self.root, text="Cidade*", font=("Century Gothic bold", 16), bg_color="transparent").place(x=260, y=320)
        self.entry_city=ctk.CTkEntry(self.root, width=200, font=("Century Gothic bold", 16), border_color="#aaa",border_width=2, fg_color="transparent")
        self.entry_city.place(x=260, y=350)

        self.label_uf=ctk.CTkLabel(self.root, text="UF*", font=("Century Gothic bold", 16), bg_color="transparent"). place(x=470, y=320)
        self.entry_uf=ctk.CTkEntry(self.root, width=50, font=("Century Gothic bold", 16), border_color="#aaa",border_width=2, fg_color="transparent")
        self.entry_uf.place(x=470, y=350)

        self.label_complement=ctk.CTkLabel(self.root, text="Complemento", font=("Century Gothic bold", 16), bg_color="transparent").place(x=530, y=320)
        self.entry_complement=ctk.CTkEntry(self.root, width=130, font=("Century Gothic bold", 16), border_color="#aaa",border_width=2, fg_color="transparent")
        self.entry_complement.place(x=530, y=350)

        self.label_obs=ctk.CTkLabel(self.root, text="Observação", font=("Century Gothic bold", 16), bg_color="transparent").place(x=30, y=400)
        self.entry_obs=ctk.CTkEntry(self.root, width=530, height=100, font=("Century Gothic bold", 16), border_color="#aaa",border_width=2, fg_color="transparent")
        self.entry_obs.place(x=130, y=400)

        self.button_cep=ctk.CTkButton(self.root, width=80, text="BUSCAR", fg_color="#4B0082", hover_color="#4B0082", command=self.api_city).place(x=170, y=350)

        self.button_update=ctk.CTkButton(self.root, text="ATUALIZAR", fg_color="#808080", hover_color="#696969", command=self.update_customers).place(x=35, y=530)

        self.button_read=ctk.CTkButton(self.root, text="CONSULTAR", fg_color="#0000FF", hover_color="#0000CD",command=self.new_root).place(x=195, y=530)

        self.button_creat=ctk.CTkButton(self.root, text="CADASTRAR", fg_color="#008000", hover_color="#006400", command=self.add_customers).place(x=355, y=530)

        self.button_delete_entry=ctk.CTkButton(self.root, text="LIMPAR DADOS", fg_color="#FF0000", hover_color="#8B0000", command=self.delete_entry).place(x=515, y=530)

    def new_root(self):
        self.newroot=ctk.CTkToplevel()
        self.newroot.title("Clientes")
        self.newroot.transient()
        self.newroot.geometry("1000x600")
        self.newroot.minsize(1000,600)
        self.newroot.focus_force()
        self.newroot.grab_set()

        self.button_delete=ctk.CTkButton(master=self.newroot, text="DELETAR",fg_color="#FF0000", hover_color="#8B0000", command=self.delete_customers).place(x=500, y=30)
        self.button_get=ctk.CTkButton(master=self.newroot, text="BUSCAR",fg_color="#0000CD", hover_color="#000080", command=self.get_customers).place(x=350, y=30)

        self.entry_customers=ctk.CTkEntry(self.newroot, width=300, font=("Century Gothic bold", 16), border_color="#aaa",border_width=2, fg_color="transparent",text_color="#000000", placeholder_text="Digite o id ou o nome", placeholder_text_color="#A9A9A9")
        self.entry_customers.place(x=30, y=30)
    
        self.list_customers=ttk.Treeview(master=self.newroot, height=3, column=("col1", "col2", "col3", "col4", "col5","col6", "col7", "col8", "col9", "col10", "col11", "col12", "col13"))
        self.list_customers.heading("#0", text="")
        self.list_customers.heading("#1", text="ID")
        self.list_customers.heading("#2", text="NOME")
        self.list_customers.heading("#3", text="DATA")
        self.list_customers.heading("#4", text="TELEFONE")
        self.list_customers.heading("#5", text="CELULAR")
        self.list_customers.heading("#6", text="EMAIL")
        self.list_customers.heading("#7", text="LOGRADOURO")
        self.list_customers.heading("#8", text="NÚMERO")
        self.list_customers.heading("#9", text="CEP")
        self.list_customers.heading("#10", text="CIDADE")
        self.list_customers.heading("#11", text="UF")
        self.list_customers.heading("#12", text="COMPLEMENTO")
        self.list_customers.heading("#13", text="OBS")

        self.list_customers.column("#0", width=1)
        self.list_customers.column("#1", width=10)
        self.list_customers.column("#2", width=50)
        self.list_customers.column("#3", width=50)
        self.list_customers.column("#4", width=50)
        self.list_customers.column("#5", width=50)
        self.list_customers.column("#6", width=50)
        self.list_customers.column("#7", width=50)
        self.list_customers.column("#8", width=50)
        self.list_customers.column("#9", width=50)
        self.list_customers.column("#10", width=50)
        self.list_customers.column("#11", width=50)
        self.list_customers.column("#12", width=50)
        self.list_customers.column("#13", width=50)

        self.list_customers.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.85)
        self.select_customers()
        self.list_customers.bind("<Double-1>", self.OnDoubleClick)

    def validate_entry(self):
        self.validate_telephone=(self.root.register(self.validate_entry_telephone), "%P")
        self.validate_cel=(self.root.register(self.validate_entry_cel), "%P")

    def menus(self):
        menubar=Menu(self.root)
        self.root.config(menu=menubar)
        filemenu=Menu(menubar)
        filemenu2=Menu(menubar)

        def quit(): self.root.destroy()

        menubar.add_cascade(label="Opções", menu=filemenu)
        menubar.add_cascade(label="Relatório", menu=filemenu2)

        filemenu.add_command(label="Sair", command=quit)
        filemenu2.add_command(label="Gerar ficha do cliente", command=self.generate_reports)

App()