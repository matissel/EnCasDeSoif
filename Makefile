COM_COLOR   = \033[0;34m
OBJ_COLOR   = \033[0;36m
OK_COLOR    = \033[0;32m
ERROR_COLOR = \033[0;31m
WARN_COLOR  = \033[0;33m
NO_COLOR    = \033[m

OK_STRING    = "[OK]"
ERROR_STRING = "[ERROR]"
WARN_STRING  = "[WARNING]"

test: format
	@echo "--> Running tests"
	@python manage.py test --parallel
	@echo "$(OK_COLOR)$(OK_STRING)$(NO_COLOR)"

format:
	@echo "--> Formating"
	@autopep8 --ignore=E501 -a -i $(shell find `pwd` -name "*.py")
	@echo "$(OK_COLOR)$(OK_STRING)$(NO_COLOR)"

.PHONY: format test 