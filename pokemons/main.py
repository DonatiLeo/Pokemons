from database import ManageData
from menu import Menu


def main():
    manage_data = ManageData()
    manage_data.insert_into_table()
    menu = Menu()
    menu.ask_account()


if __name__ == '__main__':
    main()
