############Description##################

A rough MVC framework for viewing data over stdin/stdout.

A routing mechanism reconciles each unique combination of inputs to a handler (a method in a controller class).  

The contollers get their data from entities declared in model classes, which use local dummy dictionaries as a read-only data source. Future versions may supply pckling objects to/from file storage. 

Controller results are assumed to be lists of dictionaries, and are routed to either a base view/formatter or a raw data view depending on the inclusion of a decorator at the controller method.  Future versions may include specifying the view name with the decorator. 


############EXAMPLES#####################


##### Show user #####
$ python main.py -u Ron
id	name
----------
2	Ron

#####Show projecst by user matching name 
$ python main.py -u Joe -p all
user_id	id	name
---------------------
1	2	Another Project


$ python main.py -u Ron -p all
user_id	id	name
---------------------
2	1	Project List

####### Show all projects #######
$ python main.py -p all
user_id	id	name
---------------------
2	1	Project List
1	2	Another Project

#######Show all users #########
$ python main.py -u all
id	name
----------
1	Joe
2	Ron
3	Ralph

