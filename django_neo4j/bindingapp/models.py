from django_neo4j.models import NodeModel, StringProperty
# Create your models here.


class Person(NodeModel):
    name = StringProperty()
    age = IntegerProperty()