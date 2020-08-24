Download the folder off of github
The requirements.txt file contains all the dependencies this app needs
Go into the app folder and enter the following command:

Command: pip3 install -r requirements.txt

Run the command

Note: You will need to use python3

This app runs in a virtual environment. I have used it to ensure it does not affect the packages installed for other projects

Command: source env/bin/activate

Run the command to start the virtual environment

###Data Used
I intented to implement a form to add data to the database, but due to time constraints, I used dummy data

###Database
The database used for this app is PostgreSQL. I used PSQL because I found it to be suitable for this project in terms of performance.
When using flask, it is used with an ORM layer to manage it.
My reasons for using PSQL:
- It supports JSON data
- It is a relational database which provides structure for the type of data collected in this usecase
Note: As the data collected varies, PSQL may experience replication of data due to multiple tables.

***Scalability***
To make this solution cloud-scalable, I would dockerize the app. It would make deployments more organized and better managed. I could use Kubernetes to deploy multiple containers and configure the scalability. This gives better control based on usage. When the usage reaches a set threshold the containers scale up, when the usage is low containers can be terminated.
This discussion would overlap with the database selection criteria. If there is significant analytical and operational workloads, I would suggest looking into a cloud NOSQL database such as Google BigTable. Its design is better suited with a storage engine for machine learning applications while offering low latency.

###Deployment
This app could be deployed using Heroku and a Gunicorn server.

###Comments
If I had more time, and a substantial portion of sample data, I would have used pandas to analyze, read and write data to the database.

###Error Handling
I have not implemented error handling methods. This is mandatory, however, I had to skip due to time constraints.