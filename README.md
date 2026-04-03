# Sistema Automatizado de Validação e Organização de Peças Industriais em Python

## Descrição do projeto
Este projeto foi desenvolvido para a disciplina de Algoritmos e Lógica de Programação com o objetivo de simular um sistema de automação industrial para controle de peças.

O programa permite cadastrar peças, verificar se elas estão aprovadas ou reprovadas com base em critérios definidos, armazenar automaticamente peças aprovadas em caixas com capacidade máxima de 10 unidades, remover peças cadastradas, listar caixas fechadas e gerar um relatório final.

---

## Regras de validação das peças
Uma peça será considerada **aprovada** somente se atender a todos os critérios abaixo:

- Peso entre **95 e 105**
- Cor **azul** ou **verde**
- Comprimento entre **10 e 20**

Caso não atenda a qualquer um desses critérios, a peça será classificada como **reprovada**.

---

## Funcionalidades do menu
O sistema possui um menu interativo com as seguintes opções:

1. Cadastrar nova peça  
2. Listar peças aprovadas/reprovadas  
3. Remover peça cadastrada  
4. Listar caixas fechadas  
5. Gerar relatório final  
0. Sair  

---

## Como rodar o programa

### Passo a passo
1. Instale o **Python** no computador
2. Baixe ou clone este repositório
3. Abra a pasta do projeto no terminal
4. Execute o arquivo com o comando:
   
```bash
python main.py

