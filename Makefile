.PHONY: test lint

test:
	pytest tests --maxfail=1 --disable-warnings -q

lint:
	flake8 src tests
