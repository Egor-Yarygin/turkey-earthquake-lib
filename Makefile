# # Тестирование
test:
	pytest test.py

# # Сборка
build:
	python setup.py sdist
	python setup.py bdist_wheel

# Установка
install:
	conda install cartopy
	python -m pip install .