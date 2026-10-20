requisicao = {
    "docente_ativo": True,
    "hora_atual": 4,
    "nicho_ocupado": False,
    "chave_solicitada": "Lab 01",
}

if not requisicao["docente_ativo"]:
    print("Acesso Negado: Cadastro Inativo.")
elif requisicao["hora_atual"] >= 23 or requisicao["hora_atual"] < 5:
    print("Acesso Negado: Trava Noturna  (indisponivel entre 23:00 e 05:00).")
elif requisicao["nicho_ocupado"]:
    print("Acesso Negado: Chave Indisponivel.")
else:
    print(f"Acesso Concedido: Chave do {requisicao['chave_solicitada']} Liberada.")


def validar_acesso(id_cracha: str, horario: int) -> dict:
    """Função que valida o acesso do colaborador ao armário de chave
    Args:
    id_cracha (str): id do crachá do colaborador.
    horario(int): horario da retirada ou devolução.
    returns:
    dict: Dicionario com o resultado da validação."""

    colaborador_senai = colaboradores.get(id_cracha)
