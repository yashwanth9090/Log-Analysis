# Project 3 : Log Analysis
### by Yashwanth Manchikatla
This project is a part of Udacity [Full Stack Web Developer Nanodegree program](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## Description
In this project, a large database that could have come from a real-world web application is explored by building complex SQL queries to draw business conclusions for the data.The database contains newspaper articles, as well as the web server log for the site. This project mimics an internal reporting tool for a newpaper site to discover what kind of articles the site's readers like.

## PreRequisites
 - python 2.x
 - Vagrant
 - VirtualBox

## Project Contents
This project containes the following files:
 - articles_report.py - main python script to generate report
 - logs_output.txt - sample output file

## How to Run the Project
 - Install Vagrant and VirtualBox.
 - Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
 - Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here.
 - Unzip the data after downloading it. Inside you'll find newsdata.sql.
 - Copy the newsdata.sql and the content of this repository and put these files into vagrant directory.

## Launching the Virtual Machine
1. Launch the Vagrant by running:
```sh
$ vagrant up
```
2. Then log into this using:
```sh
$ vagrant ssh
```
## Setting up the database and creating Views
1. Change the directory to /vagrant and load the data in local database using
```sh
psql -d news -f newsdata.sql
```
2. Use ```psql -d news``` to connect to database

3. The database includes three tables:
    -  Authors table
    -  Articles table
    -  Log table

4. Create View titleViews using:
```sh
create view titleViews as select title,views from (SELECT count(*) as views, REGEXP_REPLACE(path, '.*/', '') AS path FROM log group by path) as temp join articles on articles.slug = temp.path order by views desc;
```
5. Create View authorViews using:
```sh
create view authorViews as select name, totalviews from (select author, sum(views) as totalviews from tempview group by author) as tempviews join authors on tempviews.author = authors.id order by totalviews desc;
```
6. Create View dailyViews using:
```sh
create view dailyViews as select date(time), count(*) as sum from log group by date(time) order by date;
```
7. Create View errorViews using:
```sh
create view errorViews as select date(time), count(*) as sum from log where status = '404 NOT FOUND' group by date(time) order by date;
```

## Running the queries
To execute the program, from the vagrant directory inside the virtual machine, run articles_report.py using:
```sh
$ python articles_report.py
```
