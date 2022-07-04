## AirBnB clone
The goal of the project is to deploy on your server a simple copy of the  [AirBnB website](https://intranet.hbtn.io/rltoken/FrRTcvuF5L9wWDzFE9k01A "AirBnB website").

The web application will be composed by:

-   A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
-   A website (the front-end) that shows the final product to everybody: static and dynamic
-   A database or files that store data (data = objects)
-   An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

# The Console

##  Getting started
### Clone this repository in your computer
```
git clone https://github.com/mglssr/holbertonschool-AirBnB_clone.git
cd holbertonschool-AirBnB_clone
```
The console works in two ways:

* **Interactive mode:**
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
* And non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
## Commands

|Command | Syntax | Description |
|:---:| :---: | :----------- |
|quit| quit |Quit command to exit the program|
|EOF| *Ctrl + D\* | EOF command to exit the program |
|help| help <command\>| List all available commands with "help" (if no command is passed) or gives a short description of the command passed|
|create| create <class\>| Creates a new object.|
|show| show <class\> <id\> or <class name\>.show(<id\>)| Show information of an object|
|destroy| destroy <class\> <id\> or <class name\>.destroy(<id\>)| Deletes an object|
|all| all <class\> or <class name\>.all()| Pirnts all objects, or is an class argument is passed it only prints the objects of that class|
|update| update <class\> <id\> <attribute name\> <attribute value\> or <class name\>.update(<id\>, <attribute name\>, <attribute value\>)|Update an existing instance based on his id|
|count| <class name\>.count()| Retrieve the number of instance of a class|
  
# Examples
### create command
```
root@2a1eca11adbf:~/holbertonschool-AirBnB_clone# ./console.py
(hbnb) create BaseModel
51e3fb6b-8060-4f96-9c3a-ad3a376ee049
```
### show command
```
(hbnb) show BaseModel 51e3fb6b-8060-4f96-9c3a-ad3a376ee049
[BaseModel] (51e3fb6b-8060-4f96-9c3a-ad3a376ee049) {'id': '51e3fb6b-8060-4f96-9c3a-ad3a376ee049', 'created_at': datetime.datetime(2022, 7, 3, 18, 8, 14, 573493), 'updated_at': datetime.datetime(2022, 7, 3, 18, 8, 14, 573516)}
```
### all command
```
(hbnb) all
["[BaseModel] (f17f1adf-d3ee-47fa-8e24-4c7df9480064) {'id': 'f17f1adf-d3ee-47fa-8e24-4c7df9480064', 'created_at': datetime.datetime(2022, 7, 2, 17, 36, 48, 945207), 'updated_at': datetime.datetime(2022, 7, 2, 17, 36, 48, 945217), 'name': 'Rick Sanchez', 'my_number': 69}", "[BaseModel] (002c36ae-e9f2-4318-bc6c-5c3392398e6e) {'id': '002c36ae-e9f2-4318-bc6c-5c3392398e6e', 'created_at': datetime.datetime(2022, 7, 2, 17, 37, 18, 844669), 'updated_at': datetime.datetime(2022, 7, 2, 17, 37, 18, 844679), 'name': 'Rick Sanchez', 'my_number': 69}", "[BaseModel] (40f55b02-b57b-47a2-a45a-6bebf83b7f1c) {'id': '40f55b02-b57b-47a2-a45a-6bebf83b7f1c', 'created_at': datetime.datetime(2022, 7, 2, 17, 38, 23, 342109), 'updated_at': datetime.datetime(2022, 7, 2, 17, 38, 23, 342118), 'name': 'Rick Sanchez', 'my_number': 69}", "[BaseModel] (72e127db-f8f4-4be2-802e-8ea87f443b81) {'id': '72e127db-f8f4-4be2-802e-8ea87f443b81', 'created_at': datetime.datetime(2022, 7, 2, 17, 41, 42, 635526), 'updated_at': datetime.datetime(2022, 7, 2, 17, 41, 42, 635542), 'name': 'Rick Sanchez', 'my_number': 69}", "[BaseModel] (498745fe-6cbf-455a-895b-dcb724ba2c89) {'id': '498745fe-6cbf-455a-895b-dcb724ba2c89', 'created_at': datetime.datetime(2022, 7, 2, 17, 42, 7, 337049), 'updated_at': datetime.datetime(2022, 7, 2, 17, 42, 7, 337070), 'name': 'Rick Sanchez', 'my_number': 69}"]
```
### command count 
```
(hbnb) User.count()
21
```

## Authors
- [Kevin Fundora](https://github.com/KevinFRX)
- [Maia Iglesias](https://github.com/mglssr)
