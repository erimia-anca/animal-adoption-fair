## ✦ Animal Adoption Fair Form
This project is a simple animal adoption request system built using Bash CGI scripts and a MySQL database.

### ✦ About the project
The project demonstrates how a web application can communicate with background processes using a named pipe (FIFO).

The main goal was to create a small but functional web application while practicing Linux system programming concepts.

### ✦ Technologies

  ♡ Bash

  ♡ CGI (Common Gateway Interface)

  ♡ HTML & CSS

  ♡ MySQL
  
  ♡ Named Pipe (FIFO)
  
  ♡ Linux
  
  ♡ Apache HTTP Server

## ✦ Features

  ♡ Animal selection
  
  ♡ Adoption request form the users can fill in
  
  ♡ Asynchronous request processing
  
  ♡ Background worker
  
  ♡ The worker records its activity in worker.log
  

## ✦ The process

The project started by setting up the CGI scripts and creating the adoption form. When a user submits a request, the data is sent through a named pipe to a background worker.

The worker processes the request, inserts it into the MySQL database, and logs the operation in worker.log. The project was built step by step, starting with the web interface and ending with the inter-process communication and database integration.

## ✦ What I learned

Through this project, I learned more about:
  
  ♡ Bash scripting
  
  ♡ coproc
  
  ♡ Pipes
  
  ♡ Receive HTTP requests
  
  ♡ Read POST data
  
  ♡ Background processing
  
  ♡ Database integration
  

## ✦ Possible improvements
  ♡ The application should validate the user's name and age
  
  ♡ Use a database for animals in MySQL
  
  ♡ Improve error handling

## ✦ Future improvements

  ♡ A future version could include an administration panel

  ♡ Users could create accounts and track their adoption requests

  ♡ Each request could have a status such as pending, approved, rejected and completed

## ✦ Video

[https://github.com/user-attachments/assets/9e4f8f83-a056-499d-86ee-88924dec0738](https://github.com/user-attachments/assets/19078577-68da-437c-99ab-ac1bfaa0d484)



