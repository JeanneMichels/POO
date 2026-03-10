coando_email = "git config user.email \"20241pvai0030002@estudantes.ifpr.edu.br\""
comando1 = "git add *"
mensagem = input("mensagem do commit: ")
while(len(mensagem) < 5):
    print("mensagem muito pequena, digite mais...😑")
    mensagem = input("mensagem do commit: ")
comando2 = f"git commit -m {mensagem}"
comando3 = "git push"
