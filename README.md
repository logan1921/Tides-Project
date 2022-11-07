DFO Water Level Download
==============================

This python script was developed to download water levels from the DFO API. The script will bring up a small gui that will allow the user to input a StationIDI and Start Year and End Year to download water levels.

Getting Started
------------
Ensure you have Python 3.10 or greater installed - otherwise you will run into installation errors with python modules(pandas)  

https://www.python.org/downloads/

As well ensure you have GIT installed

https://git-scm.com/downloads


Code Example
------------
In the folder you want to work in, open **cmd.exe** in admin mode and clone the local repository:

`git clone https://github.com/logan1921/Tides-Project`  

.Then start a virtual environment with python by using the command (in this case `py` refers to python):

`py -m venv env`  

This will open a virtual environment where all of your packages can be independently downloaded and used over your own personal site-packages of python libraries. If you are using a Windows machine, activate the virtual environment by using the command:

`.\env\Scripts\activate`

Change directories to 'Tides-Project

`cd ./Tides-Project`

Install all of the dependencies with pip by using the requirements.txt file:

`py -m pip install -r requirements.txt`

Now you can run the intended python script to download DFO water levels. Use the command:

`py grab_Tides_data.py`

When you are finished with the script, deactivate the environment by typing the command:

`deactivate`
