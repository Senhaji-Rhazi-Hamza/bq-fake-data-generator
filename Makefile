
clean: clean_pyc

clean_pyc:
	find . -name "*pyc" -exec rm -f {} \;
