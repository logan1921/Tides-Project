DFO Water Level Download
==============================

This python script was developed to download water levels from the DFO API. 

Getting Started
------------
Initialize a new git repository:

`git init`  

Ensure you have Python 3.10 or greater installed`  

https://www.python.org/downloads/

In the folder you have cloned the git repository, open up Windows Power Shell. Start a virtual environment with python by using the command (in this case `py` refers to python):

`py -m venv env`  

This will open a virtual environment where all of your packages can be independently downloaded and used over your own personal site-packages of python libraries. If you are using a Windows machine, activate the virtual environment by using the command:

`.\env\Scripts\activate`

Install all of the dependencies with pip by using the requirements.txt file:

`py -m pip install -r requirements.txt`

Now you can run the intended python script to download DFO water levels. Use the command:

`py grab_Tides_data.py`
