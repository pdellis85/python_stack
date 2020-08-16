(django2) MacBook-Pro:single_model_orm porsheaellis$ python manage.py shell
Python 3.8.3 (default, Jul  7 2020, 13:04:12) 
[Clang 11.0.3 (clang-1103.0.32.62)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from users_app.models import *
>>> User.objects.create(first_name="Porshea", last_name="Ellis",email_address="poi08@aol.com", age="35")
<User: User object (1)>
>>> User.objects.create(first_name="Rashaud", last_name="Ellis",email_address="rash@aol.com", age="33")
<User: User object (2)>
>>> User.objects.create(first_name="Summer", last_name="Coleman",email_address="summer@aol.com", age="33")
<User: User object (3)>
>>> 
>>> User.objects.all()
<QuerySet [<User: User object (1)>, <User: User object (2)>, <User: User object (3)>]>
>>> User.objects.last()
<User: User object (3)>
>>> User.objects.first()
<User: User object (1)>
>>> c= User.objects.get(id=3)
>>> c.last_name = "Pancakes"
>>> c.save()
>>> d=User.objects.get(id=2)
>>> d.delete()
(1, {'users_app.User': 1})
>>> User.objects.all().values().order_by("first_name")
<QuerySet [{'id': 1, 'first_name': 'Porshea', 'last_name': 'Ellis', 'email_address': 'poi08@aol.com', 'age': 35, 'created_at': datetime.datetime(2020, 8, 16, 19, 4, 12, 299853, tzinfo=<UTC>), 'updated_at': datetime.datetime(2020, 8, 16, 19, 4, 12, 299942, tzinfo=<UTC>)}, {'id': 3, 'first_name': 'Summer', 'last_name': 'Pancakes', 'email_address': 'summer@aol.com', 'age': 33, 'created_at': datetime.datetime(2020, 8, 16, 19, 5, 15, 188986, tzinfo=<UTC>), 'updated_at': datetime.datetime(2020, 8, 16, 19, 18, 0, 343202, tzinfo=<UTC>)}]>
<QuerySet [{'id': 3, 'first_name': 'Summer', 'last_name': 'Pancakes', 'email_address': 'summer@aol.com', 'age': 33, 'created_at': datetime.datetime(2020, 8, 16, 19, 5, 15, 188986, tzinfo=<UTC>), 'updated_at': datetime.datetime(2020, 8, 16, 19, 18, 0, 343202, tzinfo=<UTC>)}, {'id': 1, 'first_name': 'Porshea', 'last_name': 'Ellis', 'email_address': 'poi08@aol.com', 'age': 35, 'created_at': datetime.datetime(2020, 8, 16, 19, 4, 12, 299853, tzinfo=<UTC>), 'updated_at': datetime.datetime(2020, 8, 16, 19, 4, 12, 299942, tzinfo=<UTC>)}]>
