# 1. Variables and Constants
total_score = 5  # Initialize a variable to store the current score
MAX_POINTS = 50  # Initialize a constant for the maximum possible points
total_score += 10  # Increase the total score by 10
print(f"Total Score: {total_score}, Max Points: {MAX_POINTS}")  # Display the updated score and constant

# 2. Functions
def subtract(a, b):
    return a - b  # A function to subtract two numbers

divide = lambda a, b: a / b if b != 0 else "Cannot divide by zero"  # Lambda function to divide two numbers
print(f"Subtract 10 from 15: {subtract(15, 10)}")  # Call the subtract function and print the result
print(f"Divide 10 by 2: {divide(10, 2)}")  # Call the lambda function to divide and print the result
print(f"Divide 10 by 0: {divide(10, 0)}")  # Handle division by zero

# 3. Lists (Arrays in Python)
animals = ["dog", "cat", "elephant"]  # A list of animal names
animals.insert(1, "rabbit")  # Insert "rabbit" into the second position in the list
print(f"Animals: {animals}")  # Print the updated list of animals

# 4. Dictionaries (Objects in Python)
book = {
    "title": "To Kill a Mockingbird",  # Book title
    "author": "Harper Lee",  # Book author
    "get_summary": lambda: "A novel about racism and injustice."  # Function to return a book summary
}
print(f"Book title: {book['title']}, Author: {book['author']}")  # Print book details
print(book["get_summary"]())  # Call the function to get the summary

# 5. Loops
cities = ["New York", "Los Angeles", "Chicago"]  # A list of cities
for city in cities:
    print(f"City: {city}")  # Print each city in the list

# 6. Conditional Statements
temperature = 35  # Current temperature in Celsius
if temperature > 30:
    print("It's a hot day!")  # Print if the temperature is above 30
elif temperature > 20:
    print("It's a warm day.")  # Print if the temperature is above 20 but below 30
else:
    print("It's a cold day.")  # Print if the temperature is 20 or below

# 7. File Handling (Reading and Writing)
with open("user_data.txt", "w") as file:
    file.write("Name: John\nAge: 25\nLocation: New York")  # Write some user data to a file

with open("user_data.txt", "r") as file:
    print(f"User data: {file.read()}")  # Read and display the contents of the file

# 8. User Input
age = int(input("Enter your age: "))  # Ask the user to input their age
if age >= 18:
    print("You are eligible to vote!")  # Check if the user is old enough to vote
else:
    print("Sorry, you are not eligible to vote.")  # Message if the user is too young

# 9. Basic HTTP Requests (using requests library)
import requests  # Import the requests library to make HTTP requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")  # Send a GET request to fetch posts
posts = response.json()  # Parse the JSON response to get the list of posts
print(f"First Post Title: {posts[0]['title']}")  # Print the title of the first post
