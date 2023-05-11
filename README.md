# Address_Book
A FastAPI backend application with Address book that takes a distance and gives all addresses within that distance

> 1) Cloning and running the app.
Below is the detailed explanation of running the app on windows.

--- clone this repository.

clone the repository at the location run this command in Git CMD.
> cd C:\Users\{user_name}\Anaconda3\Scripts

command to clone rpository in Git CMD.
> git clone https://github.com/salahauddin/Address_Book


Now in command terminal.
Create Virtual environment at C:\Users\{user_name}\Anaconda3\Scripts.
> cd C:\Users\{user_name}\Anaconda3\Scripts

command to create virtual env.
> env\scripts\activate

Now move to Address folder in command terminal. 
> cd Address_Book\Address

Now install all pakages.
By running the following commands.

#this is the command to upgrade pip.

> python.exe -m pip install --upgrade pip

command to install all packages.
> pip install FastAPI sqlalchemy geopy logging uvicorn


Once every package is installed.
run the following command to start the application.

command to run the application.
> uvicorn Address.main:app --reload

The FastAPI Swagger UI can be accessed at the link
>http://127.0.0.1:8000/docs



> 2) Functionality of the application

the base cordinates with which the application calculates distance is 12.910592, 77.630669.

>post method of this application creates an address record with latitudes and longitutes.
>Get method can fetch address with respect the distance from the base cordinates.
>Patch method updates the record for the specified ID.
>Delete method deletes the address of the specified ID.

a logfile is added at the project directory level at \Address_Book\Address\ for all logs to be registered.
