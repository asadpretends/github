install:
	pip install --upgrade pip&\
	pip install -r requirements.txt

lint:
	pylint --disable=C,R app.py

test:
	python -m pytest -vv --cov=app test_app.py
