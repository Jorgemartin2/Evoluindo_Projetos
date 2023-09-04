from módulos import *

class Validate():
    def api_city(self):
        try:
            cep=self.entry_cep.get()
            link=f"https://viacep.com.br/ws/{cep}/json/"
            request=requests.get(link)
            dic_request=request.json()
            self.entry_city.insert(END, dic_request['localidade'])
            self.entry_uf.insert(END, dic_request['uf'])
        except:
            return CTkMessagebox(title="ERRO", message="Cep não encontrado", icon="cancel", option_1="Fechar")
    
    def validate_birth(self):
        try:
            date=self.entry_birth.get()
            datetime.strptime(date, "%d/%m/%Y")
            return True
        except:
            return False
            
    def validate_entry_telephone(self, text):
        if text=="":
            return True
        try:
            value=int(text)
        except ValueError:
            return False
        return 0 <= value <= 100000000

    def validate_entry_cel(self, text):
        if text=="":
            return True
        try:
            value=int(text)
        except ValueError:
            return False
        return 0 <= value <= 100000000000