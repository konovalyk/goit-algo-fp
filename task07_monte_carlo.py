# python task07_monte_carlo.py --trials 10000
import random
from collections import Counter
from typing import Dict, List, Tuple

import matplotlib.pyplot as plt


# Theoretical probabilities for sum of two dice
THEORETICAL_PROBABILITIES: Dict[int, float] = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36,
}


def monte_carlo_simulation(trials: int = 1_000_000) -> Dict[int, float]:
    sums: List[int] = []
    for _ in range(trials):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        sums.append(die1 + die2)

    counter = Counter(sums)
    empirical = {s: counter[s] / trials for s in range(2, 13)}
    return empirical


def print_comparison(theoretical: Dict[int, float], empirical: Dict[int, float]) -> None:
    print("\n" + "=" * 80)
    print(f"{'Сума':<6} {'Теоретична':<15} {'Монте-Карло':<15} {'Різниця':<15} {'Відсоток':<10}")
    print("=" * 80)
    for s in range(2, 13):
        theo = theoretical[s]
        emp = empirical.get(s, 0)
        diff = abs(theo - emp)
        pct = (diff / theo * 100) if theo > 0 else 0
        print(f"{s:<6} {theo:<15.6f} {emp:<15.6f} {diff:<15.6f} {pct:<10.2f}%")
    print("=" * 80)


def plot_comparison(theoretical: Dict[int, float], empirical: Dict[int, float]) -> None:
    sums = sorted(theoretical.keys())
    theo_probs = [theoretical[s] for s in sums]
    emp_probs = [empirical.get(s, 0) for s in sums]

    x = range(len(sums))
    width = 0.35

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar([i - width / 2 for i in x], theo_probs, width, label="Теоретична", alpha=0.8)
    ax.bar([i + width / 2 for i in x], emp_probs, width, label="Монте-Карло", alpha=0.8)

    ax.set_xlabel("Сума двох кубиків")
    ax.set_ylabel("Ймовірність")
    ax.set_title("Порівняння теоретичних та емпіричних ймовірностей")
    ax.set_xticks(x)
    ax.set_xticklabels(sums)
    ax.legend()
    ax.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.show()


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=1_000_000)
    args = parser.parse_args()

    print(f"Симуляція {args.trials:,} кидків двох кубиків...")
    empirical = monte_carlo_simulation(args.trials)

    print_comparison(THEORETICAL_PROBABILITIES, empirical)
    plot_comparison(THEORETICAL_PROBABILITIES, empirical)


if __name__ == "__main__":
    main()
