# Address_Book
A FastAPI backend application with Address book that takes a distance and gives all addresses within that distance

Below is the detailed explanation of running the app on windows

clone this repository
Save the project at the location C:\Users\{user_name}\Anaconda3\Scripts
Create Virtual environment at  C:\Users\{user_name}\Anaconda3\Scripts

To create virtual env use env\scripts\activate

Now move to Address folder in command terminal 
cd Address

Now install all pakages.
By running the following commands.

#this is to upgrade pip 
python.exe -m pip install --upgrade pip

pip install FastAPI
pip install sqlalchemy
pip install geopy
pip install logging
pip install uvicorn

Once every package is installed
run the following command to start the application
uvicorn Address.main:app --reload
