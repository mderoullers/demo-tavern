EXEC = run

all : $(EXEC)

install:
	apt-get install -y python-pip
	pip install --upgrade setuptools && pip install -U pytest && pip install tavern[pytest] && pip install colorlog
