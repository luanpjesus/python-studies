import random
 
class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
        
        
        
    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNivel: {self.get_nivel()}"
    
    def receber_dano(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0
    
    
    def ataque(self, alvo):
        dano =  random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        alvo.receber_dano(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou  {dano} de dano!")
    
    
            
    
    
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
        
    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}"    
    
    def ataque_especial(self, alvo):
        dano =  random.randint(self.get_nivel() * 5, self.get_nivel() * 8) #Dano aumentado
        
        alvo.receber_dano(dano)
        print(f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em alvo {self.get_nome()} e causou {dano} de dano!")
    
    
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
        
        
    def get_tipo(self):
        return self.__tipo            
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}"
        



class Jogo:
    
    
    def __init__(self) -> None:
        self.heroi = Heroi(nome="Heroi", vida=100, nivel=5 ,habilidade= "Super-forca")            
        self.inimigo = Inimigo(nome="Morcego", vida=50, nivel=3, tipo="Voador")
        
    def iniciar_batalha(self):
        print("Iniciando a batalha")
        
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("detalhes do personagem:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())
            
            
            input("Pressionme Enter para atacar...")
            escolha = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial: )")
            
            if escolha == "1":
                self.heroi.ataque(self.inimigo)
            elif escolha == "2":
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha invalida, escolha novamente!")    
            
            if self.inimigo.get_vida() > 0:
                self.inimigo.ataque(self.heroi)
                
        if self.heroi.get_vida() > 0 :
            print("Parabens vc venceu a batalha")
        else:
            print("Voce foi derrotado!")        
            
# Criar instancia do jogo e iniciar batalha

jogo = Jogo()
jogo.iniciar_batalha()                                       


heroi = Heroi(nome="Luan", vida=100, nivel=5, habilidade="Super-forca")
print(heroi.exibir_detalhes())            



inimigo = Inimigo(nome="Batman", vida=100,nivel=4, tipo="Voador") 

print(inimigo.exibir_detalhes())