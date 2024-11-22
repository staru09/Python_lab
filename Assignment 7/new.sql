CREATE TABLE Employee (
    First_Name CHAR(20) NOT NULL,
    Last_Name CHAR(20),
    Age INT,
    Gender CHAR(1),
    Department CHAR(20),
    Income FLOAT
);

INSERT INTO Employee (First_Name, Last_Name, Age, Gender, Department, Income)
VALUES
    ('John', 'Doe', 28, 'M', 'Engineering', 60000.50),
    ('Jane', 'Smith', 32, 'F', 'Marketing', 75000.00),
    ('Sam', 'Brown', 45, 'M', 'HR', 50000.00),
    ('Lisa', 'Taylor', 30, 'F', 'Finance', 72000.00),
    ('Mike', 'Wilson', 25, 'M', 'IT', 45000.00);

SELECT * FROM Employee;
