.PHONY: install
install:
	@ansible-galaxy install --force --role-file=requirements.txt
