# Skills-Path AI

## Overview

Skills-Path AI is an AI-based system that helps learners generate structured learning paths for technical skills and discover related skills commonly associated with them in real industry job profiles.

The system builds a learning roadmap using skill prerequisite relationships and also analyzes job descriptions to identify skills that frequently appear together in industry roles.

This helps learners understand what to learn next and which complementary skills are commonly required in the job market.

---

## Project Aim

The aim of this project is to develop an intelligent learning assistant that:

* Generates structured learning paths based on prerequisite relationships between skills.
* Identifies complementary skills by analyzing job descriptions.
* Helps learners discover related knowledge areas that often appear together in industry roles.

---

## Features

* AI-based learning path generation
* Skill dependency graph for prerequisite relationships
* Industry skill recommendations from job descriptions
* Skill co-occurrence analysis
* Interactive web interface
* Progress tracking for completed skills

---

## Technologies Used

### Programming Language

* Python

### Framework

* Streamlit

### Libraries

* JSON
* Collections (Counter)
* Regular Expressions (re)

### AI Concepts

* Knowledge Representation using Skill Graphs
* Graph Traversal Algorithms (Depth First Search)
* Natural Language Processing (NLP)
* Skill Co-Occurrence Analysis

---

## Project Structure

```
skills-path-ai
│
├── app
│   ├── skill_graph.py
│   ├── path_generator.py
│   └── ai_skill_recommender.py
│
├── data
│   └── job_descriptions.json
│
├── app.py
├── README.md
└── requirements.txt
```

---

## How the System Works

1. The user selects a skill or learning goal.
2. The system generates a learning path using a skill dependency graph.
3. Job descriptions are analyzed using NLP techniques.
4. Skills frequently appearing together in job descriptions are identified.
5. These complementary skills are recommended to the learner.

---

## Disclaimer

* The estimated learning time is an approximate value and may vary depending on the learner's pace and prior knowledge.
* The generated learning path is based on skill prerequisite relationships and job description analysis.
* The roadmap is intended as a general guideline and may not be perfect for every learner.

---

## Learning Outcomes

Through this project we learned:

* How to represent knowledge using skill graphs
* How to implement graph traversal algorithms
* How to apply NLP to analyze job descriptions
* How to design AI-based recommendation systems
* How to build interactive applications using Streamlit

---

## Future Improvements

* Integrating real job datasets from LinkedIn or Kaggle
* Improving NLP skill extraction using TF-IDF or machine learning
* Adding visualization of skill relationships
* Providing personalized user learning profiles

---

## Author

Project developed as part of an Artificial Intelligence Fundamentals project.
