from flask_restful import Resource
from flask import request, jsonify, make_response
from marshmallow import ValidationError

from src import api
from src.schemas.registro_schemas import registro_schema, registros_schema
from src.services import registro_services


class RegistroList(Resource):
    def get(self):
        """
        Lista todos os registros.
        ---
        tags:
            - Registros
        responses:
            200:
                description: Lista de registros
            404:
                description: Nenhum registro cadastrado
        """
        registros = registro_services.listar_registros()

        if not registros:
            return make_response(jsonify({'message': 'Não existem registros!'}), 404)

        return make_response(jsonify(registros_schema.dump(registros)), 200)

    def post(self):
        """
        Cria um novo registro.
        ---
        tags:
            - Registros
        parameters:
            - in: body
              name: body
              required: true
              schema:
                type: object
                properties:
                    tipo:
                        type: boolean
                    fk_produto:
                        type: integer
        responses:
            201:
                description: Registro criado com sucesso
            400:
                description: Erro de validação
        """
        try:
            registro = registro_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        try:
            resultado = registro_services.criar_registro(registro)
            return registro_schema.dump(resultado), 201
        except Exception as e:
            return {"message": str(e)}, 400


class RegistroResource(Resource):
    def get(self, id_registro):
        """
        Busca um registro por ID.
        ---
        tags:
            - Registros
        parameters:
            - name: id_registro
              in: path
              type: integer
              required: true
        responses:
            200:
                description: Registro encontrado
            404:
                description: Registro não encontrado
        """
        registro = registro_services.buscar_registro(id_registro)
        if not registro:
            return {"message": "Registro não encontrado!"}, 404

        return registro_schema.dump(registro), 200

    def put(self, id_registro):
        """
        Atualiza um registro.
        ---
        tags:
            - Registros
        parameters:
            - name: id_registro
              in: path
              type: integer
              required: true
            - in: body
              name: body
              required: true
              schema:
                type: object
                properties:
                    tipo:
                        type: boolean
                    fk_produto:
                        type: integer
        responses:
            200:
                description: Registro atualizado
            404:
                description: Registro não encontrado
        """
        try:
            novo_registro = registro_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400

        registro = registro_services.atualizar_registro(id_registro, {
            "tipo": novo_registro.tipo,
            "fk_produto": novo_registro.fk_produto
        })

        if not registro:
            return {"message": "Registro não encontrado!"}, 404

        return registro_schema.dump(registro), 200

    def delete(self, id_registro):
        """
        Deleta um registro.
        ---
        tags:
            - Registros
        parameters:
            - name: id_registro
              in: path
              type: integer
              required: true
        responses:
            200:
                description: Registro deletado com sucesso
            404:
                description: Registro não encontrado
        """
        if registro_services.deletar_registro(id_registro):
            return {"message": "Registro deletado com sucesso!"}, 200
        return {"message": "Registro não encontrado!"}, 404


api.add_resource(RegistroList, '/registros')
api.add_resource(RegistroResource, '/registro/<int:id_registro>')
