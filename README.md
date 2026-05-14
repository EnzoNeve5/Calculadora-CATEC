# Documento de Especificação de Produto (PRD): Calculadora Desktop Python

---

## 1. Visão Geral do Produto
A **Calculadora Desktop** é uma aplicação de interface gráfica (GUI) desenvolvida em Python utilizando a biblioteca **Tkinter**. O produto visa oferecer uma ferramenta de cálculo rápido para o sistema operacional, replicando as funcionalidades e a estética de calculadoras padrão, com foco em clareza visual e facilidade de uso.

## 2. Objetivos e Público-Alvo
* **Objetivo:** Fornecer uma ferramenta de cálculo aritmética básica e avançada (como raiz quadrada) para uso em ambiente desktop.
* **Público-Alvo:** Estudantes, profissionais e usuários casuais que necessitam de uma calculadora rápida que não dependa de conexão com a internet.

---

## 3. Requisitos Funcionais

### 3.1 Operações Aritméticas
O sistema deve processar e exibir os resultados das seguintes operações:
* **Operações Básicas:** Soma (`+`), Subtração (`-`), Multiplicação (`×`) e Divisão (`÷`).
* **Operações Avançadas:** Cálculo de Raiz Quadrada (`√x`) e Elevação ao Quadrado (`x²`).

### 3.2 Interface e Controles
* **Display Duplo:** O visor deve exibir a expressão total acumulada (em uma fonte menor) e o número atual sendo digitado (em destaque).
* **Limpeza de Dados:** * Botão `C`: Limpa a entrada atual.
    * Botão `Clear`: Limpa todo o histórico e a operação em curso.
* **Entrada de Decimais:** Suporte a números flutuantes através do botão de ponto (`.`).

---

## 4. Especificações Técnicas

### 4.1 Stack Tecnológica
* **Linguagem:** Python 3.x.
* **Biblioteca de GUI:** `tkinter` (nativa do Python).
* **Processamento Matemático:** Uso da função `eval()` do Python para avaliação de strings numéricas.

### 4.2 Componentes da Interface
* **Display Frame:** Área superior contendo dois labels (`total_label` e `label`) com cores de fundo específicas (#F5F5F5) para contraste.
* **Buttons Frame:** Grade (Grid) organizada para alinhamento simétrico dos dígitos e operadores.
* **Estilização:** * Botões numéricos em branco.
    * Operadores em cinza.
    * Botão de igualdade (`=`) destacado em laranja.

---

## 5. Experiência do Usuário (UX)
* **Responsividade Visual:** Os botões devem ocupar todo o espaço disponível no frame (`sticky=tk.NSEW`) para garantir uma área de clique otimizada.
* **Feedback de Erro:** Caso o usuário realize uma operação inválida (ex: divisão por zero), o display deve exibir a mensagem "Error" sem travar a aplicação.
* **Layout Fixo:** A janela possui tamanho fixo (400x500) para manter a integridade visual da grade de botões.

---

## 6. Roadmap de Melhorias
* [ ] **Histórico de Cálculos:** Adicionar uma aba lateral para visualizar as últimas operações realizadas.
* [ ] **Teclas de Atalho:** Mapear o teclado físico para aceitar comandos numéricos e operadores.
* [ ] **Modo Científico:** Inclusão de funções trigonométricas e logarítmicas.

---

## 7. Instruções de Execução
Para executar a aplicação, certifique-se de ter o Python instalado e rode:
```bash
python calculadora.py
