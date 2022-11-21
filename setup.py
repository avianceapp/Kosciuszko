def start():
    from os import system
    system('python3 -m venv kosciuszko-venv')
    system('source kosciuszko-venv/bin/activate')
    system('pip install -r requirements.txt')
    import time
    time.sleep(3)
    setup()

def create_user():
    from prompt_toolkit.shortcuts import input_dialog, message_dialog, yes_no_dialog
    from prisma.models import User

    username = input_dialog(
        title='Create an admin account',
        text='Enter a username:'
    ).run()
    email = input_dialog(
        title='Create an admin account',
        text='Enter a email:'
    ).run()

    if username is None:
        return

    password = input_dialog(
        title='Create an admin account',
        text='Enter a password:'
    ).run()

    if password is None:
        return

    User.prisma().create(data={'email': email, 'username': username, 'password': password, 'admin': True})
    message_dialog(
        title='Success',
        text='Admin account created!'
    ).run()


def setup():
    from prompt_toolkit.shortcuts import input_dialog, message_dialog, yes_no_dialog
    message_dialog(
        title='Welcome to Kosciuszko',
        text='If this is the first time you are running the setup utility. We will now connect you to the database.'
    ).run()

    message_dialog(
        title='Database connection',
        text='Kosciuszko only supports either PostgresQL or cockroachDB. Please make sure you have one of these installed & have the connection ready to go.'
    ).run()
    key = input_dialog(
        title='Database connection',
        text='Enter the database connection string:'
    ).run()

    if key is None:
        return message_dialog(title='Failure.', text='No database connection string provided.').run()

    env_writer = open('.env', 'w')
    env_writer.write(f'DATABASE_URL={key}')
    env_writer.close()
    system('prisma migrate dev --name init --preview-feature --accept-data-loss')
    
    message_dialog(
        title='Admin account',
        text='We will now create an admin account for you.'
    ).run()
    create_user()

if __name__ == '__main__':
    setup()