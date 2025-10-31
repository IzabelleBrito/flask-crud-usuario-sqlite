from flask import Blueprint, request, jsonify
from ..extensions import db
from ..services.user_service import UserService
from flasgger import swag_from

users_bp = Blueprint('users', __name__)


@users_bp.route('/users', methods=['GET'])
@swag_from({'summary': 'Lista todos os usuários',
    'responses': {
        200: {
            'description': 'Lista de usuários',
            'schema': {
                'type': 'array',
                'items': {'$ref': '#/definitions/User'}
            }
        }
    }
})
def get_users():
    """Retorna a lista de todos os usuários"""
    users = UserService.get_all()
    return jsonify([user.to_dict() for user in users])


@users_bp.route('/users/<int:user_id>', methods=['GET'])
@swag_from({
    'summary': 'Detalhes de um usuário',
    'parameters': [
        {
            'name': 'user_id',
            'in': 'path',
            'type': 'integer',
            'required': True
        }
    ],
    'responses': {
        200: {
            'description': 'Detalhes do usuário',
            'schema': {'$ref': '#/definitions/User'}
        },
        404: {'description': 'Usuário não encontrado'}
    }
})
def get_user(user_id):
    """Retorna os detalhes de um usuário específico"""
    try:
        user = UserService.get_by_id(user_id)
        return jsonify(user.to_dict())
    except ValueError:
        return jsonify({'error': 'Usuário não encontrado'}), 404


@users_bp.route('/users', methods=['POST'])
@swag_from({
    'summary': 'Cria um novo usuário',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'example': 'João Silva'},
                    'email': {'type': 'string', 'example': 'joao@email.com'},
                    'password': {'type': 'string', 'example': '123456'}
                },
                'required': ['name', 'email', 'password']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Usuário criado com sucesso',
            'schema': {'$ref': '#/definitions/User'}
        },
        400: {'description': 'Dados inválidos'}
    }
})
def create_user():
    """Adiciona um novo usuário"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'JSON requerido'}), 400

        user = UserService.create(data)
        return jsonify(user.to_dict()), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Erro interno do servidor'}), 500


@users_bp.route('/users/<int:user_id>', methods=['PUT'])
@swag_from({
    'summary': 'Atualiza um usuário',
    'parameters': [
        {
            'name': 'user_id',
            'in': 'path',
            'type': 'integer',
            'required': True
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'email': {'type': 'string'},
                    'password': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Usuário atualizado',
            'schema': {'$ref': '#/definitions/User'}
        }
    }
})
def update_user(user_id):
    """Atualiza os dados de um usuário existente"""
    try:
        user = UserService.get_by_id(user_id)
        data = request.get_json()
        if not data:
            return jsonify({'error': 'JSON requerido'}), 400

        updated_user = UserService.update(user, data)
        return jsonify(updated_user.to_dict())
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Erro interno do servidor'}), 500


@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
@swag_from({
    'summary': 'Remove um usuário',
    'parameters': [
        {
            'name': 'user_id',
            'in': 'path',
            'type': 'integer',
            'required': True
        }
    ],
    'responses': {
        204: {'description': 'Usuário removido com sucesso'},
        404: {'description': 'Usuário não encontrado'}
    }
})
def delete_user(user_id):
    """Remove um usuário"""
    try:
        user = UserService.get_by_id(user_id)
        UserService.delete(user)
        return '', 204
    except ValueError:
        return jsonify({'error': 'Usuário não encontrado'}), 404