<!-- Create a model called User following the ERD above -->
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

<!-- Create and run the migration files to create the User table in your database -->

(django2) MacBook-Pro:single_model_orm porsheaellis$ python manage.py makemigrations
Migrations for 'users_app':
  users_app/migrations/0001_initial.py
    - Create model User
(django2) MacBook-Pro:single_model_orm porsheaellis$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, users_app
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK
  Applying users_app.0001_initial... OK

<!-- Run the shell and import your User model -->
(django2) MacBook-Pro:single_model_orm porsheaellis$ python manage.py shell
Python 3.8.3 (default, Jul  7 2020, 13:04:12) 
[Clang 11.0.3 (clang-1103.0.32.62)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from users_app.models import *

<!-- Query: Create 3 new users -->
>>> User.objects.create(first_name="Porshea", last_name="Ellis",email_address="poi08@aol.com", age="35")
<User: User object (1)>
>>> User.objects.create(first_name="Rashaud", last_name="Ellis",email_address="rash@aol.com", age="33")
<User: User object (2)>
>>> User.objects.create(first_name="Summer", last_name="Coleman",email_address="summer@aol.com", age="33")
<User: User object (3)>
>>> 
<!-- Query: Retrieve all the users -->
>>> User.objects.all()
<QuerySet [<User: User object (1)>, <User: User object (2)>, <User: User object (3)>]>

<!-- Query: Retrieve the last user -->
>>> User.objects.last()
<User: User object (3)>

<!-- Query: Retrieve the first user -->
>>> User.objects.first()
<User: User object (1)>

<!-- Query: Change the user with id=3 so their last name is Pancakes. -->

>>> c= User.objects.get(id=3)
>>> c.last_name = "Pancakes"
>>> c.save()

<!-- Query: Delete the user with id=2 from the database -->

>>> d=User.objects.get(id=2)
>>> d.delete()
(1, {'users_app.User': 1})

<!-- Query: Get all the users, sorted by their first name -->

>>> User.objects.all().values().order_by("first_name")
<QuerySet [{'id': 1, 'first_name': 'Porshea', 'last_name': 'Ellis', 'email_address': 'poi08@aol.com', 'age': 35, 'created_at': datetime.datetime(2020, 8, 16, 19, 4, 12, 299853, tzinfo=<UTC>), 'updated_at': datetime.datetime(2020, 8, 16, 19, 4, 12, 299942, tzinfo=<UTC>)}, {'id': 3, 'first_name': 'Summer', 'last_name': 'Pancakes', 'email_address': 'summer@aol.com', 'age': 33, 'created_at': datetime.datetime(2020, 8, 16, 19, 5, 15, 188986, tzinfo=<UTC>), 'updated_at': datetime.datetime(2020, 8, 16, 19, 18, 0, 343202, tzinfo=<UTC>)}]>

<!-- BONUS Query: Get all the users, sorted by their first name in descending order -->

<QuerySet [{'id': 3, 'first_name': 'Summer', 'last_name': 'Pancakes', 'email_address': 'summer@aol.com', 'age': 33, 'created_at': datetime.datetime(2020, 8, 16, 19, 5, 15, 188986, tzinfo=<UTC>), 'updated_at': datetime.datetime(2020, 8, 16, 19, 18, 0, 343202, tzinfo=<UTC>)}, {'id': 1, 'first_name': 'Porshea', 'last_name': 'Ellis', 'email_address': 'poi08@aol.com', 'age': 35, 'created_at': datetime.datetime(2020, 8, 16, 19, 4, 12, 299853, tzinfo=<UTC>), 'updated_at': datetime.datetime(2020, 8, 16, 19, 4, 12, 299942, tzinfo=<UTC>)}]>
