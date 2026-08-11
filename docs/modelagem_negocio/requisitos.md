# Modelagem de Negócio — CodeHub — 2026

## Requisitos Funcionais

* O sistema deve permitir o **cadastro de empresas**, que servirão como base para organizar as demais informações do sistema.

*
  **Exemplo:**
  `Empresa → Usuários → Grupos → Projetos`

* O sistema deve permitir o **cadastro e gerenciamento de projetos**, sem armazenar diretamente os arquivos dos projetos.

* O sistema deve permitir o **cadastro de desenvolvedores e demais usuários**.

* O sistema deve permitir a **organização dos usuários em grupos**, de acordo com suas áreas de atuação ou especialização.

  **Exemplo:**
  `Front-end`, `Back-end`, `Banco de Dados`, entre outros.

* O sistema deve permitir que a empresa **defina como serão aplicadas as permissões de acesso**, podendo utilizar cargos ou outras formas de organização.

* O sistema deve permitir o **cadastro de clientes** relacionados aos projetos.

* O sistema deve permitir o **cadastro e gerenciamento de tarefas**, que poderão ser atribuídas aos desenvolvedores.

* O sistema deve possuir um **chat interno** para comunicação entre os usuários.

* O sistema deve possuir um **sistema de níveis e recompensas**, baseado na conclusão de tarefas e demais atividades realizadas pelos usuários.

* O sistema deve permitir o **registro e acompanhamento do andamento dos projetos**.

* Necessário ter sistema de cadastro e login.

## Requisitos Não Funcionais

* S.G.B.D (Sistema Gerenciador de Banco de Dados) utilizado: PostgreSQL v18.x para utilização em nuvem;

* Interface Gráfica: Aplicação Web;

* Sistema baseado em Ortogonalidade: Módulos Independentes;

* Auditoria: Ações consideradas importantes devem ser registradas;

* Segurança: Permissões do sistema devem ser baseadas no usuário;
