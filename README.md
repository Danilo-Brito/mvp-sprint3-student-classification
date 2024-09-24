<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="front/img/home_logo.jpg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Melhor Estudante - API</h3>

  <p align="center">
   Projeto MVP - Sprint: Qualidade Segurança de Sistemas Inteligentes
</div>

## Sobre o Projeto

[![Product Name Screen Shot][product-screenshot]](http://127.0.0.1:5000/openapi/swagger)

### Este projeto tem como objetivo treinar um modelo de machine learning utilizando métodos clássico para um problema de classificação. 

### Notebook contém:

 * Carga dos dados, incluindo a separação entre treino e teste (holdout)
 * Transformação de dados (normalização e padronização)
 * Modelagem (utilização dos algoritmos KNN, Árvore de Classificação, Naive Bayes e SVM)
 * Otimização de hiperparâmetros
 * Avaliação e comparação de resultados dos modelos treinados com os diferentes algoritmos
 * Exportação do modelo resultante.

  ### Link para Codelabs: 
<a href="https://colab.research.google.com/drive/1UdXAMbiadLcWbRL_Pc2e9OZkOEvVt9UK?usp=sharing" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

### Aplicação *fullstack*
* **API** (GET, DELETE, POST)
* **Front** (Adiciona/Deleta/Lista todos os alunos)


[![Product Name Screen Shot][api-bg]](http://127.0.0.1:5000/openapi/swagger)

## Como Executar

### API
1. Após clonar o reposítorio, com o VSCode abra a pasta de api e instale as dependências do projeto executando esse comando no terminal.

   ```sh
   (env)$ pip install -r requirements.txt
   ```

2. Depois de instalado as depenências, execute a sua venv
   ```sh
   python3 -m venv env
   source env/bin/activate
   ```
   
3. Execute o projeto
   ```sh
   python3 app.py
   ```
4. Abra no seu browser o link para ter acesso a doc da api
   ```
   http://127.0.0.1:5000/openapi/swagger
   ```

### Front
1. Abra a pasta front no VSCode e execute o arquivo index.html no browser.
<!-- CONTACT -->

## Contact

Danilo Brito - danilomelo.brito19@gmail.com

[product-screenshot]: front/img/bg.png
[ex]: front/img/home_logo.jpg
[api-bg]: front/img/api-bg.png
[codelabs]: https://colab.research.google.com/drive/1UdXAMbiadLcWbRL_Pc2e9OZkOEvVt9UK?usp=sharing