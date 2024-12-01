import os
from os import listdir
from datetime import datetime

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
        os.mkdir(new_folder)
    except FileExistsError:
        print(f"Folder {new_folder} already exists.")
        return
    except Exception as e:
        print(f"Error creating folder {new_folder}: {e}")
        return

    try:
        with open(os.path.join(new_folder, next_day + '.in'), 'w') as f:
            f.write("# puzzle_input")
        open(os.path.join(new_folder, next_day + '.test'), 'w').close()
        solution_script = f"""import sys
import re
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('{next_day}.in', 'r') as f:
    D = f.read().strip()
print(D)
"""
        with open(os.path.join(new_folder, next_day + '.py'), 'w') as f:
            f.write(solution_script)
    except Exception as e:
        print(f"Error creating files in {new_folder}: {e}")
        return

    update_readme(year_folder, next_day)

# Function to update the README.md with the new day's row
def update_readme(year_folder, next_day):
    readme_file = os.path.join(year_folder, 'README.md')

    if not os.path.exists(readme_file):
        print(f"{readme_file} not found!")
        return

    problem_url = f'https://adventofcode.com/{year_folder.split("/")[-1]}/day/{next_day}'
    new_row = f"| Day {next_day} | Puzzle Title | | [Solution](https://github.com/SebastianGranath/adventofcode/blob/master/{year_folder}/Day%20{next_day}/{next_day}.py) |\n"

    try:
        with open(readme_file, 'r') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading {readme_file}: {e}")
        return

    table_start = None
    table_end = None
    for i, line in enumerate(lines):
        if line.strip() == "| Day  | Puzzle Title         | Difficulty  | Solution Link                                                                            |":
            table_start = i + 2
        elif table_start is not None and line.strip() == "":
            table_end = i
            break

    if table_start is None:
        print("Couldn't find the start of the progress table in README.md")
        return

    if table_end is not None:
        lines.insert(table_end, new_row)
    else:
        lines.append(new_row)

    try:
        with open(readme_file, 'w') as f:
            f.writelines(lines)
    except Exception as e:
        print(f"Error writing to {readme_file}: {e}")

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
