[![API tests](https://github.com/pav1top/Autotests-on-Python/actions/workflows/tests.yml/badge.svg)](https://github.com/pav1top/Autotests-on-Python/actions/workflows/tests.yml)

# Autotests on Python

API autotests for jsonplaceholder on pytest + requests.

## How to run

```
pip install -r requirements.txt
pytest
```

More options:

```
pytest -v                 # подробный вывод
pytest -m negative        # только негативные тесты
pytest -m positive        # только позитивные тесты
```
