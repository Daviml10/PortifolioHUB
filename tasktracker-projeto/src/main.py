def ler_titulo():
    """Solicita um titulo ate que o usuario informe um valor valido."""
    while True:
        titulo = input("Titulo da tarefa: ").strip()
        if titulo:
            return titulo
        print("Erro: o titulo nao pode ficar vazio. Tente novamente.")


def ler_prioridade():
    """Aceita somente Alta, Media/Media ou Baixa."""
    prioridades = {
        "alta": "Alta",
        "media": "Media",
        "media": "Media",
        "baixa": "Baixa",
    }

    while True:
        prioridade = input("Prioridade (Alta, Media ou Baixa): ").strip().lower()
        if prioridade in prioridades:
            return prioridades[prioridade]
        print("Erro: prioridade invalida. Escolha Alta, Media ou Baixa.")


def cadastrar_tarefa(tarefas):
    """Le os dados e adiciona uma tarefa a lista."""
    print("\n--- Cadastro de tarefa ---")
    titulo = ler_titulo()
    descricao = input("Descricao da tarefa: ").strip()
    prioridade = ler_prioridade()
    data_limite = input("Data limite (ex.: DD/MM/AAAA): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite if data_limite else "Nao informada",
        "status": "Pendente",
    }

    tarefas.append(tarefa)
    print("\nTarefa cadastrada com sucesso!")


def visualizar_tarefas(tarefas):
    """Exibe todas as tarefas cadastradas."""
    print("\n--- Tarefas cadastradas ---")
    if not tarefas:
        print("Ainda nao existem tarefas cadastradas.")
        return

    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {indice}")
        print(f"Titulo: {tarefa['titulo']}")
        print(f"Descricao: {tarefa['descricao'] or 'Nao informada'}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite']}")
        print(f"Status: {tarefa['status']}")


def exibir_menu():
    print("\n========== TASKTRACKER ==========")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair")


def main():
    tarefas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao (1-3): ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            print("Obrigado por usar o TaskTracker. Ate mais!")
            break
        else:
            print("Opcao invalida. Digite 1, 2 ou 3.")


if __name__ == "__main__":
    main()
