APP_DIR = .

install:
	virtualenv venv
	$(APP_DIR)/install_deps.sh
	$(APP_DIR)/venv/bin/pip install -r requirements.txt
	$(APP_DIR)/install_sip.sh
	$(APP_DIR)/install_pyqt.sh

run:
	./venv/bin/python $(APP_DIR)/src/main.py

test:
	./venv/bin/python $(APP_DIR)/tests/runner.py
