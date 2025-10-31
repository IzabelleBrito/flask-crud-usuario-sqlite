from ..extensions import db
from ..models.user import User
from sqlalchemy.exc import IntegrityError


class UserService:
    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def get_by_id(user_id):
        user = User.query.get(user_id)
        if not user:
            raise ValueError(f"Usuário com ID {user_id} não encontrado")
        return user

    @staticmethod
    def create(data):
        # Validações
        if not User.validate_email(data.get('email', '')):
            raise ValueError("Email inválido")
        if not data.get('name', '').strip() or len(data['name'].strip()) < 2:
            raise ValueError("Nome deve ter pelo menos 2 caracteres")
        if not data.get('password') or len(data['password']) < 6:
            raise ValueError("Senha deve ter pelo menos 6 caracteres")

        # Cria usuário SEM senha
        user = User(
            name=data['name'].strip(),
            email=data['email'].lower().strip()
        )
        user.set_password(data['password'])

        try:
            db.session.add(user)
            db.session.commit()
            return user
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Email já cadastrado")

    @staticmethod
    def update(user, data):
        if 'name' in data:
            if len(data['name'].strip()) < 2:
                raise ValueError("Nome deve ter pelo menos 2 caracteres")
            user.name = data['name'].strip()

        if 'email' in data:
            if data['email'] != user.email and not User.validate_email(data['email']):
                raise ValueError("Email inválido")
            if data['email'] != user.email:
                # Verifica duplicidade
                existing = User.query.filter(User.email == data['email'].lower().strip()).first()
                if existing:
                    raise ValueError("Email já cadastrado")
            user.email = data['email'].lower().strip()

        if 'password' in data:
            if len(data['password']) < 6:
                raise ValueError("Senha deve ter pelo menos 6 caracteres")
            user.set_password(data['password'])

        db.session.commit()
        return user

    @staticmethod
    def delete(user):
        db.session.delete(user)
        db.session.commit()
