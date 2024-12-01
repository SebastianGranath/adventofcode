import os
from os import listdir
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get session cookie from environment variables
SESSION = os.getenv("SESSION")

if not SESSION:
    raise ValueError("SESSION environment variable not set!")

# Function to get the highest day folder currently present.
def get_highest_day():
    try:
        D = listdir()
    except Exception as e:
        print(f"Error listing directories: {e}")
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

# Function to create the new day's folder and files.
def next_day(high_day):
    next_day = str(int(high_day) + 1)
    new_folder = 'Day ' + next_day

    try:
        os.mkdir(new_folder)
    except FileExistsError:
        print(f"Folder {new_folder} already exists.")
        return
    except Exception as e:
        print(f"Error creating folder {new_folder}: {e}")
        return

    # Fetch input from Advent of Code
    input_url = f'https://adventofcode.com/2023/day/{next_day}/input'
    headers = {'cookie': f'session={SESSION}'}
    try:
        response = requests.get(input_url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        puzzle_input = response.text.strip()
    except requests.RequestException as e:
        print(f"Failed to fetch input for Day {next_day}: {e}")
        return

    try:
        with open(os.path.join(new_folder, next_day + '.in'), 'w') as f:
            f.write(puzzle_input)
        open(os.path.join(new_folder, next_day + '.test'), 'w').close()
        solution_script = f"""import sys
import re

with open('{next_day}.in', 'r') as f:
    D = f.read().strip()
print(D)
"""
        with open(os.path.join(new_folder, next_day + '.py'), 'w') as f:
            f.write(solution_script)
    except Exception as e:
        print(f"Error creating files in {new_folder}: {e}")
        return

    # Add a new row to the README.md
    update_readme(next_day)

# Function to update the README.md with the new day's row
def update_readme(next_day):
    readme_file = 'README.md'

    # Make sure the README file exists
    if not os.path.exists(readme_file):
        print(f"{readme_file} not found!")
        return

    # URL to the day's problem
    problem_url = f'https://adventofcode.com/2023/day/{next_day}'

    # New row for the progress table
    new_row = f"| Day {next_day} | Puzzle Title | | [Solution](https://github.com/SebastianGranath/adventofcode/blob/master/Day%20{next_day}/{next_day}.py) |\n"

    try:
        with open(readme_file, 'r') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading {readme_file}: {e}")
        return

    # Find the position to insert the new row
    table_start = None
    table_end = None
    for i, line in enumerate(lines):
        if line.strip() == "| Day  | Puzzle Title         | Difficulty  | Solution Link                                                                            |":
            table_start = i + 2  # Skip the table header
        elif table_start is not None and line.strip() == "":
            table_end = i
            break

    if table_start is None:
        print("Couldn't find the start of the progress table in README.md")
        return

    # Add the new row to the correct place
    if table_end is not None:
        lines.insert(table_end, new_row)
    else:
        lines.append(new_row)  # If no empty line was found, append to the end

    try:
        with open(readme_file, 'w') as f:
            f.writelines(lines)
    except Exception as e:
        print(f"Error writing to {readme_file}: {e}")

# Main script logic
def main():
    high_day = get_highest_day()

    if high_day == 0:
        print("No 'Day X' folders found, starting with Day 1.")
    else:
        print(f"Highest day folder found: Day {high_day}")

    next_day(high_day)

if __name__ == "__main__":
    main()
