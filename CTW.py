from json import load, dump
from sys import argv
from requests import post, get
from bs4 import BeautifulSoup

username, password = str(), str()


def show_menu():
    print('''
            Welcome to this SCRIPT coded by DOD

    -D  : Log in with your default user         (1)
    -C  : Log in with your custom user          (2)
    -I  : Insert new Login Data                 (3)
    -cD : Change Default Login User             (4)
    -E  : Edit Login data username or password  (5)
    -lo : Log out                               (6)
    -A  : Show all users                        (7)
    -S  : Show status                           (8)
    ''')


def show_login_datas(login_datas: dict):
    for login_data in login_datas.items():
        print("%s.  UName : ( %8s ) , PWord : ( %12s ) , User : %s  %s" %
              (login_data[0].upper(), login_data[1]["username"], login_data[1]["password"],login_data[1]["info"],login_data[1]["flag"]))


def set_user_data(login_datas: dict, chosen_user: str):
    global u_username, u_password
    for login_data in login_datas.items():
        if login_data[0] == chosen_user:
            u_username = login_data[1]["username"]
            u_password = login_data[1]["password"]

    return u_username, u_password


def save_data(new_data: dict):
    with open('login_data.json', 'w') as w:
        dump(new_data, w)


def connection_check(username, password):
    text = post('http://wifi.shahroodut/login',
                data='dst=&popup=true&username=%s&password=%s' % (username, password))
    error = BeautifulSoup(text.text, "html.parser")
    try:
        error = error.find(
            'div', attrs={'class': "error"}).find('div')
    except:
        pass
    return error.string


def get_id(login_datas: dict):
    global maximum
    for index, data in enumerate(login_datas.items()):
        maximum = max(int(index), int(index + 1))+1
    return maximum


def connect():
    res = connection_check(username, password)
    if res is None:
        print('You are logged in with ( %s )' % username)
    else:
        print("Message : %s" % res)


args = argv[1:]

if len(args) != 0 and args[0] == '--help':
    show_menu()
    exit()
with open('login_data.json', 'r') as f:
    primary_login_data = load(f)
    if primary_login_data["1"]["username"] is None:
        primary_login_data["1"]["username"] = input(
            "Enter Your Default-User UserName : \n")
        primary_login_data["1"]["password"] = input(
            "Enter Your Default-User password : \n")
        primary_login_data["1"]["info"] = input(
            "Enter Your Default-USer Info : \n")
        show_menu()
        print("Your Default user set. Run Script again to use utilities.\n")
        with open('login_data.json', 'w') as w:
            dump(primary_login_data, w)
        exit()

username = primary_login_data["1"]["username"]
password = primary_login_data["1"]["password"]

try:
    if args[0] == '1' or args[0] == '-D':
        connect()
    elif args[0] == '2' or args[0] == '-C':
        show_login_datas(primary_login_data)
        user = input("\nUser to login with ?\n")
        username, password = set_user_data(primary_login_data, user)
        connect()
    elif args[0] == '3' or args[0] == '-I':
        n_username = input("Enter Your New UserName : \n")
        n_password = input("Enter Your New password : \n")
        n_info = input("Enter Your New User info : \n")
        new_id = get_id(primary_login_data)
        with open('login_data.json', 'r') as f:
            data = load(f)
            data[new_id] = {'username': n_username, 'password': n_password,'info':n_info,'flag':''}
            save_data(data)
    elif args[0] == '4' or args[0] == '-cD':
        show_login_datas(primary_login_data)
        change_id = input('Set user as default : \n')
        primary_login_data["1"]["username"], primary_login_data[change_id][
            "username"] = primary_login_data[change_id]["username"], primary_login_data["1"]["username"]
        primary_login_data["1"]["password"], primary_login_data[change_id][
            "password"] = primary_login_data[change_id]["password"], primary_login_data["1"]["password"]
        primary_login_data["1"]["info"], primary_login_data[change_id][
            "info"] = primary_login_data[change_id]["info"], primary_login_data["1"]["info"]
        save_data(primary_login_data)
    elif args[0] == '5' or args[0] == '-E':
        show_login_datas(primary_login_data)
        change_id = input('Which user to edit data : \n')
        change_data = int(input('Edit :\n1. UserName\n2. PassWord\n'))
        if change_data == 1:
            new_username = input('Enter new UserName : \n')
            primary_login_data[change_id]["username"] = new_username
            save_data(primary_login_data)
        elif change_data == 2:
            new_password = input('Enter new PassWord : \n')
            primary_login_data[change_id]["password"] = new_password
            save_data(primary_login_data)
        else:
            print("Wrong Income...")
    elif args[0] == '6' or args[0] == '-lo':
        get('http://wifi.shahroodut/logout?')
        print("Logged out succusfuly...")
    elif args[0] == '7' or args[0] =='-A':
        show_login_datas(primary_login_data)
    elif args[0] == '8' or args[0] == '-S':
        primary_login_data = get('http://wifi.shahroodut/status').text
        index = primary_login_data.find('Welcome')
        if index == -1:
            error = connection_check(username, password)
            if error is not None:
                print(error)
            else:
                print('You are log out')
        else:
            print('You are log in with ( %s )' %
                  primary_login_data[index + 8:index + 16])
    else:
        print("use --help handle to run correct commands.")
except:
    print("use --help handle to run correct commands.")
