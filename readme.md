[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17278532)
# Workshop 8 - Testing and File I/O

Navigate to this codespace. 

## Todays Objectives:

-   Practice writing and running unit tests
-   Gain experience with file I/O operations
-   Learn to work with CSV files in Python

## Part One - Basic Unit Testing with pytest


Create a new Python file called `calculator.py`

In `calculator.py` create the basic functions of add, subtract, multiply and divide, with each of them taking two arguments and returning the output . e.g.

```python
def something(a, b):
	output = a do something with b
	return output
```
Once you have fleshed that out, create a new file called `test_calculator.py` and write unit tests for each function in `calculator.py`. Use the `assert` statement and include tests for both normal cases and edge cases (like division by zero). 

Run your tests using the `pytest` framework. If you haven't installed pytest, you can do so using pip:

```python
pip install pytest
```
Run your tests by executing:

```python 
pytest test_calculator.py
```
Fix any failing tests and ensure all tests pass.

[What it should Look like](https://imgur.com/a/gGfM5Jb)

If you are feeling adventurous expand the functionality of your calculator!

For a little further reading, have a look here : https://learn.microsoft.com/en-us/training/modules/test-python-with-pytest/2-pytest-basics

## Part Two - File Input and Output

1.  Create a new Python file called `student_manager.py`.
2.  Implement the following functions:
a. `add_student(name, age, grade)`: Appends a new student's information to a file called `students.txt`.
b. `display_students()`: Reads and displays all students from `students.txt`.
c. `find_student(name)`: Searches for a student by name in `students.txt` and returns their information.
3.  Test your functions by adding a few students, displaying the list, and finding a specific student. You can do this basic test without having to expand out to a full test_student_mananger file. 

## Part 3: CSV Handling 

1.  Create a new Python file called `csv_handler.py`.
2.  Implement the following functions using the `csv` module:

	a. `write_to_csv(data)`: Writes a list of dictionaries to a CSV file called `data.csv`.
	b. `read_from_csv()`: Reads the `data.csv` file and returns a list of dictionaries.
	c. `sort_csv_by_column(column_name)`: Reads `data.csv`, sorts the data by the specified column, and writes the sorted data back to the file.
3.  Test your functions by creating some sample data, writing it to a CSV, reading it back, and sorting it. You can do this basic test without having to expand out to a full test_csv_handler file.
```python 
# Example Sample data to write to CSV Feel free to make your own. 
data =  [ 
		{"name":  "Rupert",  "age":  "20",  "grade":  "A"}, 
		{"name":  "Emma",  "age":  "21",  "grade":  "B"}, 
		{"name":  "Charlie",  "age":  "19",  "grade":  "C"}
]
```


## Part 4: Challenge 

Combine the concepts from Parts 1-3 to create a simple grade book application:

1.  Create a `GradeBook` class that uses CSV to store student grades.
2.  Implement methods to add students, record grades, and calculate averages.
3.  Write unit tests for your `GradeBook` class.
