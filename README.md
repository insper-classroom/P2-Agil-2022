# Prova 2 - 2022

## Projeto Ágil e Programação Eficaz - Frente de programação

**Atenção** este projeto de código vale 10.0 pontos.

É um pré-requisito para aprovação na disciplina ter tirado mais que $5.0$ em uma prova. 

A média de provas desta parte da disciplina é $MAX(P1, P2)$ de modo que este exame possa ser encarado com tranquilidade. 

## Recomendações gerais 

**Não é permitido** usar Github CoPilot ou recursos equivalentes 

Você pode consultar livremente a internet desde que **não se comunique** com outras pessoas. Nem de dentro nem de fora da sala.

**Feche o WhatsApp** e quaisquer outros recursos de comunicação individual (Outlook, Gmail, etc)

Sua tela será gravada pelo *Proctorio*, então não esqueça de manter a aba do Blackboard aberta, mesmo que em segundo plano, durante o periodo da prova

O envio é pelo repositório do Github Classroom. Faça envios frequentes (add + commit + push)

**Desligue o celular**

[**Dúvidas** deverão ser tiradas via planilha, com uma descrição clara e suficiente para a sua completa compreensão: Planilha de Dúvidas](https://docs.google.com/spreadsheets/d/1HN7NpKvvW8alXYR2SHve1H3aEHFIBEZ6_9sUhYuj6PA/edit#gid=0)


## Estrutura do projeto:

Atenção aos arquivos que precisam ser alterados. Você não vai precisar mexer em nenhum outro arquivo. 


```
├── README.md
├── doc
│   ├── Diagrama.JPG
│   └── itens.JPG
├── requirements.txt
└── src
    ├── app.py
    ├── model
    │   ├── __init__.py
    │   ├── agil_lms.db
    │   ├── db.py
    │   └── lms_models.py ** alterar **
    ├── resources
    │   ├── __init__.py
    │   └── lms_rotas.py ** alterar ** 
    └── test
        └── para_postman
            └── postman_ex_resposta_esperada.json

```


## Ambiente Virtual

Recomendamos que use um ambiente virtual para realizar a prova. Se puder deixe-o fora da pasta que contém a prova e não o envie ao Github. 

Existe um *requirements.txt* para comodidade, caso queira usar um `venv`.  De qualquer forma não usamos nenhum pacote fora do que foi testado em aula.

## Teste

Dentro da pasta `test` existe um arquivo `.json` que deverá ser carregado no Postman para que você teste as rotas, existe um exemplo de resposta da API para cada rota.

# Enunciado

Uma plataforma LMS, abreviação de *Learning Management System*, é uma plataforma de ensino que transporta o ambiente educacional para o espaço virtual.

Foi desenvolvido um protótipo com foco em sistemas com ORM, nele foram modeladas quatro classes principais **ProfessorModel**, **AlunoModel**, **EnunciadoModel** e **TarefaModel**, como mostrado no driagrama a seguir.


![Diagrama de classes da prova](https://github.com/insper-classroom/P2-Agil-2022/blob/main/doc/Diagrama.png?raw=true)


As funcionalidades e definições das classes ORM desse protótipo são simples:

- Enunciado
    - Um enunciado (*EnunciadoModel*) é uma atividade que pode ser criada única e exclusivamente por um professor, ela possui título, descrição e prazo máximo para submissão;
    - Tarefas estão sempre vinculadas a um enunciado, ou seja, alunos (*AlunoModel*) criam tarefas (*TarefaModel*) para um determinado enunciado que esteja dentro do prazo de entrega. Nota importante: uma tarefa criada é diferente de uma tarefa submetida para avaliação (mais detalhes no *bullet point* Tarefa);
    - Um professor (*ProfessorModel*) pode criar, modificar e até mesmo deletar um enunciado, desde que o mesmo tenha sido criado por ele;
- Professor
    - Um professor cria enunciados e avalia tarefas submetidas por alunos;
    - O professor pode deletar e modificar apenas enunciados que ele mesmo tenha criado;
    - O professor pode avaliar apenas tarefas que pertençam a um enunciado que ele mesmo tenha criado;
    - O professor proprietário do enunciado pode alterar o prazo de entrega;
- Aluno
    - Um aluno cria, altera e deleta uma tarefa para um determinado enunciado;
    - O aluno pode submeter a tarefa quando quiser, desde que seja proprietário da tarefa e a mesma esteja dentro do prazo de entrega permitido pelo enunciado;
- Tarefa
    - Possui resposta, estado e nota. A nota é atribuida via avaliação do professor;
    - Os estados possiveis para uma tarefa são: "aberta", "submetida", "avaliada".
        - "aberta": Qualquer tarefa criada e que ainda não foi submetida pelo aluno;
        - "submetida": Tarefa que foi submetida pelo aluno para avaliação;
        - "avaliada": Tarefa que já foi avaliada pelo professor;
    - Somente alunos criam tarefas;
    - Somente o aluno que criou a tarefa, pode submete-la;
    - Somente professores avaliam tarefas;

## Objetivo

Implemente as rotas, métodos e classes necessárias para o completo funcionamento do sistema. Segundo o último desenvolvedor a trabalhar no sistema, está faltando tudo que possui relação com "tarefas". Tanto a classe ORM TarefaModel (Model), quanto a de rota (Resource) e os métodos que estão nas classes ProfessorModel e AlunoModel que manipulam de alguma forma uma tarefa.

Existem 5 rotas no arquivo .json de teste para o Postman que estão relacionadas de alguma forma com as tarefas, são as únicas rotas que não estão funcionando e que devem ser implementadas seguindo o escopo apresentado. Na Figura abaixo temos o valor máximo para cada uma das rotas e suas funcionalidades implementadas.

![alt text](https://github.com/insper-classroom/P2-Agil-2022/blob/main/doc/itens.JPG?raw=true)

### Simplificando (TL;DR)

A aplicação foi desenvolvida utilizando a bibloiteca *Flask-Restful* e *FlaskSQLAlchemy*. A aplicação já está 85% pronta, restando apenas a implementação do que tange as tarefas dos alunos.

De uma forma bem simplista, não será necessário alterar os arquivos "src/app.py" e "src/model/db.py", e nem carregar dados no database (agil_lms.db), pois já existem.

As alterações serão realizadas nos arquivos:

- `lms_model.py`: Arquivo que contém a implementação dos ORMs das classes onde será necessario implementar na integra a classe **TarefaModel** como apresentado no diagrama. Neste mesmo arquivo deverão ser implementados as funcionalidades em vermelho mostradas no diagrama para as classes **ProfessorModel** e **AlunoModel**.
- `lms_rotas.py`: Arquivo que contém a implementação das classes de rotas (Resources) da API do Flask-Restful. Essas classes são as responsaveis por capturar uma requisão HTTP no web service, realizar a ação correpondente e então responder de forma correta. Sendo assim, é preciso ler a rota e implementar corretamente utilizando as funções `get`, `post`, `put` e `delete` na classe, sempre que necessário. No arquivo `app.py` você pode olhar quais as rotas esperadas e nome das classes que deverão implementar as rotas definidas.


### Visão geral do Fluxo

O código fonte que você esta recebendo já esta completamente funcional para criação e manipulação de Professores, Enunciados e Alunos. Você pode testar para ganhar familiaridade com a aplicação utilizando o arquivo .json do Postman que está em `test/para_postman`. Todas as rotas estão funcionando por completo e já conectadas a base de dados SQLite, com exceção das rotas que fazem parte desta avaliação.

As requisições chegarão no `app.py`, que irá procurar a classe que implementa a rota no arquivo `lms_rotas.py`, que por sua vez irá utilizar os objetos ORM das classes implementadas no arquivo `lms_models.py` para carregar e manipular os dados que estão na base, fornecendo assim, respostas adequadas para a requisição realizada.

Você possui um arquivo .json do Postman que está com todas as requisições, faça que todas as requisições (5) que envolvem tarefa funcione.


## Avaliação e Restrições

**AVISO: Somente rotas em funcionamento terão seus códigos avaliados e análisados segundo os critérios e restrições abaixo. Ou seja, rotas que não estiverem funcionando terão seus respectivos pontos zerados. Sendo assim, é preferivel que você tenha algumas funcionalidades implementadas por completo do que todas com implementações parciais.**

### Restrições

- A implementação deve ser RESTFUL e utilizando Flask-Restful;
- Deverão ser utilizadas obrigatoriamente as rotas fornecidas no arquivo do Postman e que são as mesmas também já fornecidas no "app.py";
- Tratar as rotas fornecidas fora do Flask-Restful acarretará no desconto de $2$ pontos na nota final;
- A comunicação com a base de dados deve ser realizada através do ORM como mostrado no diagrama. Comunicação direta com a base sem o uso de ORM acarretará em um desconto de 4 pontos na nota final;
- Para cada verbo HTTP e *status code* utilizado de forma errada, ou seja, em não conformidade com RestFul (maturidade 2), será descontado 0,5 ponto para cada ocorrência;
- Não verificar a autoria da tarefa antes de alterá-la, submetê-la ou deletá-la implicará em um desconto de $1.0$ ponto;
- Não verificar o prazo de entrega do enunciado ao qual a tarefa pertence antes de criá-la, submetê-la ou alterá-la, implicará em um desconto de $1.0$ ponto;
- Não verificar se a tarefa a ser avaliada por um porfessor pertence a um enunciado de sua autoria, implicara em um desconto de $1.0$ ponto;


Boa prova a todos!
