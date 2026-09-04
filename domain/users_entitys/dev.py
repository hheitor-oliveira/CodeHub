# importei uma classe para representar o relacionamento entre elas
from domain.users_entitys.stack import Stack

# aqui criei a classe Dev
class Dev():
    
    def __init__(self,
                 name: str,
                 stack: Stack,
                 project: str,
                 level: int,
                 squad: str,
                 id: int | None = None) -> None: #defini o tipo dos atributos e o tipo de retorno da classe
            
        # aqui utilizei o "_" para tornar os atributos protegido e caso queira tornar privado posso utilizar "__"
        
        self._name = name
        self._stack = stack
        self._project = project
        self._level = level
        self._squad = squad
        self._id = id
     
    # é um getter uma forma de leitura segura do atributo da minha classe, utilizando property
    # tambem posso adicionar uma logica dentro desse metodo   
    @property
    def name(self) -> str:
        return self._name
    
    # isso é um setter é um metodo que criei que tem a funcao de alterar a informação de um atributo de um objeto
    # tambem posso aplicar logica
    def change_name(self,
                    name: str) -> None:
        self._name = name
        