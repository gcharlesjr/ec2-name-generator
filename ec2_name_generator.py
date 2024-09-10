import random
import string

def generate_random_string(length=6):
    """Generate a random string of letters and digits."""
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def generate_ec2_names(department, count):
    """Generate unique EC2 names based on department and random strings."""
    ec2_names = []
    for i in range(count):
        random_suffix = generate_random_string()
        ec2_name = f"{department}-{random_suffix}"
        ec2_names.append(ec2_name)
    return ec2_names

def main():
    # Get user input for number of EC2 instances and department name
    try:
        count = int(input("Enter the number of EC2 instance names to generate: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    
    department = input("Enter the name of your department: ").strip()

    # Generate EC2 names
    ec2_names = generate_ec2_names(department, count)

    # Print the unique EC2 names
    print("\nGenerated EC2 Names:")
    for name in ec2_names:
        print(name)

if __name__ == "__main__":
    main()
