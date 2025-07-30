from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from time import sleep
import csv

# Configurando o chromedriver 

service = Service('/usr/bin/chromedriver')  # caminho para o ChromeDriver (Ubuntu)

# Inicializando o chromedriver

driver = webdriver.Chrome()

# Navegando para a página

driver.get("https://clone-olx-devaprender.netlify.app/")

# Aguarda a pagina carregar

sleep(3)

# Acha os elementos na pagina

preco = driver.find_elements(By.XPATH, "//span[@class='text-2xl font-bold text-gray-900']")
produto = driver.find_elements(By.XPATH, "//h3[@class='text-base text-gray-900 line-clamp-2 mb-1 hover:text-[#6E0AD6]']")
descricao = driver.find_elements(By.XPATH, "//p[@class='text-sm text-gray-500 line-clamp-2 mb-3']")
cidade = driver.find_elements(By.XPATH, "//div[@class='flex items-center']")

# Escreve os dados no console

for i in range(len(produto)):
    print(f"Produto: {produto[i].text} - Preço: {preco[i].text} - Descrição : {descricao[i].text} - Cidade: {cidade[i].text}")

# Cria um arquivo CSV e escreve os dados

    with open('produtos.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Produto', 'Preço', 'Descrição' , 'Cidade'])  # Escreve o cabeçalho
        for i in range(len(produto)):
            writer.writerow([produto[i].text, preco[i].text, descricao[i].text, cidade[i].text])  # Escreve os dados no CSV

# Fecha o navegador

driver.quit()