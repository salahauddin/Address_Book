# Address_Book
A FastAPI backend application with Address book that takes a distance and gives all addresses within that distance

Below is the detailed explanation of running the app on windows.

clone this repository.
Save the project at the location.
C:\Users\{user_name}\Anaconda3\Scripts


Create Virtual environment at C:\Users\{user_name}\Anaconda3\Scripts.

command to create virtual env.
env\scripts\activate

Now move to Address folder in command terminal. 
cd Address_Book\Address.

Now install all pakages.
By running the following commands.

#this is the command to upgrade pip.

python.exe -m pip install --upgrade pip

command to install all packages.
pip install FastAPI sqlalchemy geopy logging uvicorn


Once every package is installed.
run the following command to start the application.

command to run the application.
uvicorn Address.main:app --reload.
