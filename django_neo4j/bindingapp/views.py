from django.http import HttpResponse
from .models import Person

def create_person(request):
    # Create a new person
    person = Person(name="John Doe", age=30).save()
    return HttpResponse(f"Person {person.name} created.")

def get_person(request, name):
    # Get a person by name
    person = Person.nodes.get(name=name)
    return HttpResponse(f"Person: {person.name}, Age: {person.age}")

def update_person(request, name):
    # Update a person's age
    person = Person.nodes.get(name=name)
    person.age = 31
    person.save()
    return HttpResponse(f"Person {person.name} updated.")

def delete_person(request, name):
    # Delete a person
    person = Person.nodes.get(name=name)
    person.delete()
    return HttpResponse(f"Person {person.name} deleted.")