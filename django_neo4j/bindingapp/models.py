from neomodel import StructuredNode, StringProperty, RelationshipTo, UniqueIdProperty , IntegerProperty

class Country(StructuredNode):
    code = StringProperty(unique_index=True, required=True)

class City(StructuredNode):
    name = StringProperty(required=True)
    country = RelationshipTo('Country', 'FROM_COUNTRY')

class Person(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)
    country = RelationshipTo('Country', 'IS_FROM')
    city = RelationshipTo('City', 'LIVES_IN')