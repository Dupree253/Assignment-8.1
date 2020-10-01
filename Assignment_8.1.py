import os
import os.path
import time


def user_dir_file():
    user_dir = input("Please enter a directory to save a file in: ")
    user_file = None
    if os.path.exists(user_dir):
        user_file = input("Please enter the name of the file you want to save in the specified directory: ")
    else:
        os.makedirs(user_dir)
        print("Although the specified directory did not exist, I went ahead and created it for you!")
        print("------------------------")
        time.sleep(1.5)
        user_file = input("Please enter the name of the file you want to save in the specified directory: ")
        time.sleep(1.5)
        print("Processing...")
        time.sleep(1)
        print("------------------------")
        time.sleep(1.5)

    write_to_file(user_dir, user_file)
    return user_dir, user_file


def write_to_file(user_dir, user_file):
    print("Please enter the following information to be written to the specified file: ")
    print("------------------------")
    user_name = input("Name: ")
    user_address = str(input("Address: "))
    user_phone_num = str(input("Phone number: "))
    print("------------------------")
    time.sleep(1.5)
    print("Processing....")
    print("------------------------")
    time.sleep(1)

    with open(user_file, 'w') as f:
        f.write(user_name)
        f.write(user_address)
        f.write(user_phone_num)

    f = open(user_file, "r")
    if f.mode == "r":
        contents = f.read()
        print("Please verify the data below:")
        print("")
        time.sleep(1.5)
        print(contents)

    f.close()


if __name__ == '__main__':
    user_dir_file()
