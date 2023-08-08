from models import Usuarios


def insert_user():
    user = Usuarios(cpf='07510631505', nome='Isac', data_nascimento='2000-05-26')
    print(user)
    Usuarios.save(user)


def select_user():
    user = Usuarios.query.all()
    for i in user:
        print(i)


def update_user():
    user = Usuarios.query.filter_by(cpf='07510631505').first()
    user.nome = 'Isac Kaik Oliveira Santos'
    Usuarios.save(user)


def delete_user():
    user = Usuarios.query.filter_by(cpf='4444444444').first()
    Usuarios.delete(user)


if __name__ == '__main__':
    insert_user()
    select_user()
