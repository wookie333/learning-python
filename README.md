# Learning Python 🐍

Мой учебный репозиторий по Python и основам Data Science / Machine Learning.

Здесь я собираю конспекты, практику и небольшие задания по мере обучения.

## 📚 Что изучаю

* **NumPy** — работа с массивами и математическими операциями
* **Pandas** — обработка и анализ данных
* **Matplotlib** — визуализация данных
* **Scikit-learn** — первые шаги в Machine Learning

## 📂 Структура

```text
01-numpy/
    notes/
02-pandas/
03-matplotlib/
04-sklearn/
```

Сейчас упражнения находятся в `01-numpy/tasks_intro.py` и `01-numpy/tasks_02.py`, конспекты — в `01-numpy/notes/`. Папки `02-pandas`, `03-matplotlib` и `04-sklearn` пока содержат только `.gitkeep`.

## ▶️ Установка и запуск

Команды выполняются из корня проекта. Для текущих упражнений нужен Python 3 и NumPy 2.x.

На macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install "numpy>=2,<3"
```

Если `.venv` уже создано, достаточно активировать его и установить NumPy, если он ещё не установлен.

Запуск упражнений:

```bash
python 01-numpy/tasks_intro.py
python 01-numpy/tasks_02.py
```

Во втором скрипте сообщение `out of bounds for int8` ожидаемо: это результат обработки `OverflowError` в задании про диапазон `int8`.

## 🎯 Цель

Разобраться в Python, Data Science и постепенно перейти к Machine Learning и ML Engineering.

## 📈 Progress

* [ ] NumPy
* [ ] Pandas
* [ ] Matplotlib
* [ ] Scikit-learn
* [ ] ML projects

> Learning by doing.
