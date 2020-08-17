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
<!-- Query: Delete the 3 dojos you just created   -->
<!-- Query: Create 3 more dojos   -->
<!-- Query: Create 3 ninjas that belong to the first dojo   -->
<!-- Query: Create 3 ninjas that belong to the second dojo   -->
Query: Create 3 ninjas that belong to the third dojo  
Query: Retrieve all the ninjas from the first dojo  
Query: Retrieve all the ninjas from the last dojo  
Query: Retrieve the last ninja's dojo  Add a new text field called "desc" to your Dojo class  Create and run the migration files to update the table in your database. If needed, provide a default value of "old dojo"  
Query: Create a new dojo