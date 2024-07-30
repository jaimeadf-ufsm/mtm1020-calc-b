# Trabalho Extra

Minimização de funções utilizando o método de Newton e a descida de gradiente.

## Requisitos

- [Python](https://www.python.org/)

## Execução

1. Baixe os arquivos clicando [aqui](https://git-link.vercel.app/api/download?url=https%3A%2F%2Fgithub.com%2Fjaimeadf-ufsm%2Fmtm1020-calcb%2Ftree%2Fmain%2Ftrabalhos%2Fextra).

2. Descompacte o arquivo zip e abra o terminal na pasta onde os arquivos `.py` estão localizados.

3. Instale as dependências com o comando:
   ```sh
    pip install -r requirements.txt
   ```

4. Execute os scripts conforme o método desejado:
   - Para o método de Newton:
     ```sh
        python newton.py
     ```
   - Para a descida de gradiente:
     ```sh
        python gradient_descent.py
     ```

5. Caso esteja no linux ou no macOS, você pode utilizar os arquivos de exemplo como entrada:

```sh
    python newton.py < examples/n01.txt
    python gradient_descent.py < examples/g01.txt
```