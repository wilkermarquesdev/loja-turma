"""Classe Produto (Aula 3)."""


class Produto:
    """Um produto à venda na loja."""

    def __init__(self, nome, preco, estoque, categoria):
        # Construtor: é chamado quando fazemos Produto("Mouse", 100, 20, eletronicos)
        # Atributos PRIVADOS (dois sublinhados): só a própria classe mexe neles
        self.__nome = nome
        self.__preco = 0.0
        self.__categoria = categoria          

        self.alterar_preco(preco)    # RN1: preço maior que zero
        if estoque < 0:                    # RN2: estoque não pode ser negativo
            raise ValueError("O estoque não pode ser negativo.")
        self.__estoque = estoque

    # metodos construtores propriedades (permitem LER, mas não alterar direto)
    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @property
    def estoque(self):
        return self.__estoque

    @property
    def categoria(self):
        return self.__categoria

    # ---------- métodos (ações) ----------
    def alterar_preco(self, valor):
        """Encapsulamento: o preço só muda se for válido."""
        if valor <= 0:
            raise ValueError(f"Preço inválido para {self.__nome}: precisa ser maior que zero.")
        self.__preco = float(valor)

    def tem_estoque(self, quantidade):
        """Responde se existem pelo menos `quantidade` unidades."""
        return self.__estoque >= quantidade

    def baixar_estoque(self, quantidade):
        """Tira unidades do estoque (quando alguém compra)."""
        if not self.tem_estoque(quantidade):
            raise ValueError(
                f"Estoque insuficiente de {self.__nome}: há {self.__estoque} unidade(s)."
            )
        self.__estoque -= quantidade

    def repor_estoque(self, quantidade):
        """Devolve unidades ao estoque."""
        self.__estoque += quantidade

    def __str__(self):
        # __str__ define o que aparece quando fazemos print(produto)
        return f"{self.__nome} - R$ {self.__preco:.2f} ({self.__estoque} em estoque) [{self.__categoria}]"