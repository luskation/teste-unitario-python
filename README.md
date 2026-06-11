# Teste Unitário com Python

Projeto desenvolvido nas aulas práticas de Teste de Software utilizando Python e `unittest`.

## Estrutura do projeto

```
teste-unitario-python/
│
├── calculadora.py           # Funções matemáticas
├── test_calculadora.py      # Testes da aula anterior (Teste Unitário 1)
├── test_calculadora_ia.py   # Testes desta aula (Teste Unitário IA)
└── README.md
```

## Como executar os testes

```bash
python -m unittest discover
```

---

## Uso de IA para geração de cenários de teste

### Função escolhida

`calcular_media(lista)`

### Prompt utilizado

```text
Atue como um professor de Teste de Software.

Tenho a seguinte função Python:

def calcular_media(lista):
    if not lista:
        raise ValueError("A lista não pode estar vazia.")
    return sum(lista) / len(lista)

Quero criar testes unitários usando unittest.

Antes de gerar o código, liste cenários de teste para essa função.

Para cada cenário, informe:
- nome do cenário;
- entrada usada;
- resultado esperado;
- tipo do cenário: caso normal, caso de borda ou caso de erro.

Use linguagem simples, pois sou iniciante em testes unitários. Responda em português.
```

### Cenários sugeridos pela IA

| ID  | Cenário                          | Entrada                          | Resultado esperado | Tipo        |
|:----|:---------------------------------|:---------------------------------|:-------------------|:------------|
| T01 | Lista com inteiros               | `calcular_media([10, 8, 6])`     | `8`                | normal      |
| T02 | Lista com decimais               | `calcular_media([2.5, 7.5])`     | `5.0`              | normal      |
| T03 | Lista com negativos              | `calcular_media([-2, -4, -6])`   | `-4`               | normal      |
| T04 | Lista com positivos e negativos  | `calcular_media([-5, 5])`        | `0`                | normal      |
| T05 | Lista com um único elemento      | `calcular_media([7])`            | `7`                | borda       |
| T06 | Lista com apenas zeros           | `calcular_media([0, 0, 0])`      | `0`                | borda       |
| T07 | Lista vazia                      | `calcular_media([])`             | `ValueError`       | erro        |

### Análise dos cenários

Todos os 7 cenários sugeridos pela IA foram **aceitos** sem alterações, pois todos fazem sentido lógico e cobrem situações reais de uso da função.

- **T01, T02, T03, T04** cobrem o uso normal da função com diferentes tipos de número.
- **T05** é um caso de borda relevante: uma lista com um único elemento deve retornar o próprio valor.
- **T06** é um caso de borda que verifica se a função lida corretamente com zeros.
- **T07** já existia nos testes anteriores, mas foi mantido e documentado porque é o único caso de erro da função.

Os cenários T05 e T06 **não estavam nos testes originais** e foram uma contribuição importante da IA.

### Código final dos testes

```python
# test_calculadora_ia.py

import unittest
from calculadora import calcular_media


class TestCalculadoraIA(unittest.TestCase):

    def test_media_lista_inteiros(self):
        """Caso normal: lista com múltiplos números inteiros."""
        self.assertEqual(calcular_media([10, 8, 6]), 8)

    def test_media_lista_decimais(self):
        """Caso normal: lista com números decimais."""
        self.assertEqual(calcular_media([2.5, 7.5]), 5.0)

    def test_media_lista_negativos(self):
        """Caso normal: lista com números negativos."""
        self.assertEqual(calcular_media([-2, -4, -6]), -4)

    def test_media_lista_positivos_e_negativos(self):
        """Caso normal: lista com positivos e negativos que se cancelam."""
        self.assertEqual(calcular_media([-5, 5]), 0)

    def test_media_lista_um_elemento(self):
        """Caso de borda: lista com um único elemento deve retornar o próprio valor."""
        self.assertEqual(calcular_media([7]), 7)

    def test_media_lista_todos_zeros(self):
        """Caso de borda: lista com apenas zeros deve retornar zero."""
        self.assertEqual(calcular_media([0, 0, 0]), 0)

    def test_media_lista_vazia_lanca_excecao(self):
        """Caso de erro: lista vazia deve lançar ValueError."""
        with self.assertRaises(ValueError):
            calcular_media([])


if __name__ == "__main__":
    unittest.main()
```

### Resultado da execução

```bash
python -m unittest test_calculadora_ia -v
```

Saída obtida:

```
test_media_lista_decimais (test_calculadora_ia.TestCalculadoraIA.test_media_lista_decimais)
Caso normal: lista com números decimais. ... ok
test_media_lista_inteiros (test_calculadora_ia.TestCalculadoraIA.test_media_lista_inteiros)
Caso normal: lista com múltiplos números inteiros. ... ok
test_media_lista_negativos (test_calculadora_ia.TestCalculadoraIA.test_media_lista_negativos)
Caso normal: lista com números negativos. ... ok
test_media_lista_positivos_e_negativos (test_calculadora_ia.TestCalculadoraIA.test_media_lista_positivos_e_negativos)
Caso normal: lista com positivos e negativos que se cancelam. ... ok
test_media_lista_todos_zeros (test_calculadora_ia.TestCalculadoraIA.test_media_lista_todos_zeros)
Caso de borda: lista com apenas zeros deve retornar zero. ... ok
test_media_lista_um_elemento (test_calculadora_ia.TestCalculadoraIA.test_media_lista_um_elemento)
Caso de borda: lista com um único elemento deve retornar o próprio valor. ... ok
test_media_lista_vazia_lanca_excecao (test_calculadora_ia.TestCalculadoraIA.test_media_lista_vazia_lanca_excecao)
Caso de erro: lista vazia deve lançar ValueError. ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.002s

OK
```
