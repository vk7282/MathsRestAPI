# Overview
## Mathematical Web Service
This application contains the REST API for three different mathematical functions as described below.

1. Factorial Number (n)      - Calculate the factorial of non-negative integer n.
2. Ackermann Function (m, n) - Calculate the value of A(m, n) with input values m and n.
3. Fibonacci Series (n)      - Calculate the nth value in fibonacci series.

I have used `FLASK` framework for quickly developing the REST APIs for these mathematical functions. 

## REST API Definition

* ***Factorial Number API*** 

`GET  /factorial/<n>`

calculates the factorial value of the non-negative integer provided by the user. See the example below.

Request - `http://localhost:5000/factorial/2`

Response - `2`

**NOTE** - Maximum number acceptable for this API is `200000`. The input greater than this will return `413` code.

* ***Fibonacci Series API*** 

`GET  /fibonacci/<n>`

calculates the nth value of fibonacci series provided by the user. See the example below.

Request - `http://localhost:5000/fibonacci/9`

Response - `21`

**NOTE** - Maximum number acceptable for this API is `200000`. The input greater than this will return `413` code.

* ***Ackermann Function API***

`GET  /ackermann/<m>/<n>`

calculates the value of A(m, n) provided m and n are non-negative integer values. See the example below.

Request - `http://localhost:5000/ackermann/1/2`

Response - `4`

**NOTE** - Since Ackermann function does a huge recursion in case of small numbers even, this can produce 
`RecursionError` exception in case of different input for m & n. I made an assumption here to handle it and 
gracefully exit the algorithm to not produce a long error traceback. 


# Development
Prerequisite
* python 3.8 or greater
* Flask

## SetUp
Create a virtual environment and use it for development and testing.

You can create virtualenv using below command and activate it.
```
virtualenv -p python3 venv

source venv/bin/activate
```
**Note:** - Make sure you have virtualenv installed in your system.

You can also create it using `python3` below command.
```
python3 -m venv venv
```

Please install the requirements from below files.
* `requirements.txt` - libraries required for production code.
* `requirements-dev.txt` - libraries required for development and test purpose.

## Installation
Install the requirements file by below commands:-
```
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

# Run

There are 2 ways to run this application. 

- *Using flask*

You can run this application using below command - 
```
flask run 
```
This will run the flask application in Development mode and can call the APIs.

- *Using Gunicorn*

you can run this application using gunicorn with parameters suitable to you. Example below- 
``` 
gunicorn --bind 0.0.0.0:5000 wsgi:app --log-level INFO
```
**NOTE** - It can take a bit of time (around 1-2 minutes) to start when you run it first time due to loading of 
the monitoring dashboard module.

# Test

I have used pytest for writing tests. All the tests for additional files are inside `tests` folder.

To run the tests, you can run the below command:-

```
pytest -v
```

To run the tests with the coverage, you can run the below command:-
```
pytest --cov=app 
```
where `app` is the application folder.

# Logging

You can find the log file named `app.log` inside `logs` folder under the project root directory. You can also 
configure/override the log path and log level using below environment variable.

* **LOG_PATH** - The path where `logs` folder should be created with the log file inside.
* **LOG_LEVEL** - This level will override the level set using gunicorn.

# Monitoring

I have used `flask_monitoringdashboard` module for basic information where you can see the request hits, request duration 
and also API performance. Once you run the application using `flask run`, the dashboard will be deployed automatically 
on the `/dashboard` endpoint. Use `admin` and `admin` as login credentials for login. 

I am also logging the time taken by mathematical algorithms in the log file for more information.

# Cloud Deployment (AWS)

You can read more details in [CLOUD_README.md](CLOUD_README.md) about how to deploy this application in AWS. 


# Assumptions
- If any string or negative integer passed to the REST API to any of the mathematical functions, it will produce a 
  400 code because of invalid input.
  
- For Fibonacci and Factorial API, the Maximum acceptable number through API is 200000. If input provided is greater 
  than this value will throw 413 status code.
  