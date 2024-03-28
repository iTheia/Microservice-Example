from providers.database import Database

postgresql = Database()

"""
  TODO: Aceptar campos especificos que no deberian ser actualizados
"""
class BaseRepository:
    def __init__(self, model_class, database=None):
        self.db = database if database else postgresql
        self.model_class = model_class

    def create(self, entity_data):
        entity = self.model_class(**entity_data)
        session = self.db.get_session()
        session.add(entity)
        session.commit()
        session.close()

    def get_all(self, pagination_options=None):
        session = self.db.get_session()
        query = session.query(self.model_class)

        if pagination_options :
            query = self._apply_filters(query, self.model_class, pagination_options)
            query = self._apply_pagination(query, pagination_options)

        entities = query.all()
        session.close()
        return entities

    def get_by_id(self, id):
        session = self.db.get_session()
        entity = session.query(self.model_class).filter_by(id=id).first()
        session.close()
        return entity

    def update(self, id, updated_entity_data):
        session = self.db.get_session()
        entity = session.query(self.model_class).filter_by(id=id).first()
        if entity:
            for key, value in updated_entity_data.items():
                setattr(entity, key, value)
            session.commit()
            session.close()

    def delete(self, id):
        session = self.db.get_session()
        entity = session.query(self.model_class).filter_by(id=id).first()
        if entity:
            session.delete(entity)
            session.commit()
            session.close()

    def _apply_pagination(self, query, pagination: dict):
        if pagination:
            limit = pagination.get('limit')
            offset = pagination.get('offset')
            query = query.offset(offset).limit(limit)
        return query

    def _apply_filters(self, query, entity_class, pagination_options = None):
        if 'filters' in pagination_options:
            for filter_data in pagination_options['filters']:
                filter_field = filter_data.get('field')
                filter_value = filter_data.get('filter')
                if hasattr(entity_class, filter_field):
                    filter_attr = getattr(entity_class, filter_field)
                    query = query.filter(filter_attr == filter_value)
        return query
