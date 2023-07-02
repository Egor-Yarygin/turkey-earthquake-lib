# Тестирование
test:
    pytest test.py

# Сборка
build:
	python setup.py sdist bdist_wheel

# Установка
install:
	python -m pip install .
