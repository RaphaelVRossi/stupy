test: unit

unit:
	@pytest --cov=stupy tests/

setup build install:
	@pip install -Ue .[tests]

format:
	@black .

package:
	@python setup.py sdist

deploy:
	@echo "deployed!"
