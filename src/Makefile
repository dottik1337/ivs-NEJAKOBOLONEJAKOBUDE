CC=python3
DEPENDECIES=python3-pyqt5 python3-pytest

#packing
DIRECTORY=..
REPO_FILE=xgallo06_xpaska05_xhalas14.zip

all:
	sudo apt install $(CC)
	sudo apt install $(DEPENDECIES)

test:
	pytest test.py

doc:
	doxygen Doxyfile

run:
	$(CC) kalkulacka.py

profile:
	$(CC) profiler.py <stddev_samples/vstup1.txt >../profiling/vystup1.txt
	$(CC) profiler.py <stddev_samples/vstup2.txt >../profiling/vystup2.txt
	$(CC) profiler.py <stddev_samples/vstup3.txt >../profiling/vystup3.txt

pack:
	@zip -r $(DIRECTORY)/$(REPO_FILE) $(DIRECTORY) -x@$(DIRECTORY)/$(GITIGNORE)

clear:
	@rm -rf ./build
	@rm -rf ./dist
	@rm -f kalkulacka.spec

pyinstall:
	@pyinstaller kalkulacka.py
