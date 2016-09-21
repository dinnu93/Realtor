# Status log

## 19/09/16

1. Input to the script is the list of **city names** followed by a **state code**. Eg: **San Francisco, CA**.
2. Url-format of search planning to use for maximum entries in a page based on city name.
   * *http://www.realtor.com/realestateandhomes-search/City-Name_State-Code>/pg-Page-Number?pgsz=50*
3. The script substitutes the city name and state code and keeps incrementing the page numbers till the end.
   from each page numbered webpage gather the link on the View-Details buttons and fetch the webpage and
   extract the data points of interest and store it in a database
4. Data Points planning to be scrapped
   * The last section of url path is the uniquely identifying factor the site already uses.
   * Address, No.of.Beds, No.of.Baths, Listing Agent, Listing Broker
   * Open House, Overview, All data points in the Key Facts section, All data points in Features section.
5. As most of the data points may or may not exist for each listing, so planning to use NoSql kind of database like **mongodb** or **Elastic Search**.
6. Just tested grabbing basic webpages with python in realtor.com it didn't give any error pages like some websites.
   So for now I can use basic python libraries rather than using selenium based data extraction to look like a human.
7. Currently just worrying about code that runs on **single core**.
8. Have to run the script like a chron job everyday to sync up the updates.

## 20/09/16

1. After reading a lot of stuff I finally decided to use **MySQL** as I already know the types of all the data points I'm going to gather.
2. I'm still a little bit worried about the performance of MySQL in a distributed setting.
   At this point I don't have a lot of experience in using databases in large projects,
   but I've to start somewhere and **RDBMS** seem to be a good starting point for beginners.
3. ORM I choose is **SqlAlchemy** due to its framework independent nature and good documentation.
4. I experimented a bit with SqlAlchemy.
5. Trying to figure out the database design.

## 21/09/16

1. Spent some time on reviewing the relational databases concepts from this [course](https://www.udacity.com/course/intro-to-relational-databases--ud197).
2. Came up with a [schema](https://drive.google.com/open?id=1KDjOMj_BeyNZMog2_m-l8hFSVd8iUNPHB-qJkV5zH3I) using (street address,city,county,state) as primary key .
3. Installation and setup : MySQL, mysql-python connector, SqlAlchemy.
4. Went through sqlalchemy documentation to setup initial table.
5. Wrote some trivial code to test sqlalchemy.
