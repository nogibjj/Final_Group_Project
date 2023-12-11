# Final_Group_Project
This is a repository for IDS 706 Final Team Project. Produced by Kelly Tong, Cassie Kang, Katherine Tian. 

## Purpose
This repository contains the microservice for a music schedule builder website application and spotify popular songs dataset exploratory analysis. These microservices interface with Azure Databricks pipeline (workspace, compute cluster, job run etc.), Azure Web App Service, and Flask app to deploy and run. We will explain these microservices in details in the sections below in thsi `READ.md` file. 
The music builder website application uses Docker to containerize images in Azure App Registry. The data exploration is done with extract, transform_load, query and python data exploratory packages such as pandas and matplotlib. It is then clone in Azure Databricks workspace to run jobs on the pipeline.


## Architecture

![Architecture](https://github.com/nogibjj/Final_Group_Project/assets/142815940/1760fca3-381a-4f2c-930a-bd9d3b32cf1e)


## Key Components of the Repository
- ``.devcontainer`` includes a Dockerfile and devcontainer.json.
                The 'Dockerfile' within this folder specifies how the container should be built

- ``workflows`` includes CI.yml, which contain configuration files for setting up automated build, test, and deployment pipelines

- ``.gitignore`` is used to specify which files or directories should be excluded from version control when using Git.

- ``Makefile`` is a configuration file used in Unix-based systems for automating tasks and building software. It contains instructions and dependencies for compiling code, running tests, and other development tasks.

- ``README.md`` is the instruction file for the readers.

- ``main.py`` is a Python file. This specific main.py includes the functions for the Flask App. 

- ``requirements.txt`` is to specify the dependencies (libraries and packages) required to run the project.

- ``test_main.py`` is a test file for main.py

- ``templates`` folder includes all the templates for the app
  
- ``static`` includes the necessary files which are downloadede
  
- ``Dockerfile``is provided to containerize the Flask app

- ``mylib``folder contains the exploratory functions for analyzing the spotify dataset `lib.py`, and the `extract.py` for extracting the dataset from an url and `query.py` for performing queries on the dataset. 

## Github Actions CI/CD
Github actions are used to test the Makefile commands and the pipeline as well. The Status badges for Lint, Install, Format and CI action in general are included here. 
[![Lint](https://github.com/nogibjj/Final_Group_Project/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Final_Group_Project/actions/workflows/lint.yml)
[![install](https://github.com/nogibjj/Final_Group_Project/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Final_Group_Project/actions/workflows/install.yml)
[![Format](https://github.com/nogibjj/Final_Group_Project/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Final_Group_Project/actions/workflows/format.yml)
[![CI](https://github.com/nogibjj/Final_Group_Project/actions/workflows/CI.yml/badge.svg)](https://github.com/nogibjj/Final_Group_Project/actions/workflows/CI.yml)

Example Github Action for Test
<img width="926" alt="截屏2023-12-10 17 37 39" src="https://github.com/nogibjj/Final_Group_Project/assets/142815940/5a04cda0-9e02-43cc-ae7c-01c6cccb7aa1">

## Data Exploration Dataset
The dataset used in this project is from Kaggle, which contains 300000 Spotify songs. It is originally from Spotify via the spotifyr package. For each song, there are 24 variables, including track id, name, artist, popularity, danceability etc. The spotify dataset can be found in `spotify_song.csv`. 


## Research Questions - Data Exploration
- What is the highest popularity track in the dataset?
- Which genre of music are the most popular?
- Trends in popularity - Does releasing a song at a certain month of a year, lead to higher popularity?
## Data Exploration Visualization and Analysis

![popularity_distribution](https://github.com/nogibjj/Final_Group_Project/assets/143833511/a15396fa-ac96-4775-8cee-4b4452d6b081)

The popularity distribution plot shows overall the tracks' popularity follow a normal distribution with a mean around 55. Yet there is an exception that large amounts of tracks fall into 0 popularity. 
After sorting the tracks by popularity, we found out Dance Monkey by Tones and I has the highest popularity among all songs on Spotify, with a popularity score at 100. 

![genre_popularity](https://github.com/nogibjj/Final_Group_Project/assets/143833511/65bd2479-5767-455d-ae82-7ffffc316f92)

From our analysis, we can see that among all genres, pop is the most popular, followed by latin. And we found that Edm is the least popular genre on Spotify. 

![monthly_popularity](https://github.com/nogibjj/Final_Group_Project/assets/143833511/256e3f96-4ff2-4cf4-9796-dd4b1c263d36)

The plot depicting the average track popularity over the months indicates a general upward trend as the year progresses. The tracks released in November tend to have the highest average popularity. This could be attributed to a rise in people's leisure time and engagement with relaxing activities, particularly music, during the holiday seasons.



## App Demonstration
APP can be found here: [MusicScheduleBuilder](http://myfinalschedule.kindground-9784b48c.westus2.azurecontainerapps.io)

<img width="895" alt="截屏2023-12-10 17 54 33" src="https://github.com/nogibjj/Final_Group_Project/assets/142815940/8b5f9857-b9c6-47e5-9064-a09d3c41ac59">


## App Functionality
**Build a schedule for listening to popular spotify music:** This app helps to build schedule for listening to popular spotify music. Users can input their desired music songs, and the schedule builder will be able to return a daily schedule for the user. The schedule will be able to return the exact time suitable for listening to the music without interfering with the user's other essential to-dos. 

## Load Test - Quantitative Assessment
We use `Locust` test to load test for our Flask app. This is a useful platform for testing web application. It helps us assess how our web application handles increased requests. 
The code for running Locust test in stored in `locustfile.py`. 
To run this, use `pip install locust` to install locust on codespace or local machine. 
Then run `locust` command to run the web version locust test. This can be used within the link provided by running the command. 

<img width="1133" alt="截屏2023-12-10 17 11 26" src="https://github.com/nogibjj/Final_Group_Project/assets/142815940/0263d2ea-a347-4ea2-9acb-fe0d8af0db39">

Loaded Tests: 
<img width="1504" alt="截屏2023-12-10 17 05 21" src="https://github.com/nogibjj/Final_Group_Project/assets/142815940/e2f75883-0519-442f-b3d0-b71a540c4fa4">

<img width="1505" alt="截屏2023-12-10 17 05 27" src="https://github.com/nogibjj/Final_Group_Project/assets/142815940/2fd443c2-d107-4b6e-b965-0d03e929ff4a">

<img width="1509" alt="截屏2023-12-10 17 05 31" src="https://github.com/nogibjj/Final_Group_Project/assets/142815940/b5eb9496-4e54-427a-b033-97d960da2b3e">

Load test on Locust is set to test 10000 requests per second. We adjust the matrices for number of users and Spawn rate (users started/second) to get the response rate. 
The computed results as shown in the statistical plots above are good for now. As response time reaches more than 10,000 ms for both 50th and 95th percentile. 
Total requests per second reach about more than 400 requests per second as well. 

## Preparation and Setup Web Application (Flask App)
1. clone the repository
2. modify requirements.txt file to contain the necessary packages
3. use `pip install Flask` to install Flask on codespace
4. use `brew update && brew install azure-cli` to install azure-cli locally
5. login to Azure locally using "az login"
6. Build an image locally using `docker build --tag myfinalschedule .`
<img width="882" alt="截屏2023-12-10 13 24 45" src="https://github.com/nogibjj/Individual_Project4_Kelly_Tong/assets/142815940/69b0a2ad-5235-42a9-acf0-ce7ab18baaf5">
   
7. Build a container locally using `docker run --detach --publish 5000:50505 myfinalschedule`
   
<img width="813" alt="截屏2023-12-10 13 23 46" src="https://github.com/nogibjj/Individual_Project4_Kelly_Tong/assets/142815940/3cefbe70-78f2-411a-94c5-f628336ad08b">

8. Create an App on Azure using `az containerapp up --resource-group myfinalschedule --name myfinalschedule --ingress external --target-port 50505 --source .` This will first create the resource group, run the same line again to create the flask app.
   
<img width="1141" alt="截屏2023-12-10 13 27 10" src="https://github.com/nogibjj/Individual_Project4_Kelly_Tong/assets/142815940/8e25f88f-a7e4-4a2c-a759-d0ae1fca894f">

<img width="1395" alt="myfinalschedule" src="https://github.com/nogibjj/Individual_Project4_Kelly_Tong/assets/142815940/1ecf7aae-4e4b-4b94-a0b5-1dd72205dc6e">


10. Set API_TOKEN in environment variable 
11. Use the Flask App as demonstrated in App usage below
12. App can be viewed in Azure Container and image can be viewed in container registry which are both in Azure Web Portal

## App Usage
1. Click plan your day
2. Input the daily to-dos with the daily essentials and desired spotify music

<img width="1525" alt="截屏2023-12-10 18 02 07" src="https://github.com/nogibjj/Final_Group_Project/assets/142815940/51383da2-34cd-4c5f-ad0a-787769b3efac">

3. Click Generate Schedule
4. A Planned schedule with a planned time to listen to the desired spotify music will be shown

<img width="1041" alt="截屏2023-12-10 18 36 34" src="https://github.com/nogibjj/Final_Group_Project/assets/142815940/0e42267d-43ff-462e-ad21-30928d8fcb4a">

## Dockerization

Docker is used to containerize the microservice including the container for resource group and the images used in web application. Dockerfile in this repository provides the details process for building and running the Docker container as well as installing the required dependencies. 

<img width="1256" alt="截屏2023-12-10 13 34 56" src="https://github.com/nogibjj/Individual_Project4_Kelly_Tong/assets/142815940/a18f81eb-42d7-4ed7-bee8-a17dcf994275">

The image "myfinalschedule" is stored in Azure APP Registry. It is automatically stored when the command line `az containerapp up --resource-group myfinalschedule --name myfinalschedule --ingress external --target-port 50505 --source .` is run for the second time.

## Azure Databricks Job Run
Action of our CI/CD Pipeline is also tested through job run on Azure Databricks. Dataset and the entire Github repository is cloned in Azure Databricks workspace. A compute cluster is then created for the workspace as well as for the designed job run pipeline. This pipeline is designed to test all the python files in `mylib` folder, which are the essential files containing data exploration, extract and query. 

<img width="1331" alt="截屏2023-12-10 18 42 34" src="https://github.com/nogibjj/Final_Group_Project/assets/142815940/2b05d6a8-90e6-4484-872f-1f379a4cde24">


## AI Usage
In this project, we have utilized knowledge learnt throughout the semester on AI tools. Particularly, we used Github Copilot, Azure Databricks Workspace AI tools and ChatGPT 4. GitHub Copilot, Databricks Workspace AI tools, and ChatGPT can form a powerful trio in streamlining a data engineering project for a team. GitHub Copilot aids developers by suggesting code snippets and entire functions, improving productivity and potentially reducing bugs by providing contextually relevant code based on the comments and code being written. Databricks Workspace offers a collaborative environment with integrated AI tools, enabling data scientists and engineers to build, train, and deploy machine learning models efficiently, leveraging Apache Spark’s big data processing capabilities. It simplifies the management of infrastructure and provides robust tools for data exploration and visualization. ChatGPT can assist the team in generating documentation, writing code, and even debugging by offering conversational insights into code structure and logic. The synergy of these tools can lead to a more cohesive development cycle, enhance the team's ability to tackle complex data problems, foster innovation, and significantly cut down on development time.

### Requirements
Your team project should include the following:

* Microservice

Build a microservice that interfaces with a data pipeline. You can choose Python or Rust for development. The microservice should include logging and be containerized using the Distroless Docker image. A Dockerfile must be included in your repository.

* Load Test

The microservice must be capable of handling 10,000 requests per second. A load test verifying this performance should be included.

* Data Engineering

Your project should involve the use of a library specializing in data engineering such as Spark, Pandas, SQL, a vector database, or any other relevant library.

* Infrastructure as Code (IaC)

Your project must utilize an IaC solution for infrastructure setup and management. You can choose among AWS CloudFormation, AWS SAM, AWS CDK, or the Serverless Framework.

√ Continuous Integration and Continuous Delivery (CI/CD)

Implement a CI/CD pipeline for your project. It could be through GitHub Actions or AWS Cloud Build or any other relevant tool.

* README.md

A comprehensive README file that clearly explains what the project does, its dependencies, how to run the program, its limitations, potential areas for improvement, and how AI Pair Programming tools (GitHub Copilot and one more tool of your choice) were used in your development process.

* Architectural Diagram

A clear diagram representing the architecture of your application should be included in your project documentation.

√ GitHub Configurations

Your GitHub repository must include GitHub Actions and a .devcontainer configuration for GitHub Codespaces. This should make the local version of your project completely reproducible. The repository should also include GitHub Action build badges for install, lint, test, and format actions.

* Teamwork Reflection

Each team member should submit a separate 1-2 page management report reflecting on the team's functioning according to the principles discussed in your teamwork book. This report should not be part of the GitHub README but rather a separate document. It should include a peer evaluation in which each team member is graded on their performance, stating three positive attributes and three areas for improvement as the basis for the grade. Note that each student will share the teamwork reflection with their team and discuss it in a session before turning in the report. The outcome of this feedback session must be included in the report for full credit.

* Quantitative Assessment

The project must include a quantitative assessment of its reliability and stability. You must use data science fundamentals to describe system performance, e.g., average latency per request at different levels of requests per second (100, 1000, etc.). ❓ Think of the software system as a data science problem that needs to be described using data science principles.

* Demo Video

A YouTube link in README.md showing a clear, concise walkthrough and demonstration of your application, including the load test and system performance assessment.

* Team Size and Makeup

The team should consist of 3-4 people, ideally composed of 1-2 strong programmers and 1-2 quantitative storytellers.

### Grading Rubric

Microservice (20%)
Implementation of the microservice: 10 points

Use of logging: 5 points
Proper containerization with Distroless: 5 points

Load Test (20%)
Successful load test at 10,000 requests/second: 20 points

Data Engineering (10%)
Effective use of a data engineering library: 10 points

Infrastructure as Code (IaC) (10%)
Correct setup and management of infrastructure using IaC: 10 points

Continuous Integration and Continuous Delivery (CI/CD) (10%)
Proper implementation of a CI/CD pipeline: 10 points

README.md (10%)
Clarity and comprehensiveness of README.md: 5 points
Explanation of AI Pair Programming tool usage: 5 points

Architectural Diagram (5%)
Quality and clarity of the architectural diagram: 5 points

GitHub Configurations (5%)
GitHub Actions + GitHub Codespaces .devcontainer configuration: 5 points

Final Team Presentation (15%)
Quality and clarity of presentation: 10 points
Team's ability to effectively answer questions and discuss the project: 5 points

Teamwork Reflection (5%)
Quality and sincerity of reflection: 3 points
Reflection includes peer evaluation with three positive attributes and three areas for improvement: 2 points

Total: 100%

Please run the below code to access the web app:
```
uvicorn app:app --reload --host 0.0.0.0 --port 5000
```
