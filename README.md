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
