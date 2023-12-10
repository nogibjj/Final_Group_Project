# Final_Group_Project
This is a repository for IDS 706 Final Team Project. Produced by Kelly Tong, Cassie Kang, Katherine Tian. 

## Purpose
This repository

## Github Actions CI/CD
[![Lint](https://github.com/nogibjj/Final_Group_Project/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Final_Group_Project/actions/workflows/lint.yml)
[![install](https://github.com/nogibjj/Final_Group_Project/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Final_Group_Project/actions/workflows/install.yml)
[![Test](https://github.com/nogibjj/Final_Group_Project/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Final_Group_Project/actions/workflows/test.yml)

## Research Questions
- What is the highest popularity track in the dataset?
- Which genre of music are the most popular?
- Trends in popularity - Does releasing a song at a certain month of a year, lead to higher popularity?

## App Demonstration
APP can be found here: [MusicScheduleBuilder](http://myfinalschedule.kindground-9784b48c.westus2.azurecontainerapps.io)

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
