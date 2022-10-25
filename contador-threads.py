#Aluno: Vinícius de Oliveira Moreira | Matrícula:497533   -   Contador de 0 a 100
import threading                                                            #Importando a biblioteca.

class nossaThread(threading.Thread):                                        #Criando uma classe nossaThread,
    def __init__(self,idt,nome):                                            #Definindo o __init__, que é a inicializacao a classe, e adicionando o id, e nome para visualizar melhor na execucao.
        threading.Thread.__init__(self)                                     #Realizando a heranca da classe pai
        self.idt = idt                                                      #Setando a variavel id da thread
        self.nome = nome                                                    #Setando a variavel nome da thread

    def run(self):                                                          #Definindo a funcao run, que é aqui que a thread vai rodar
        print('Iniciando a contagem do %s   ' % (self.nome))                
        procThread(self.nome)                                               
        print('Finalizando a contagem do %s  '  % (self.nome))              

def procThread(nome):                                                       #Definindo a funcao procThread, com o parametro nome
    cont = 0                                                                #Adicionando contador
    while (cont<100):                                                       #Adicionando while
        print('Numero %s da Thread %s  ' % (str(cont),nome))
        cont += 1

thread1 = nossaThread(1,'T1')                                               #threads independentes de acordo com a funcao da classe nossaThread
thread2 = nossaThread(2,'T2')                                               #threads independentes de acordo com a funcao da classe nossaThread

arrThread = []                                                              #Para monitorar a execucao das threads
arrThread.append(thread1)
arrThread.append(thread2)

thread1.start()                                                             #Iniciando a thread 1
thread2.start()                                                             #Iniciando a thread 2

for t in arrThread:
    t.join()                                                                #Para monitorar a execucao das threads
    
print('Fim do programa')                                                    #Fim do programa