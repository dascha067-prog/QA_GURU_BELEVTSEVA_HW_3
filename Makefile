# --- Windows-friendly Makefile (PowerShell/CMD) ---
SHELL := cmd.exe
.SHELLFLAGS := /C

.PHONY: help install run_test test_only linter hooks clean

# Справка
help:
	@echo.
	@echo Makefile commands:
	@echo   make install    - Установить зависимости
	@echo   make run_test   - Запустить все автотесты (pytest -v)
	@echo   make test_only  - Запустить тесты с меткой (по умолчанию: only)
	@echo   make linter     - Отформатировать и проверить код (isort, black, flake8)
	@echo   make hooks      - Установить/обновить pre-commit хуки
	@echo   make clean      - Очистить кеши/отчёты
	@echo.

# Установка зависимостей
install:
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt

# Запуск всех тестов
run_test:
	python -m pytest -v

# Форматирование и проверка стиля
linter:
	isort .
	black .
	flake8 .
