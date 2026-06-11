# 🧪 Teste Unitário com Python

> Projeto desenvolvido nas aulas práticas de **Teste de Software** da UFLA, utilizando Python e `unittest` — com uma segunda etapa explorando o uso de **IA generativa** como apoio na elaboração de cenários de teste.

---

## 📋 Índice

- [Visão Geral](#-visão-geral)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Como Executar](#-como-executar)
- [Módulo: Calculadora](#-módulo-calculadora)
- [Aula 1 — Testes Unitários com PyUnit](#-aula-1--testes-unitários-com-pyunit)
- [Aula 2 — IA na Geração de Cenários de Teste](#-aula-2--ia-na-geração-de-cenários-de-teste)
- [Resultados](#-resultados)
- [Aprendizados](#-aprendizados)

---

## 🔍 Visão Geral

Este repositório documenta uma progressão de duas aulas práticas sobre testes unitários em Python. Na primeira, os testes foram escritos manualmente para consolidar o entendimento dos fundamentos. Na segunda, uma ferramenta de IA foi usada como assistente para sugerir cenários — com análise crítica dos resultados antes de qualquer código ser aceito.

O objetivo não é apenas fazer os testes passarem. É entender **o que** está sendo testado, **por que** cada cenário importa e **como** usar ferramentas modernas sem perder o raciocínio técnico.

---

## 📁 Estrutura do Projeto

```
teste-unitario-python/
│
├── calculadora.py            # Funções matemáticas testadas
├── test_calculadora.py       # Testes escritos manualmente (Aula 1)
├── test_calculadora_ia.py    # Testes com apoio de IA (Aula 2)
└── README.md
```

---

## 🛠️ Tecnologias Utilizadas

| Ferramenta | Versão | Finalidade |
|:---|:---|:---|
| Python | 3.12+ | Linguagem principal |
| `unittest` (PyUnit) | nativo | Framework de testes |
| Claude (Anthropic) | — | Geração de cenários de teste (Aula 2) |
| VS Code | — | Ambiente de desenvolvimento |
| Git / GitHub | — | Versionamento e entrega |

---

## ▶️ Como Executar

**Executar todos os testes:**
```bash
python -m unittest discover
```

**Executar um arquivo específico com saída detalhada:**
```bash
python -m unittest test_calculadora -v
python -m unittest test_calculadora_ia -v
```

**Saída esperada (todos passando):**
```
----------------------------------------------------------------------
Ran 15 tests in 0.003s

OK
```

---

## 🔢 Módulo: Calculadora

O arquivo `calculadora.py` contém seis funções matemáticas que servem como alvo dos testes.

```python
def somar(a, b)       # Retorna a + b
def subtrair(a, b)    # Retorna a - b
def multiplicar(a, b) # Retorna a * b
def dividir(a, b)     # Retorna a / b  →  ZeroDivisionError se b == 0
def potencia(a, b)    # Retorna a ** b
def calcular_media(lista)  # Retorna a média  →  ValueError se lista vazia
```

A função `dividir` delega o tratamento de erro ao próprio Python (`ZeroDivisionError`). Já `calcular_media` valida a entrada explicitamente e lança `ValueError` — uma decisão de design que também é testada.

---

## 📘 Aula 1 — Testes Unitários com PyUnit

### Objetivo

Aprender a estrutura de um teste unitário: importar `unittest`, criar uma classe que herda de `TestCase`, escrever métodos prefixados com `test_` e usar asserções como `assertEqual` e `assertRaises`.

### Estratégia adotada

Os testes foram organizados usando `subTest`, o que permite cobrir múltiplos casos dentro de um único método sem perder a rastreabilidade em caso de falha — cada subcase é reportado individualmente pelo runner.

```python
def test_somar_com_varios_casos(self):
    casos = [(2, 3, 5), (5, 0, 5), (0, 0, 0), (-2, 5, 3), (-2, -3, -5)]
    for a, b, esperado in casos:
        with self.subTest(a=a, b=b):
            self.assertEqual(somar(a, b), esperado)
```

### Cobertura de cenários — Aula 1

| Função | Casos normais | Casos de borda | Casos de erro |
|:---|:---:|:---:|:---:|
| `somar` | ✅ 3 | ✅ 2 | — |
| `subtrair` | ✅ 3 | ✅ 1 | — |
| `multiplicar` | ✅ 3 | ✅ 1 | — |
| `dividir` | ✅ 3 | ✅ 1 | ✅ 1 |
| `potencia` | ✅ 3 | ✅ 1 | — |
| `calcular_media` | ✅ 3 | ✅ 2 | ✅ 1 |

---

## 🤖 Aula 2 — IA na Geração de Cenários de Teste

### Objetivo

Usar IA generativa como ferramenta de apoio para identificar cenários de teste, avaliar criticamente as sugestões recebidas e transformá-las em código `unittest`. A IA não substitui o raciocínio — ela amplia o leque de possibilidades que o desenvolvedor avalia.

### Função escolhida

`calcular_media(lista)` — escolhida por ter comportamento mais rico: aceita diferentes tipos de número, tem um caso de borda relevante (lista com um elemento) e um caso de erro explícito (lista vazia).

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

| ID | Cenário | Entrada | Resultado esperado | Tipo |
|:---|:---|:---|:---|:---|
| T01 | Lista com inteiros | `[10, 8, 6]` | `8` | Normal |
| T02 | Lista com decimais | `[2.5, 7.5]` | `5.0` | Normal |
| T03 | Lista com negativos | `[-2, -4, -6]` | `-4` | Normal |
| T04 | Positivos e negativos | `[-5, 5]` | `0` | Normal |
| T05 | Um único elemento | `[7]` | `7` | Borda |
| T06 | Apenas zeros | `[0, 0, 0]` | `0` | Borda |
| T07 | Lista vazia | `[]` | `ValueError` | Erro |

### Análise crítica dos cenários

Todos os 7 cenários foram **aceitos sem alteração**. A justificativa para cada decisão:

- **T01–T04 (aceitos):** cobrem o uso normal com os tipos de número mais comuns. T04 é particularmente útil para verificar que a média de opostos simétricos é zero — um erro de sinal passaria despercebido sem ele.
- **T05 (aceito):** caso de borda genuíno. Uma lista com um único elemento deve retornar o próprio valor. Sem esse teste, uma implementação que erroneamente exige pelo menos dois elementos passaria nos demais testes.
- **T06 (aceito):** verifica que a função não confunde "lista de zeros" com "lista vazia". É uma distinção sutil que a IA identificou e que **não estava nos testes originais da Aula 1**.
- **T07 (aceito):** já existia na Aula 1, mas foi mantido e documentado porque é o único caminho de erro da função — remover seria regredir.

> 💡 **Observação:** T05 e T06 são os casos com maior valor agregado desta etapa. A IA ampliou a cobertura em cenários de borda que o desenvolvedor não havia considerado explicitamente.

### Código final — `test_calculadora_ia.py`

```python
import unittest
from calculadora import calcular_media


class TestCalculadoraIA(unittest.TestCase):
    """Testes ampliados para calcular_media com cenários sugeridos por IA."""

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

```
test_media_lista_decimais ... ok
test_media_lista_inteiros ... ok
test_media_lista_negativos ... ok
test_media_lista_positivos_e_negativos ... ok
test_media_lista_todos_zeros ... ok
test_media_lista_um_elemento ... ok
test_media_lista_vazia_lanca_excecao ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.002s

OK
```

---

## ✅ Resultados

| Arquivo | Testes | Status |
|:---|:---:|:---:|
| `test_calculadora.py` | 8 | ✅ Todos passando |
| `test_calculadora_ia.py` | 7 | ✅ Todos passando |
| **Total** | **15** | ✅ |

---

## 💡 Aprendizados

**Sobre testes unitários:**
- Um teste que nunca falha não necessariamente é um bom teste — pode só não estar cobrindo os casos certos.
- `subTest` muda a qualidade do feedback: em vez de parar no primeiro erro, você vê exatamente qual combinação de entrada falhou.
- Casos de borda são os mais valiosos e os mais fáceis de esquecer.

**Sobre usar IA no processo:**
- A IA é útil para expandir o leque de cenários, especialmente casos que o desenvolvedor tende a ignorar por familiaridade com o código.
- Aceitar sugestões sem análise crítica é o maior risco: a IA pode gerar cenários com resultados esperados errados, funções que não existem ou código fora do padrão do framework.
- O fluxo correto é: **cenários primeiro, código depois** — avaliar a lógica antes de ver implementação evita ancoragem no código gerado.

---

<p align="center">
  Desenvolvido por <strong>Lucas</strong> · UFLA · Disciplina de Teste de Software
</p>
