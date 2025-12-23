## Heap Visualization

- Visualize a binary heap (array form) as a tree:

```
python heap_visualization.py
```

- Use programmatically:

```
from heap_visualization import visualize_heap

visualize_heap([1,3,5,7,9,11,13,15], title="Мін-купа")
```

# Fractal Tree (Task 2)

## Запуск

```bash
python pythagoras_tree.py -d 10 --linewidth 1.2 --speed 0.0008 --size 30 --scale 0.75
```

## Параметри

| Параметр      | Опис                                                                   |
| ------------- | ---------------------------------------------------------------------- |
| `-d, --depth` | Глибина рекурсії                                                       |
| `--linewidth` | Товщина ліній                                                          |
| `--speed`     | Пауза між сегментами в секундах (для live-анімації)                    |
| `--size`      | Довжина початкового стовбура                                           |
| `--scale`     | Коефіцієнт масштабування гілок на кожному рівні (за замовчуванням 0.7) |

**Примітка:** Кут розгалуження фіксований 45° (класичне дерево Піфагора).
