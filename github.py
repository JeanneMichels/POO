import os
comando_email = "git config user.email \"20241pvai0030002@estudantes.ifpr.edu.br\""
os.system(comando_email)
comando1 = "git add *"
os.system(comando1)
mensagem = input("mensagem do commit: ")

while(len(mensagem) < 5):
    print("mensagem muito pequena, digite mais...😑")
    mensagem = input("mensagem do commit: ")
    
comando2 = f"git commit -m {mensagem}"
os.system(comando2)
comando3 = "git push"
os.system(comando3)