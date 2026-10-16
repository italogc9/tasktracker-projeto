
tarefas = []


def cadastrar_tarefa():
    print("\n--- Cadastrar tarefa ---")

    while True:
        titulo = input("Título: ").strip()
        if titulo:
            break
        print("Erro: o título é obrigatório.")

    descricao = input("Descrição: ")

    while True:
        prioridade = input("Prioridade (Alta, Média ou Baixa): ").strip().capitalize()
        if prioridade in ["Alta", "Média", "Baixa", "Media"]:
            if prioridade == "Media":
                prioridade = "Média"
            break
        print("Erro: escolha Alta, Média ou Baixa.")

    while True:
        data_limite = input("Data limite: ").strip()
        if data_limite:
            break
        print("Erro: a data limite é obrigatória.")

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }

    tarefas.append(tarefa)
    print("\nTarefa cadastrada com sucesso!")


def visualizar_tarefas():
    print("\n--- Lista de tarefas ---")

    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {numero}")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite']}")
        print(f"Status: {tarefa['status']}")


def main():
    while True:
        print("\n===== TASKTRACKER =====")
        print("1. Cadastrar tarefa")
        print("2. Visualizar tarefas")
        print("3. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            visualizar_tarefas()
        elif opcao == "3":
            print("Encerrando o TaskTracker. Até mais!")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
