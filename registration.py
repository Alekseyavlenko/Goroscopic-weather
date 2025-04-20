def save_user(username, password, goroscope):
    file_exists = os.path.isfile('data/users.csv')
    with open('data/users.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        if not file_exists:
            writer.writerow(['id', 'username', 'password', 'goroscope'])
        writer.writerow([get_next_id(), username, password, goroscope])


def get_next_id():
    if not os.path.exists('data/users.csv'):
        return 0
    with open('data/users.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        return sum(1 for _ in reader) - 1
