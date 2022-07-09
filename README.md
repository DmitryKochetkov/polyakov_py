# Решения задач Полякова на Python

[![PolyakovPy Workflow](https://github.com/Dmitry-Kochetkov-space/polyakov_py/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/Dmitry-Kochetkov-space/polyakov_py/actions/workflows/python-package.yml)

Структура проекта:

- `Solutions_{}.ipynb` - Jupyter-ноутбук с решением всех задач данного типа
- `download_data.py` - Скрипт для скачивания входных данных и ответов к задачам

## Скачивание данных при помощи `download_data.py`

Автоматическое скачивание данных (файлов к задачам и ответов) можно запустить командой `python download_data.py -f`. В результате будет создана папка data со следующей структурой:
- `data/answers.csv` - Таблица ответов ко всем задачам
- `data/24data` - Входные данные к задачам 24
- `data/26data` - Входные данные к задачам 26
- `data/27data` - Входные данные к задачам 27

## Инструкции по запуску решений

Для запуска программного решения задачи используется команда `python -m solutionsX.problemY`, где `X` - номер типа задачи в ЕГЭ, `Y` - номер задачи в файле Полякова `egeX.doc`. Пример запуска 7-й задачи из файла ege27.doc:

```python -m solutions27.problem7```

## Тестирование

Для тестирования всех решений используется команда `python -m unittest discover -p "problem*.py" -v`.

Можно также тестировать решение одной задачи командой `python -m unittest solutionsX.problemY`, где `X` - номер типа задачи в ЕГЭ, `Y` - номер задачи в файле Полякова `egeX.doc`.
