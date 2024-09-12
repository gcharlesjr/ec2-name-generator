EC2 Random Name Generator 
Project Overview
This Python script generates unique EC2 instance names to help teams easily identify their resources. It’s designed for environments where multiple departments share AWS resources, ensuring that each EC2 instance has a distinct and easily identifiable name.

Features
- Allows users to input the number of EC2 instances they want names for.
- Includes department names in the generated instance names for easy identification.
- Appends random characters and numbers to ensure uniqueness.
- Provides a simple interface for generating multiple instance names in one go.


Table of Contents
- Installation
- Usage
- Example
- Contributing

Installation
Prerequisites
- Python 3.x
- Git (optional, for cloning the repository)
  
Steps

1. Clone the repository (optional): 
git clone git@github.com:<your-username>/ec2-name-generator.git
cd ec2-name-generator

2. Install dependencies (none required for this project).

Run the script:
python ec2_name_generator.py


Usage
1. Run the script: After running the script, you will be prompted to enter how many EC2 instance names you want to generate and to choose a department from a predefined list.
2. Input the number of EC2 instances: The script will ask you to input the number of names to generate.
3. Choose a department: The script will display a list of departments to choose from. You can select a department by typing the corresponding number.
4. Receive the generated names: The script will output the generated EC2 instance names based on your inputs.


Commands: python ec2_name_generator.py



Example

Enter the number of EC2 instance names to generate: 3

Available Departments:
1. Finance
2. Marketing
3. Sales
4. Engineering
5. HR
6. Operations
7. Support
8. Product
   
Select your department by entering the corresponding number: 4

Generated EC2 Names:
Engineering-a1B2c3
Engineering-XyZ9wP
Engineering-7kJ1lZ

Contributing

If you have suggestions or improvements for the project, feel free to contribute by opening issues or submitting pull requests.

