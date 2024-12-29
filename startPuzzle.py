import os, re
import requests
from os import listdir
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Set the base directory of your project (root directory)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Function to get the current year
def get_current_year():
    return str(datetime.now().year)

# Function to get the folder for the current year (checks if it exists and avoids redundant folder creation)
def get_year_folder(year):
    return os.path.join(BASE_DIR, year)

# Function to get the highest day folder currently present in the year's directory
def get_highest_day(year_folder):
    try:
        D = listdir(year_folder)
    except Exception as e:
        print(f"Error listing directories in {year_folder}: {e}")
        return 0

    high_day = 0
    for el in D:
        if el.startswith('Day '):
            try:
                day_number = int(el.split(' ')[1])
                high_day = max(high_day, day_number)
            except ValueError:
                print(f"Skipping invalid day folder: {el}")
    return high_day

# Function to create the new day's folder and files
def next_day(year_folder, high_day):
    next_day = str(int(high_day) + 1)
    new_folder = os.path.join(year_folder, 'Day ' + next_day)

    try:
        os.makedirs(new_folder, exist_ok=True)
    except Exception as e:
        print(f"Error creating folder {new_folder}: {e}")
        return

    # Create input and test files
    try:
        # Fetch puzzle input
        #puzzle_input = ' '
        puzzle_input = get_puzzle_input(next_day)
        with open(os.path.join(new_folder, next_day + '.in'), 'w') as f:
            f.write(puzzle_input)

        # Fetch test input (for now this is a placeholder)
        test_input = get_test_input(next_day)
        with open(os.path.join(new_folder, next_day + '.test'), 'w') as f:
            f.write(test_input)

        # Create solution script
        solution_script = f"""import sys, re, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('{next_day}.test', 'r') as f:
    D = f.read().strip()
print(D)
"""
        with open(os.path.join(new_folder, next_day + '.py'), 'w') as f:
            f.write(solution_script)
    except Exception as e:
        print(f"Error creating files in {new_folder}: {e}")
        return

# Function to retrieve the puzzle input from Advent of Code
def get_puzzle_input(day):
    year = get_current_year()
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    
    # Use your session cookie here
    session_cookie = os.getenv('SESSION_COOKIE')  # Replace with your session cookie
    headers = {'Cookie': f"session={session_cookie}"}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text.strip()  # Return the puzzle input
        else:
            print(f"Error fetching puzzle input for day {day}: {response.status_code}")
            return "# Error fetching input"
    except Exception as e:
        print(f"Error fetching puzzle input: {e}")
        return "# Error fetching input"

# Function to generate or fetch the test input (for now we use a simple template)
def get_test_input(day):
    year = get_current_year()
    url = f'https://adventofcode.com/{year}/day/{day}'

    session_cookie = os.getenv('SESSION_COOKIE')  # Replace with your session cookie
    headers = {'Cookie': f"session={session_cookie}"}

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(response.text.strip())

            # Match the first <code> tag and extract its content
            match = re.search(r'<code>(.*?)</code>', response.text.strip(), flags=re.DOTALL)

            if match:
                code_content = match.group(1)  # Extract the content inside the first <code> tag
                print(code_content)
            else:
                print("No <code> tag found.")

            return code_content  # Return the puzzle input
        else:
            print(f"Error fetching puzzle input for day {day}: {response.status_code}")
            return "# Error fetching input"
    except Exception as e:
        print(f"Error fetching puzzle input: {e}")
        return "# Error fetching input"
    
    print(response)
    input()
    
    # Placeholder for test input; you can modify this to fetch real test data if necessary
    test_input_template = f"""# Test input for Day {day}
# Modify this as needed to match the problem's example inputs

# Test case 1
sample_test_case_1 = 'your_input_here'

# Test case 2
sample_test_case_2 = 'another_input_here'
"""
    return test_input_template

# Main script logic
def main():
    year = get_current_year()
    year_folder = get_year_folder(year)

    try:
        os.makedirs(year_folder, exist_ok=True)
    except Exception as e:
        print(f"Error creating year folder {year_folder}: {e}")
        return

    high_day = get_highest_day(year_folder)
    if high_day == 0:
        print(f"No 'Day X' folders found for {year}, starting with Day 1.")
    else:
        print(f"Highest day folder found for {year}: Day {high_day}")

    next_day(year_folder, high_day)

if __name__ == "__main__":
    main()
