<!-- Create and run the migration files to create the tables in your database -->

(django2) MacBook-Pro:dojo_ninjas_proj porsheaellis$ python manage.py makemigrations
Migrations for 'dojo_ninjas_app':
  dojo_ninjas_app/migrations/0001_initial.py
    - Create model Dojo
    - Create model Ninja
(django2) MacBook-Pro:dojo_ninjas_proj porsheaellis$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, dojo_ninjas_app, sessions
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
  Applying dojo_ninjas_app.0001_initial... OK
  Applying sessions.0001_initial... OK
(django2) MacBook-Pro:dojo_ninjas_proj porsheaellis$ 

<!-- Run the shell and import your models -->

(django2) MacBook-Pro:dojo_ninjas_proj porsheaellis$ python manage.py shell
Python 3.8.3 (default, Jul  7 2020, 13:04:12) 
[Clang 11.0.3 (clang-1103.0.32.62)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from dojo_ninjas_app.models import *


<!-- Query: Create 3 new dojos   -->
>>> Dojo.objects.create(name="Porshea", city="Dallas", state="TX")
<Dojo: Dojo object (1)>
>>> Dojo.objects.create(name="Summer", city="Dallas", state="TX")
<Dojo: Dojo object (2)>
>>> Dojo.objects.create(name="Rashaud", city="San Jose", state="CA")

<!-- Query: Delete the 3 dojos you just created   -->
>>> d=Dojo.objects.get(id=1)
>>> d.delete()
(1, {'dojo_ninjas_app.Ninja': 0, 'dojo_ninjas_app.Dojo': 1})
>>> d=Dojo.objects.get(id=2)
>>> d.delete()
(1, {'dojo_ninjas_app.Ninja': 0, 'dojo_ninjas_app.Dojo': 1})
>>> d=Dojo.objects.get(id=3)
>>> d.delete()
(1, {'dojo_ninjas_app.Ninja': 0, 'dojo_ninjas_app.Dojo': 1})

<!-- Query: Create 3 more dojos   -->
>>> Dojo.objects.create(name="San Jose", city="San Jose", state="CA")
<Dojo: Dojo object (4)>
>>> Dojo.objects.create(name="Dallas", city="Dallas", state="TX")
<Dojo: Dojo object (5)>
>>> Dojo.objects.create(name="Oakland", city="Oakland", state="CA")
<Dojo: Dojo object (6)>

<!-- Query: Create 3 ninjas that belong to the first dojo   -->
>>> Ninja.objects.create(first_name="Porshea", last_name="Ellis", dojo_id=Dojo.objects.get(id=4))
<Ninja: Ninja object (1)>
>>> Ninja.objects.create(first_name="Rashud", last_name="Ellis", dojo_id=Dojo.objects.get(id=4))
<Ninja: Ninja object (2)>
>>> Ninja.objects.create(first_name="Elijah", last_name="Ellis", dojo_id=Dojo.objects.get(id=4))
<Ninja: Ninja object (3)>
>>> 
<!-- Query: Create 3 ninjas that belong to the second dojo   -->
>>> Ninja.objects.create(first_name="Kathy", last_name="Curry", dojo_id=Dojo.objects.get(id=5))
<Ninja: Ninja object (4)>
>>> Ninja.objects.create(first_name="Gail", last_name="Curry", dojo_id=Dojo.objects.get(id=5))
<Ninja: Ninja object (5)>
>>> Ninja.objects.create(first_name="Ava-Grace", last_name="Curry", dojo_id=Dojo.objects.get(id=5))
<Ninja: Ninja object (6)>
<!-- Query: Create 3 ninjas that belong to the third dojo   -->
>>> Ninja.objects.create(first_name="Thomas", last_name="Curry", dojo_id=Dojo.objects.get(id=6))
<Ninja: Ninja object (7)>
>>> Ninja.objects.create(first_name="Jude", last_name="Curry", dojo_id=Dojo.objects.get(id=6))
<Ninja: Ninja object (8)>
>>> Ninja.objects.create(first_name="Bob", last_name="Curry", dojo_id=Dojo.objects.get(id=6))
<Ninja: Ninja object (9)>
<!-- Query: Retrieve all the ninjas from the first dojo   -->
'Porshea'
'Ellis'
<Dojo: Dojo object (4)>
'Rashud'
'Ellis'
<Dojo: Dojo object (4)>
'Elijah'
'Ellis'
<Dojo: Dojo object (4)>
<!-- Query: Retrieve all the ninjas from the last dojo   -->
'Thomas'
'Curry'
<Dojo: Dojo object (6)>
'Jude'
'Curry'
<Dojo: Dojo object (6)>
'Bob'
'Curry'
<Dojo: Dojo object (6)>
>>> 
<!-- Query: Retrieve the last ninja's dojo   -->
>>> end.ninjas.last()
<Ninja: Ninja object (9)>
>>> end_peep = end.ninjas.last()
>>> end_peep
<Ninja: Ninja object (9)>
>>> end_peep.first_name
'Bob'
>>> end_peep.last_name
'Curry'
<!-- Add a new text field called "desc" to your Dojo class   -->
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

<!-- Create and run the migration files to update the table in your database. If needed, provide a default value of "old dojo"   -->
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> "old dojo"
Migrations for 'dojo_ninjas_app':
  dojo_ninjas_app/migrations/0003_dojo_desc.py
    - Add field desc to dojo
(django2) MacBook-Pro:dojo_ninjas_proj porsheaellis$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, dojo_ninjas_app, sessions
Running migrations:
  Applying dojo_ninjas_app.0003_dojo_desc... OK
(django2) MacBook-Pro:dojo_ninjas_proj porsheaellis$ 


<!-- Query: Create a new dojo -->

>>> Dojo.objects.create(name="Arlington", city="Arlington", state="TX", desc="old dojo")
<Dojo: Dojo object (7)>