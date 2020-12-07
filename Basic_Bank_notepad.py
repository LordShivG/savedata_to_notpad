# =========================================================================================
# As a beginner, This is my first project. Add any data to notepad in list format.
# But for practicing on project based problems, I choose this project for banking purpose.

def name():  # Define Name
    return [str(input('Enter Your Name : '))]


def mobile_no():  # Add phone No
    return [str(input('Enter Your Mobile No : '))]


def atm_pin():  # Add/ Generate ATM Pin
    return [int(input('Your ATM Pin : '))]


def money_in_account():  # Deposite
    return [float(input('Add Money In Account : '))]


def date_of_birth():  # DOB
    return [str(input('DOB in DD/MM/YYYY : '))]


def to_add_to_Bank_data():  # append all data in list, in list
    main_list = []
    total_entries = int(input('Total Entries You Want To Make = '))
    for i in range(0, total_entries):
        for j in range(i, 1 + i):
            sub_list = [name(), mobile_no(), atm_pin(), money_in_account(), date_of_birth()]
            main_list.append(sub_list)
            j += 1
        i += 1
    print(main_list)
    with open('Bank_data.txt', 'a') as bd:  # Save data to notepad
        for listitem in main_list:
            bd.write('%s\n' % listitem)


to_add_to_Bank_data()  # Calling final function
