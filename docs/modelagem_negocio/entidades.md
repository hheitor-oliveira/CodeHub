# Modelagem de Negócio — CodeHub — 2026

## Entidades e Atributos

### Projeto
- nome
- descrição
- proprietario
- colaboradores
- cliente
- status_atual
- status_anterior

### Dev 
- nome
- especializações
- projetos
- nível/xp
- squad

### Squad
- nome
- especialização
- projetos
- integrantes
- nível/xp

### Cliente
- nome
- cnpj
- projeto

### Status
- nome
- descrição

### Especializações
- tecnologia
- nível

### XP
- experiência
- nível atual 
- dev

## Regras de Negócio

* Um Dev só pode participar de um Squad.
* Um Cliente só pode ter um Projeto ativo por vez.
* Um Squad só pode ter uma Especialização.

## Relacionamentos

### Projeto

- Um Projeto só pode **ser** de um único Cliente.
- Um Projeto pode **ter** vários Dev's.
- Um Projeto pode **ter** vários Squad's envolvidos.
- Um Projeto só pode **assumir** um Status.

### Dev

- Um Dev só pode **participar** de um Squad.
- Um Dev pode **ter** várias Especializações.
- Um Dev pode **participar** de vários Projetos simultaneamente.
- Um Dev 
