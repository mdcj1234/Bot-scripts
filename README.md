# Bot scripts

Scripts utilizados para automatização de rotinas operacionais em web sites.

## Como utilizar

* Crie um diretório no seu computador e salve o código do script em um arquivo (nome arquivo).py e abra esse diretório no seu terminal.

* Para rodar um script python a primeira coisa a se fazer é baixar o python no seu computador. Acesse esse [link](https://www.python.org/) e instale a versão mais recente do python 3. Eu utilizei a versão 3.8.3. (Talvez seja necessário reabrir o terminal após a instalação)

* O projeto precisa que você instale a biblioteca do [Selenium](https://www.selenium.dev/) (caso você já não tenha). Para isso execute o seguinte comando no seu terminal:

```
$ pip install selenium
```

* Já estamos quase pronto. Agora a útima coisa que precisa é baixar um webdriver para que o Selenium possa utilizar para acessar o browser. Exitem webdrivers de praticamente todos os navegadores mais populares (Chrome, Firefox, Edge, Opera, etc...). No meu caso eu baixei o do chrome.

  * Segue o link para download do webdriver: https://chromedriver.chromium.org/downloads
  * **ATENÇÃO** o webdriver a ser baixado tem de ser compatível com a sua versão do chrome. Para saber qual é a sua versão você pode checar através das propresdades do seu chrome ou então acessando a url chrome://settings/help.
  * Depois de baixar basta apenas descompactar o webdriver dentro do mesmo diretório que você criou.

* Agora você já está pronto para executar o script. Basta executar no seu terminal (lembrando que você tem que estar na pasta que você colocou o script e o webdriver).

```
$ pyhton (nome que eu dei para o arquivo).py
```

## Autor

* **Márcio Jr** - (https://www.linkedin.com/in/marciojr1994/)
