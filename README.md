# Final_Group_Project
This is a repository for IDS 706 Final Team Project. Produced by Kelly Tong, Cassie Kang, Katherine Tian. 

## Research Questions
- What is the highest rated movie of all time?
- Which genre of music are the most popular?
- Trends in popularity - Does releasing a song at a certain month of a year, lead to higher popularity?

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
