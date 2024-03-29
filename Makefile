VERSION = 3.1.0
VENV_PATH = ./venv
VENV = . $(VENV_PATH)/bin/activate;
SRC := \
	$(wildcard src/arrrgs/*.py)

.PHONY: publish
publish:
	make clean
	make build
	git tag "v$(VERSION)"
	git push --tags
	$(VENV) python3 -m twine upload --repository pypi dist/* -umishamyrt

.PHONY: clean
clean:
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist

.PHONY: build
build:
	echo "$(VERSION)" > .version
	$(VENV) python -m build

.PHONY: install
install: build
	$(VENV) pip3 install .

.PHONY: install-system
install-system: build
	pip3 install .

.PHONY: lint
lint:
	$(VENV) pylint $(SRC)
	$(VENV) ruff $(SRC)

configure: requirements.txt
	rm -rf $(VENV_PATH)
	make $(VENV_PATH)

$(VENV_PATH):
	python3 -m venv $(VENV_PATH)
	$(VENV) pip install -r requirements.txt

$(CONFIG_PATH): config.json
	mkdir -p $(CONFIG_DIR)
	rm -f $(CONFIG_PATH)
	cp config.json $(CONFIG_PATH)
