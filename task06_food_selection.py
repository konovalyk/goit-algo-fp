# python task06_food_selection.py --budget 110
from typing import Dict, List, Tuple

items: Dict[str, Dict[str, int]] = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items: Dict[str, Dict[str, int]], budget: int) -> Dict[str, int | List[str]]:
    sorted_items = sorted(
        items.items(), key=lambda kv: kv[1]["calories"] / kv[1]["cost"], reverse=True
    )
    chosen: List[str] = []
    spent = 0
    gained = 0
    for name, data in sorted_items:
        c = data["cost"]
        cal = data["calories"]
        if spent + c <= budget:
            chosen.append(name)
            spent += c
            gained += cal
    return {"chosen": chosen, "cost": spent, "calories": gained}


def dynamic_programming(items: Dict[str, Dict[str, int]], budget: int) -> Dict[str, int | List[str]]:
    names = list(items.keys())
    costs = [items[n]["cost"] for n in names]
    calories = [items[n]["calories"] for n in names]
    n = len(names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        c = costs[i - 1]
        cal = calories[i - 1]
        for w in range(budget + 1):
            dp[i][w] = dp[i - 1][w]
            if c <= w:
                cand = dp[i - 1][w - c] + cal
                if cand > dp[i][w]:
                    dp[i][w] = cand

    # reconstruct selected items
    w = budget
    chosen: List[str] = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(names[i - 1])
            w -= costs[i - 1]
    chosen.reverse()
    spent = sum(items[n]["cost"] for n in chosen)
    gained = sum(items[n]["calories"] for n in chosen)
    return {"chosen": chosen, "cost": spent, "calories": gained}


def _print_solution(title: str, result: Dict[str, int | List[str]]) -> None:
    print(title)
    print(f"  Обрано: {result['chosen']}")
    print(f"  Вартість: {result['cost']}, Калорії: {result['calories']}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--budget", type=int, default=90)
    args = parser.parse_args()

    print(f"Бюджет: {args.budget}")
    greedy_res = greedy_algorithm(items, args.budget)
    dp_res = dynamic_programming(items, args.budget)

    _print_solution("\nЖадібний алгоритм:", greedy_res)
    _print_solution("\nДинамічне програмування:", dp_res)
