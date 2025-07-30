# 🛠️ Automação Web com Selenium - Coleta de Dados OLX Clone

Este projeto é uma automação desenvolvida em **Python** utilizando a biblioteca **Selenium** para coletar informações de produtos listados em uma página web (OLX Clone). Os dados extraídos incluem **produto, preço, descrição e cidade**, e são salvos em um arquivo CSV.

---

## 📌 Funcionalidades

- Acessa automaticamente o site [OLX Clone](https://clone-olx-devaprender.netlify.app/).
- Coleta as seguintes informações de cada produto:
  - Nome do produto
  - Preço
  - Descrição
  - Cidade
- Exibe os dados coletados no terminal.
- Salva os dados em um arquivo **`produtos.csv`** no formato tabular.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.12**
- **Selenium WebDriver**
- **Google Chrome** e **ChromeDriver**
- **CSV (módulo nativo do Python)**

---

## 📂 Estrutura do Projeto

📦 automacao-olx-clone
┣ 📜 app.py # Script principal de automação
┣ 📜 produtos.csv # Arquivo gerado com os dados coletados
┗ 📜 README.md # Documentação do projeto

---

## ⚙️ Pré-requisitos

1. Ter o **Python 3.x** instalado.
2. Instalar o **Google Chrome**.
3. Instalar o **ChromeDriver** compatível com a versão do seu navegador.
4. Instalar as dependências do projeto:
   ```bash
   pip install selenium
   ```

▶️ Como Executar

1. Clone este repositório:

````bash git clone https://github.com/seu-usuario/automacao-olx-clone.git
``` cd automacao-olx-clone

2. Verifique se o caminho do ChromeDriver no app.py está correto:
 ```bash service = Service('/usr/bin/chromedriver') ```
  ```bash Ajuste o caminho se necessário. ```

3. Execute o script:
```bash python3 app.py ```

4. O script abrirá o navegador, coletará os dados e gerará o arquivo produtos.csv.


📊 Exemplo de Saída (Terminal)
```bash Produto: Notebook Dell Inspiron - Preço: R$ 2.500 - Descrição: Notebook Dell com 8GB RAM - Cidade: São Paulo
Produto: Smartphone Samsung S22 - Preço: R$ 3.000 - Descrição: Aparelho novo, lacrado - Cidade: Rio de Janeiro```

````

📈 Melhorias Futuras
Adicionar suporte a mais páginas (paginação).

Tratar erros de conexão e elementos não encontrados.

Permitir salvar em outros formatos (JSON, Excel).

Executar em modo headless (sem abrir o navegador).

📝 Observações
Este projeto é apenas para fins de estudo.

O site utilizado é um clone didático da OLX e não deve ser utilizado em produções reais sem permissão.

Desenvolvido por André Victor.
