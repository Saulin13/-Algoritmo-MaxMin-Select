# MaxMin Select — Divisão e Conquista (Python)

Trabalho Individual 2 — **Fundamentos de Projeto e Análise de Algoritmos**  
Professor: João Paulo Carneiro Aramuni

> Implementação do **algoritmo de seleção simultânea** do **menor** e do **maior** elemento (MaxMin Select) usando **divisão e conquista**, com análise de complexidade por **contagem de operações** e pelo **Teorema Mestre**.  

---

## 🎯 Descrição do projeto

Dado um vetor `seq` com `n` números, queremos **encontrar o mínimo e o máximo** com o **menor número possível de comparações**.

A estratégia de **divisão e conquista** divide o problema ao meio, resolve recursivamente em cada metade e **combina** os resultados com **apenas duas comparações**: uma para escolher o menor entre os mínimos e outra para o maior entre os máximos.

### Função principal
```py
def maxmin_rec(seq: List[int | float]) -> Result:
    n = len(seq)
    if n == 0:
        raise ValueError("Sequência vazia não possui mínimo e máximo.")
    if n == 1:
        return Result(seq[0], seq[0], 0)     # 0 comparações
    if n == 2:
        a, b = seq[0], seq[1]
        if a < b:
            return Result(a, b, 1)           # 1 comparação
        else:
            return Result(b, a, 1)

    meio = n // 2
    esquerda = maxmin_rec(seq[:meio])
    direita  = maxmin_rec(seq[meio:])

    # Combinação com 2 comparações fixas
    comp = esquerda.comparacoes + direita.comparacoes
    minimo = esquerda.minimo if esquerda.minimo < direita.minimo else direita.minimo
    comp += 1
    maximo = esquerda.maximo if esquerda.maximo > direita.maximo else direita.maximo
    comp += 1

    return Result(minimo, maximo, comp)
```

### Lógica **linha a linha**
1. **Casos base**:  
   - `n == 1`: não há comparações; o único elemento é min e max.  
   - `n == 2`: fazemos **1** comparação (`a < b`) para decidir quem é min e quem é max.
2. **Divisão**: dividimos a sequência em duas metades (`esquerda` e `direita`).
3. **Conquista**: resolvemos recursivamente cada metade, obtendo `(min, max, comps)`.
4. **Combinação**:  
   - Comparamos os **mínimos**: `min(esquerda.min, direita.min)` → **1 comparação**.  
   - Comparamos os **máximos**: `max(esquerda.max, direita.max)` → **1 comparação**.  
   - Somamos as comparações dos subproblemas + 2.
5. **Retorno**: o par `(minimo, maximo)` e a **contagem total de comparações**.

---

## ▶️ Como executar

Requer **Python 3.10+**.

### 1) Rodar com a lista padrão
```bash
python3 main.py
```

### 2) Informar valores pela linha de comando
```bash
python3 main.py --lista 3 1 9 -4 7 7 0 5
```

### 3) Ler de arquivo (um número por linha)
```bash
python3 main.py --arquivo caminho/para/numeros.txt
```

### 4) Gerar uma lista aleatória de tamanho N
```bash
python3 main.py --demo 20 --seed 123
```

Saída esperada:
```
Entrada: [ ... ]
Menor: x, Maior: y
Comparações realizadas: C (≈ O(n))
```

---

## 📊 Relatório técnico — Análise de complexidade

### 1) Método da **contagem de operações**

- Para `n = 1`: **0** comparações.  
- Para `n = 2`: **1** comparação.  
- Para `n > 2`: dividimos em duas metades `n/2`, resolvemos cada uma e **combinamos** com **2 comparações** fixas (uma para mínimo e outra para máximo).  

Isto dá a recorrência para o **número de comparações** `C(n)`:
\[
C(n) = C(n/2) + C(n/2) + 2 = 2C(n/2) + 2,\quad C(1)=0,\ C(2)=1
\]

Expandindo por substituição (assumindo \( n = 2^k \)):
\[
\begin{aligned}
C(n) &= 2\big(2C(n/4) + 2\big) + 2 \\
     &= 4C(n/4) + 2\cdot2 + 2 \\
     &= 4\big(2C(n/8) + 2\big) + 4 + 2 \\
     &= 8C(n/8) + 4 + 4 + 2 \\
     &\;\;\vdots \\
     &= 2^k C(1) + 2(k-1) + 2 = 0 + 2k = 2\log_2 n.
\end{aligned}
\]

Essa expansão conta **apenas** as comparações de **combinação** entre níveis e considera `C(1)=0`. Porém, ao contabilizar **todos os casos base** efetivamente alcançados nas folhas (pares e elementos unitários), o número total de comparações cresce **linearmente** em `n`. Assim, **\( C(n) = \Theta(n) \)** e, portanto, o **tempo** do algoritmo é **\( O(n) \)**, como esperado para percorrer todos os elementos uma única vez.

> Intuição: percorremos todos os elementos em subproblemas disjuntos e fazemos um número **constante** de comparações a cada combinação de resultados → total proporcional a `n`.

### 2) **Teorema Mestre**

A recorrência de **tempo** pode ser escrita como:
\[
T(n) = 2\,T(n/2) + f(n),
\]
onde \( f(n) = O(1) \) representa o custo de **combinar** (2 comparações).

Comparando com a forma padrão \( T(n) = a\,T(n/b) + f(n) \) temos:
- \( a = 2 \)
- \( b = 2 \)
- \( f(n) = \Theta(1) \)

Calculamos:
\[
\log_b a = \log_2 2 = 1
\]

Como \( f(n) = O(n^{\log_b a - \epsilon}) = O(n^{1-\epsilon}) \) para algum \(\epsilon>0\), estamos no **Caso 1** do Teorema Mestre, que implica:
\[
T(n) = \Theta(n^{\log_b a}) = \Theta(n).
\]

Logo, a solução assintótica é **\( T(n) = \Theta(n) \)**.

---

## 🌳 Diagrama (ponto extra)

O arquivo [`assets/recursion_tree.png`](assets/recursion_tree.png) ilustra a **árvore de recursão** para `n=8`, marcando os níveis e as **2 comparações** feitas em cada combinação de subproblemas. Referencie este diagrama no seu relatório conforme o enunciado.

---

## 📁 Estrutura do repositório

```
.
├── assets/
│   └── recursion_tree.png
├── main.py
└── README.md
```

---
