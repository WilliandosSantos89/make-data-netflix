# Extração e Manipulação de Dados com Python

---
Este projeto tem como objetivo demonstrar como utilizar Python de forma prática para extrair e manipular dados de arquivos Excel. O código apresentado foi desenvolvido para lidar com arquivos Excel localizados em um diretório específico e realizar operações de tratamento de dados, como adicionar informações do arquivo ao DataFrame e extrair dados específicos.
___

**Funcionalidades**
- Localiza arquivos Excel em um diretório especificado.
- Lê cada arquivo Excel e adiciona o nome do arquivo a uma coluna 'filename'.
- Determina a localização com base no nome do arquivo ('brasil', 'france' ou 'italian') e adiciona essa informação a uma coluna 'location'.
- Extrai a campanha da coluna 'utm_link' e adiciona essa informação a uma coluna 'campaign'.
- Concatena todos os DataFrames tratados em um único DataFrame.
- Salva o DataFrame final em um arquivo Excel limpo.

**Como Usar**
- Clone o repositório para o seu computador.
- Certifique-se de ter o Python e as bibliotecas Pandas e XlsxWriter instaladas.
- Execute o arquivo extract_data.py.

**Estrutura do Projeto**
- src/: Contém o código fonte do projeto.
- data/
- raw/: Pasta onde devem ser colocados os arquivos Excel a serem processados.
- ready/: Pasta onde o arquivo Excel limpo será salvo.
- extract_data.py: Arquivo principal do projeto, responsável por extrair e manipular os dados.
README.md: Este arquivo que você está lendo.

**Links Úteis**
- [Repositório Original](https://github.com/digitalinnovationone/netflix-dataset/tree/main)
- [Instalar Python](https://www.python.org/downloads/)
- [Documentação Pandas](https://pandas.pydata.org/docs/)
- [Bootcamp Python](https://www.dio.me/sign-up?ref=2BXO5T6ZQ1)
- [Professor Felipe Aguiar](https://github.com/felipeAguiarCode) 
- [Meu Linkedin](https://www.linkedin.com/in/willian-dos-santos/)


**Contribuição**
Sinta-se à vontade para contribuir com melhorias neste projeto. Basta fazer um fork do repositório, implementar as melhorias e enviar um pull request.



