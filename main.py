
from __future__ import annotations
from dataclasses import dataclass
from typing import List, Tuple, Optional
import argparse
import random

@dataclass
class Result:
    minimo: int | float
    maximo: int | float
    comparacoes: int  # contagem de comparações realizadas

def maxmin_rec(seq: List[int | float]) -> Result:
    """
    Retorna (minimo, maximo, comparacoes) usando divisão e conquista.
    Recorrência: T(n) = 2T(n/2) + O(1) (2 comparações para combinar resultados).
    Casos base: n=1 e n=2.
    """
    n = len(seq)
    if n == 0:
        raise ValueError("Sequência vazia não possui mínimo e máximo.")
    if n == 1:
        return Result(seq[0], seq[0], 0)
    if n == 2:
        a, b = seq[0], seq[1]
        if a < b:
            return Result(a, b, 1)
        else:
            return Result(b, a, 1)

    meio = n // 2
    esquerda = maxmin_rec(seq[:meio])
    direita  = maxmin_rec(seq[meio:])

    comp = esquerda.comparacoes + direita.comparacoes
    minimo = esquerda.minimo if esquerda.minimo < direita.minimo else direita.minimo
    comp += 1
    maximo = esquerda.maximo if esquerda.maximo > direita.maximo else direita.maximo
    comp += 1

    return Result(minimo, maximo, comp)

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="MaxMin Select (Divisão e Conquista)")
    g = p.add_mutually_exclusive_group()
    g.add_argument("--lista", nargs="+", type=float, help="Lista de números (ex: --lista 3 1 9 -4 7)")
    g.add_argument("--arquivo", type=str, help="Caminho de arquivo com um número por linha")
    g.add_argument("--demo", type=int, metavar="N", help="Gera uma lista aleatória de tamanho N para demonstração")
    p.add_argument("--seed", type=int, default=42, help="Semente do gerador aleatório para --demo (default: 42)")
    return p.parse_args()

def carregar_entrada(args: argparse.Namespace) -> list[float]:
    if args.lista is not None:
        return [float(x) for x in args.lista]
    if args.arquivo:
        with open(args.arquivo, "r", encoding="utf-8") as f:
            return [float(l.strip()) for l in f if l.strip()]
    if args.demo is not None:
        random.seed(args.seed)
        return [random.randint(-100, 100) for _ in range(args.demo)]
    # Se nada for passado, usa um exemplo simples
    return [3, 1, 9, -4, 7, 7, 0, 5]

def main():
    args = parse_args()
    dados = carregar_entrada(args)
    res = maxmin_rec(dados)
    print("Entrada:", dados)
    print(f"Menor: {res.minimo}, Maior: {res.maximo}")
    print(f"Comparacoes realizadas: {res.comparacoes} (~= 2T(n/2)+O(1) => O(n))")

if __name__ == "__main__":
    main()
