How to run:

On build.tamu.edu, make sure numpy is installed. If not, then make sure to install it.
In the demo version that I have in the Project directory on build.tamu.edu, I already have numpy installed with a virtual environment. 

To run the program, simply activate the virtual envronment with:
source ./myenv/bin/activate

Then you can run it with:
python3 FinalProject.py

When you are done, be sure to deactivate the virtual environment with:
deactivate.




Installing numpy with a virtual environment:

Use pwd to show path to home directory.
	python3 -my venv -- without-pip /path/to/home/directory/myenv
	source ./myenv/bin/activate
	wget https://pypi.python.org/packages/source/s/setuptools/setuptools-3.4.4.tar.gz
	tar -vzxf setuptools-3.4.4.tar.gz
	cd setuptools-3.4.4
	python3 setup.py install
	cd path/to/home/directory 
	wget https://pypi.python.org/packages/source/p/pip/pip-1.5.6.tar.gz
	tar -vzxf pip-1.5.6.tar.gz
	cd pip-1.5.6
	python3 setup.py install
	cd path/to/home/directory
	deactivate
	source ./myenv/bin/activate
	python3 -m pip install --upgrade pip
	pip install numpy
	deactivate

After running pip install numpy, then numpy should be installed in the virtual environment myenv, and you can run this program with the listed steps below.
	source ./myenv/bin/activate
	python3 FinalProject.py


