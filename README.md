# pydrive-images-clone

Copia seus arquivos do Google Drive em uma pasta local

## Instalação

Intale os pacotes com `pip install -r requirements.txt`

Depois siga esse [tutorial](https://pythonhosted.org/PyDrive/quickstart.html)
para obter o arquivo `client_secrets.json`

Você pode definir quais pastas do Google Drive serão copiadas criando um
arquivo `.env`, como no exemplo abaixo, para as pastas `teste` e `teste2`:

```
FOLDERS="teste;teste2"
```

## Uso

Rode o arquivo `main.py` com o parâmetro `-d pasta_destino` para definir a
pasta onde serão copiados os arquivos:

```
> python main.py -d ./pasta_teste
```
