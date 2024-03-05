import os
import re

class Task8:

    # ----task 8----
    #  1: Check if file exists before reading
    def check_file(file_path):
        if not os.path.exists(file_path):
            # Create the file in a subfolder of your choice
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                f.write('This is a new file.')

    #  2: Read names of users into a generator
    def read_users(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                yield line.strip()

    #  3: Read user names into an array excluding 10% of users
    def read_users_exclude_10(file_path):
        with open(file_path, 'r') as f:
            users = [line.strip() for line in f]

        excluded_users_count = int(len(users) * 0.1)
        excluded_users = users[:excluded_users_count]
        remaining_users = users[excluded_users_count:]

        return remaining_users

    #  4: Read users of even rows
    def read_even_users(file_path):
        with open(file_path, 'r') as f:
            users = [line.strip() for i, line in enumerate(f) if i % 2 == 0]

        return users

    #  5: Check email addresses and addresses for correctness
    def check_email_addresses(file_path):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

        addresses_regex = r'^\d+\s\w+\s\w+'

        email_addresses = []
        addresses = []

        with open(file_path, 'r') as f:
            for line in f:
                if re.match(email_regex, line.strip()):
                    email_addresses.append(line.strip())
                elif re.match(addresses_regex, line.strip()):
                    addresses.append(line.strip())

        return email_addresses, addresses

    #  6: Get Gmail email addresses
    def get_gmail_addresses(email_addresses):
        gmail_addresses = list(filter(lambda x: x.endswith('@gmail.com'), email_addresses))
        return gmail_addresses

    #  7: Check if each email address is complex from the username
    def complex_check(email, username):
        pass

    def check_complexity(email_addresses, usernames):
        results = []
        for email, username in zip(email_addresses, usernames):
            if complex_check(email, username):  # Replace with your own complexity check function
                results.append(True)
            else:
                results.append(False)
        return results

    #  8: Check user's name in the list, convert to different formats, and count 'A's
    def check_user_name(user_name, user_list):
        user_name = user_name.lower()
        ascii_codes = [ord(char) for char in user_name]
        reversed_name = user_name[::-1]
        num_a = user_name.count('a')

        if user_name in user_list:
            return True, ascii_codes, reversed_name, num_a
        else:
            return False, ascii_codes, reversed_name, num_a

    #  9: Convert variable names to uppercase
    variable_names = ['var1', 'var2', 'var3']
    variable_names = [name.upper() for name in variable_names]

    #  10: Calculate total payment for customer groups
    def calculate_total_payment(customers):
        total_payment = sum([200 if customer % 8 == 0 else 250 for customer in customers])
        return total_payment


# הרצת main ל task 8
file_path = 'UsersEmail.txt'
check_file(file_path)
users_generator = read_users(file_path)
users = read_users_exclude_10(file_path)
even_users = read_even_users(file_path)
email_addresses, addresses = check_email_addresses(file_path)
gmail_addresses = get_gmail_addresses(email_addresses)
email_addresses_1 = ['user1@example.com', 'user2@example.com']
email_addresses_2 = ['user3@example.com', 'user4@example.com']
usernames = ['user1', 'user2', 'user3', 'user4']
results = check_complexity(email_addresses_1 + email_addresses_2, usernames)
user_name = 'John'
user_list = ['john', 'jane', 'jack']
found, ascii_codes, reversed_name, num_a = check_user_name(user_name, user_list)
total_payment = calculate_total_payment([5, 19, 43, 4, 88, 76, 15, 15])

# הדפסות של התוצאות
print(users)
print(even_users)
print(email_addresses)
print(addresses)
print(gmail_addresses)
print(results)
print(found, ascii_codes, reversed_name, num_a)
print(variable_names)
print(total_payment)
