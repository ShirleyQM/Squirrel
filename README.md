# Squirrel
This is my final project.
#### Group 29 Miao Qi(mq2237)

## Introduction
This app is used to track the information and location of squirrels in the Central Park of New York. 
The app is called sightings. You can use it to view the information of squirrels. It also allows you to insert or update the data. Plus, statistics about the squirrel will bring a lot of fun.


All required files are in this repository.
- Source code
- README
- requirements.txt
- .gitignore

## Detail
### Homepage
This page is the index. You can go to anywhere you like: Squirrel Map, Squirrel sightings, Add a squirrel's information or Squirrel Statistics.

### Squirrel Map
This map shows the location of squirrels in our database. It might be a little bit dense.

### Squirrel sightings
On this page, you can see entries about squirrels including ID and Date. For more details, please refer to the link: "details or update". This link will bring you to an editable detail page.
You can also add a new squirrel through the button on the top.

### Add a new squirrel
Find a new squirrel? Do not hesitate to track it now. You can go to this page through the homepage or 'Squirrel sightings'.

### Squirrel Statistics
This page shows some facts about the squirrel. 

## About my project
Files in /sightings are models, views, urls, templates and urls.
Other configuration files are in /project.
There may be something different in my hw from the requirement.
- I did not deploy it because I met a lot of trouble. However, it runs well on my vm. I am sorry about that.
- When building models, I set some fields to be not-null through selection box. For example, the 'Age' field has 3 choices: 'Adult', 'Juvenile', 'Unknown'. 
- When importing data, I found the original csv downloaded from the link is duplicated. So I remove the duplicated ones. I also add some test cases.

I am still not familiar with all these development tools. There might be some mistakes. But software development is interesting. Hope I can do better the next time.
