class Televisao:

    def __init__(self, canal, volume, isMudo):
        self.canal = canal
        self.volume = volume
        self.isMudo = isMudo

    def alterar_canal(self):
        print("Alterando canal...")
        self.canal += 1

    def alterar_volume(self):
        # Ao tentar alterar o volume quando a televisão estiver muda o comportamento é desligado
        if self.isMudo:
            print("Não está mais mudo")
            self.isMudo = False

        print("Alterando volume...")
        self.volume += 1
        
    
    def colocar_mudo(self):
        if self.isMudo:
             print("Televisão já está muda")
        else:      
            print("Televisão muda")
            self.isMudo = True