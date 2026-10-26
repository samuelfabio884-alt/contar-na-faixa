
[README.md](https://github.com/user-attachments/files/33988020/README.md)
# Contar números em uma faixa (Python)

Programa de terminal que lê números digitados pelo usuário e conta quantos deles estão dentro de uma faixa definida. Foi feito como exercício de estudo de lógica de programação e Python.

## O que ele faz

1. Pede um número inteiro por vez.
2. Se o valor digitado não for um número inteiro, mostra um aviso e pede de novo.
3. Se o número estiver entre o mínimo e o máximo (inclusive), soma 1 ao contador.
4. Quando o usuário digita `0`, o programa para e mostra quantos números ficaram dentro da faixa.

Neste exemplo, a faixa é de **100 a 300**.

## Como executar

É necessário ter o Python 3 instalado.

```
python3 contar_na_faixa.py
```

No Windows, use `python contar_na_faixa.py`.

## Exemplo de uso

```
Digite um número (0 para sair): 150
Digite um número (0 para sair): 50
Digite um número (0 para sair): abc
Valor inválido! Digite apenas números inteiros.
Digite um número (0 para sair): 250
Digite um número (0 para sair): 300
Digite um número (0 para sair): 0
A quantidade de números entre 100 e 300 é: 3
```

Os valores 150, 250 e 300 estão na faixa. O 50 está fora, e o `abc` é rejeitado sem encerrar o programa.

## Conceitos praticados

- Funções com parâmetros e retorno (`contar_na_faixa(minimo, maximo)`), com dicas de tipo
- Laço `while True` com `break`
- Contador (`cont += 1`)
- Condição com comparação encadeada (`minimo <= num <= maximo`)
- Tratamento de erro com `try` / `except ValueError`
- Entrada e saída de dados (`input` e `print`)
- Uso de `if __name__ == "__main__"` para separar a função principal

## Ideias para evoluir

- Permitir que o usuário escolha o mínimo e o máximo ao iniciar o programa
- Mostrar também a soma e a média dos números que estão na faixa
- Guardar os números em uma lista para exibir todos no final
