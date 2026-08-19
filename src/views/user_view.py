from flask_restful import Resource
from flask import request, jsonify, make_response
from src.schemas.user_schemas import (usuario_schema, usuarios_schema)
from marshmallow import ValidationError
from src.services import user_services
from src import api

class UsuarioList(Resource):
    def get(self):

        """
        Lista todos os usuários.
        ---
        tags:
            - Usuários
        responses:
            200:
                description: Lista de usuários
            404:
                description: Não existem usuários cadastrados.
        """
        usuarios = user_services.listar_usuario()

        if not usuarios:
            return make_response(jsonify({'message':'Não existem usuarios!'}), 404)

        return make_response(jsonify(usuarios_schema.dump(usuarios)), 200)

    def post(self):

        """
        Cria um novo usuário.
        ---
        tags:
            -- Usuários
        parameters:
            - in: body
            name: body
            required: true
            schema:
                type: object
                properties:
                    nome:
                        type: string
                    email:
                        type: string
                    senha:
                        type: string
                        example: senha123
        ---
        responses:
            201:
                description: Usuário criado com sucesso.
            400:
                description: Erro de validação
            409:
                description: Email já cadastrado
            

        """ 
        try:
            usuario = usuario_schema.load(request.get_json())

        except ValidationError as err:
            return err.messages, 400

        if user_services.listar_usuario_email(usuario.email):
            return {"message":"Email já cadastrado!"}, 409

        try:
            resultado = user_services.criar_usuario(usuario)

            return usuario_schema.dump(resultado), 201

        except Exception as e:
            return {
                "message":str(e)

            }, 400

api.add_resource(UsuarioList, '/usuarios')

class UsuarioResource(Resource):
    def get(self, id_usuario):

        """
        Buscar usuário por ID
        ---

        tags:
            - Usuários
        parameters:
            - name: id_usuario
              in: path
              type: integer
              required: True
        responses:
            200:
                description: Lista de Usuários
            404:
                description: Nenhum usuário encontrado
            409:
                description:

        
        """


        
        usuario = user_services.listar_usuario_id(id_usuario)
        if not usuario:
            return {
                "message":"Usuário não encontrado!"
            }, 404

        return usuario_schema.dump(usuario), 200
    
    def put(self, id_usuario):
           """
            Cadastrar um novo usuário
            ---
    
            tags:
                - Usuários
            parameters:
                - name: id_usuario
                  in: path
                  type: integer
                  required: True
                - in: body
                name: body
                required: True
                schema:
                  type: object
                  properties:
                    nome:
                      type: string
                    email:
                      type: string
                    senha:
                      type: string
            """
    try:
        novo_usuario = usuario_schema.load(request.get_json())

    except ValidationError as err:
        return err.messages, 400

    usuario = user_services.editar_usuario(
        id_usuario, {
            "nome": novo_usuario.nome,
            "email": novo_usuario.email,
            "senha": novo_usuario.senha
        }
    )

    if not usuario:
        return {"message": "Usuário não encontrado!"}, 404

    return usuario_schema.dump(usuario), 200

    def delete(self, id_usuario):

        """
        Deletar Usuário
        ---

        tags:
          - Usuário
        """
        if user_services.deletar_usuario(id_usuario):
            return {
                "message":"Usuário deletado com sucesso!"
            }, 200
        return {"message": "Usuário não encontrado!"}, 404

api.add_resource(UsuarioResource, '/usuario/<int:id_usuario>')

