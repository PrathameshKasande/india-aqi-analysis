.PHONY: install test clean run

install:
	pip install -r requirements.txt

test:
	pytest python/tests/

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -rf .pytest_cache

run:
	python python/src/main.py