CC=python3
DEPENDECIES=python3-pyqt5 python3-pytest

#packing
DIRECTORY=..
REPO_FILE=xgallo06_xpaska05_xhalas14.zip

all:
	sudo apt install $(CC)
	sudo apt install $(DEPENDECIES)

test:
	$(CC) test.py

doc:
	@echo "to be added"

run:
	$(CC) kalkulacka.py

profile:
	@echo "to be added"

pack:
	@zip -r $(DIRECTORY)/$(REPO_FILE) $(DIRECTORY) -x@$(DIRECTORY)/$(GITIGNORE)
	
clean:
	@echo "to be added"

