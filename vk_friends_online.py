from getpass import getpass
from pprint import pprint

import vk

APP_ID = 6331864


def get_user_login():
    return '+79997912013'
    # return input('Введите логин: ')


def get_user_password():
    return '86421357Jt'
    # return getpass('Введите пароль: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friend_ids = api.friends.getOnline()
    friends = api.users.get(
        user_ids=','.join(map(str, friend_ids)),
        fields='first_name,last_name',
    )
    return friends


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print('{} {}'.format(friend['first_name'], friend['last_name']))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    print("Друзья онлайн:")
    output_friends_to_console(friends_online)
