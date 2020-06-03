from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import csv
import os
import json

if __name__ == '__main__':
    veiculos = carregarDadosCSV()
    multas = minerarMultasDetranMG(veiculos)
    salvarDadosCSV(multas)

# Manipulação CSV 
def carregarDadosCSV():
    dados = []
    diretorio = os.path.dirname(os.path.abspath(__file__))
    with open(diretorio + '/input.csv') as file:
        csvReader = csv.reader(file)
        for dado in csvReader:
               dados.append(dado)
    return dados

def salvarDadosCSV(dados):
    with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter = ';', lineterminator = '\n')
        writer.writerow(['placa', 'sequencia', 'processo', 'descricao', 'local', 'valor', 'url'])
        for dadojson in dados:
            dado = json.loads(dadojson)
            writer.writerow([dado['placa'], dado['sequencia'], dado['processo'], dado['descricao'], dado['local'], dado['valor'], dado['url']])
        
# Funções do bot
def minerarMultasDetranMG(veiculos):
    driver = webdriver.Chrome()
    multas = []
    for veiculo in veiculos:
        multas += obterMultas(driver, veiculo)
    return multas
        
def obterMultas(driver, veiculo):
    multas = []
    driver.get("https://www.detran.mg.gov.br/veiculos/situacao-do-veiculo/emissao-de-boleto-de-multas/")
    driver.find_element_by_id("EmitirExtratoMultaPlaca").send_keys(veiculo[0])
    driver.find_element_by_id("EmitirExtratoMultaRenavam").send_keys(veiculo[2])
    driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div/div[1]/div[2]/form/div[2]/div[3]/button")[0].click()
    elem = driver.find_elements_by_id("flashMessage")

    if  len(elem) == 0:
        urls = []
        elements = driver.find_elements_by_xpath("//*[@id='conteudo']/div[2]/div/div/div/div/table/tbody/tr/td[1]/a")
        for element in elements:
            urls.append(element.get_attribute('href'))
        for url in urls:
            multas += minerarMultasEncontradas(driver,url,veiculo[0])
    return multas
            
def minerarMultasEncontradas(driver,url,placa):
    driver.get(url)
    multas = []
    trs = driver.find_elements_by_xpath("//*[@id='conteudo']/div[2]/div/div/div/div/table/tbody/tr")
    for tr in trs:
        multa = {}
        tds = tr.find_elements(By.TAG_NAME, "td")
        multa['placa'] = placa
        multa['sequencia'] = tds[0].text
        multa['processo'] = tds[1].text
        multa['descricao'] = tds[2].text
        multa['local'] = tds[3].text
        multa['valor'] = tds[4].text
        multa['url'] = tds[5].find_elements(By.TAG_NAME, "a")[0].get_attribute('href')
        multas.append(json.dumps(multa))
    return multas