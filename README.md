# Automatização de rotinas utilizando python

O Selenium é uma biblioteca utilizada para automatização de rotinas em web sites. Podemos aproveitar esse poderozo recurso disponível gratuitamente para criar bots que executam tarefas operacionais repetitivas.

## Como utilizar

* Crie um diretório no seu computador e salve o código do script em um arquivo (nome arquivo).py e abra esse diretório no seu terminal.

* Para rodar um script python a primeira coisa a se fazer é baixar o [Python](https://www.python.org/)  no seu computador. Instale a versão mais recente do python 3. Eu utilizei a versão 3.8.3. (Talvez seja necessário reabrir o terminal após a instalação)

* Para executar o Selenium é preciso que você instale a biblioteca do [Selenium](https://www.selenium.dev/) (caso você já não tenha). Para isso execute o seguinte comando no seu terminal:

```
$ pip install selenium
```

* Já estamos quase pronto. Agora a útima coisa que precisa é baixar um webdriver para que o Selenium possa acessar o browser. Exitem webdrivers de praticamente todos os navegadores mais populares (Chrome, Firefox, Edge, Opera, etc...). No meu caso eu baixei o do chrome.

  * Segue o link para download do webdriver: https://chromedriver.chromium.org/downloads
  * **ATENÇÃO** o webdriver a ser baixado tem de ser compatível com a sua versão do chrome. Para saber qual é a sua versão você pode checar através das propresdades do seu chrome ou então acessando a url:
    * chrome://settings/help
  * Depois de baixar basta apenas descompactar o webdriver dentro do mesmo diretório que você criou.

* Por fim você irá precisar de construir o seu arquivo de input para que o bot use as informações necessárias como Placa, Chassi e Renavam do veículo. Para isso crie um arquivo .csv chamado input.csv (Da pra alterar esse nome no código) e preencha as informações assim como o exemplo abaixo:

```csv
placa, chassi, renavam
```

  * **ATENÇÃO** se você utilizar o excel para gerar o arquivo salve o arquivo de forma que csv fique serparado por vírgulas (,) e não por ponto e vírgula (;).
  
* Agora você já está pronto para executar o script. Basta executar no seu terminal (lembrando que você tem que estar na pasta que você colocou o script e o webdriver).

```
$ pyhton (nome que eu dei para o arquivo).py
```

## Autor

* **Márcio Jr** - (https://www.linkedin.com/in/marciojr1994/)
