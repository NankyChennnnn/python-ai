# Author: bibberzz
# Created: 2026/6/1 14:38
# Project: day7
# File: throw_diy_exception.py
# Description:

def get_password():
    password = input("Please input password: ")

    # 1
    # if len(password) < 8:
    #     raise Exception("Error password length.")

    # 2 assert method
    assert len(password) >= 8, "Error password length."

    return password


if __name__ == '__main__':
    try:
        get_password()
    except Exception as e:
        print(e)
