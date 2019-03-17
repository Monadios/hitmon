import uuid
from entity import Entity

class EntityGenerator:
    def generate_entity(self, atts):
        return Entity(uuid.uuid4(), atts)


        
