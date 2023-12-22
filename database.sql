```sql
-- database.sql

-- Create database
CREATE DATABASE ai_adaptive_tutor;

-- Use the created database
USE ai_adaptive_tutor;

-- Create table for users
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

-- Create table for courses
CREATE TABLE courses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(255) NOT NULL,
    course_description TEXT,
    created_by INT,
    FOREIGN KEY (created_by) REFERENCES users(id)
);

-- Create table for user_courses to track user progress
CREATE TABLE user_courses (
    user_id INT,
    course_id INT,
    progress FLOAT DEFAULT 0,
    PRIMARY KEY (user_id, course_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- Create table for assessments
CREATE TABLE assessments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    course_id INT,
    assessment_name VARCHAR(255) NOT NULL,
    assessment_description TEXT,
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- Create table for user_assessments to track user performance
CREATE TABLE user_assessments (
    user_id INT,
    assessment_id INT,
    score FLOAT,
    feedback TEXT,
    PRIMARY KEY (user_id, assessment_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (assessment_id) REFERENCES assessments(id)
);

-- Create table for certifications
CREATE TABLE certifications (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    course_id INT,
    certification_name VARCHAR(255) NOT NULL,
    issue_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
```
