from getpass import getpass
import vk

APP_ID = 6331864


def get_user_login():
    return input('Введите логин: ')


def get_user_password():
    return getpass('Введите пароль: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    friends = api.friends.get(order='name', fields='online', name_case='nom')
    return [friend for friend in friends if friend['online'] == 1]


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print('{} {}'.format(friend['first_name'], friend['last_name']))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    print("Друзья онлайн:")
    output_friends_to_console(friends_online)
