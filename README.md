### This repository is a part of the Assignment given by Kisanhub. The API is built using Django and Django REST framework toolkit. 
This Django app can be used to store and retrieve the weather data. The source data comes from the URL provided in the assignment doc. 

Please install the required libraries from the *requirements.txt* file.
For the databse I have used **SQLite** which is by default present in a Django project. The database is **empty**. Please fill it first using the custom command explained it point 2.
1.	I have created the data model using Django ORM to store data from the json files.
2.	Created a Custom Django management command which will fetch above json files for all locations and metrics, parse and store them in the models. The name of the command is **fetch**.

       - Instruction to run this command and fetch data for all locations and metrics: 
       
            ```python manage.py fetch``` 
       - Instruction to run this command and fetch data for specific location and metric provided as parameters:
       
            ```python manage.py fetch --metric=<METRIC_NAME> --loc=<LOCATION>``` <br>
               For example(test case):<br>
            ```python manage.py fetch --metric=Tmax --loc=UK``` <br>
          
3.  Created a REST API using Django Rest Framework which will implement HTTP GET method to deliver the weather data stored in the models.<br>

       - First start the server: <br><br>
          ```python manage.py runserver``` <br><br>
          On the localhost the URL will be like this:<br><br>
          ```http://127.0.0.1:8000/core/2/weather/?start=<START_DATE>&end=<END_DATE>&location=<LOCATION>&metric=<METRIC_NAME>&format=json```<br>
       - The **_start_** and **_end_** parameters contains date in the format YYYY-MM or YYYY-M <br>, START_DATE should be less than END_DATE
       - The **_location_** parameter can have one of the 4 values: UK, England, Scotland, Wales. <br>
       - The **_metric_** parameter can have one of the 3 values: Tmax, Tmin, Rainfall. <br>
        
       For example(test cases): <br>
       ```http://127.0.0.1:8000/core/2/weather/?start=1940-1&end=2000-2&location=UK&metric=Rainfall``` will return data in the following format:<br>
       ```{"1940-01":68.5,"1940-02":71.6,"1940-03":93.5,..... "2000-01":99.7,"2000-02":127.7}``` <br><br>
       ```http://127.0.0.1:8000/core/2/weather/?start=1910-11&end=1987-12&format=json&location=England&metric=Tmax``` will return:<br>
       ```{"1910-11":6.5,"1910-12":8.3,..... "1987-11":8.8,"1987-12":7.8}```
       
