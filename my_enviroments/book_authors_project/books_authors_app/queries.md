 <!-- Create the Book class model   -->
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

 <!-- Create the Author class model   -->
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    book_by_author = models.ManyToManyField(Book, related_name='author_book')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

 <!-- Create and run the migration files to create the tables in your database   -->
(django2) MacBook-Pro:book_authors_project porsheaellis$  python manage.py makemigrations
Migrations for 'books_authors_app':
  books_authors_app/migrations/0001_initial.py
    - Create model Book
    - Create model Author
(django2) MacBook-Pro:book_authors_project porsheaellis$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, books_authors_app, contenttypes, sessions
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
  Applying books_authors_app.0001_initial... OK
  Applying sessions.0001_initial... OK
(django2) MacBook-Pro:book_authors_project porsheaellis$ 


 <!-- Query: Create 5 books with the following names: C Sharp, Java, Python, PHP, Ruby   -->
 >>> Book.objects.create(title="C Sharp", desc="programming")
<Book: Book object (1)>
>>> Book.objects.create(title="Java", desc="programming")
<Book: Book object (2)>
>>> Book.objects.create(title="Python", desc="programming")
<Book: Book object (3)>
>>> Book.objects.create(title="PHP", desc="programming")
<Book: Book object (4)>
>>> Book.objects.create(title="Ruby", desc="programming")
<Book: Book object (5)>

 <!-- Query: Create 5 different authors: Jane Austen, Emily Dickinson, Fyodor Dostoevksy, William Shakespeare, Lau Tzu  -->

>>> Author.objects.create(first_name="Jane", last_name="Austen")
<Author: Author object (1)>
>>> Author.objects.create(first_name="Emily", last_name="Dickinson")
<Author: Author object (2)>
>>> Author.objects.create(first_name="Fyodor", last_name="Dostoevksy")
<Author: Author object (3)>
>>> Author.objects.create(first_name="William", last_name="Shakespeare")
<Author: Author object (4)>
>>> Author.objects.create(first_name="Lau", last_name="Tzu")
<Author: Author object (5)>

 <!-- Add a new text field in the authors table called 'notes'.  -->
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    note = models.CharField(max_length=255)
    book_by_author = models.ManyToManyField(Book, related_name='author_book')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

 <!-- Create and run the migration files to update the table in your database.  -->
(django2) MacBook-Pro:book_authors_project porsheaellis$  python manage.py makemigrations
You are trying to add a non-nullable field 'note' to author without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> "old books"
Migrations for 'books_authors_app':
  books_authors_app/migrations/0002_author_note.py
    - Add field note to author
(django2) MacBook-Pro:book_authors_project porsheaellis$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, books_authors_app, contenttypes, sessions
Running migrations:
  Applying books_authors_app.0002_author_note... OK
(django2) MacBook-Pro:book_authors_project porsheaellis$ 

 <!-- Query: Change the name of the C Sharp book to C#   -->
>>> change = Book.objects.get(id=1)
>>> change
<Book: Book object (1)>
>>> change.title
'C Sharp'
>>> change.title ="C#"
>>> change.save()
>>> change.title
'C#'

 <!-- Query: Change the first name of the 4th author to Bill   -->
 
>>> name_change = Author.objects.get(id=4)
>>> name_change.first_name
'William'
>>> name_change.first_name ="Bill"
>>> name_change.save()
>>> name_change.first_name
'Bill'
 Query: Assign the first author to the first 2 books 

 Query: Assign the second author to the first 3 books  

 Query: Assign the third author to the first 4 books 

 Query: Assign the fourth author to the first 5 books (or in other words, all the books) 

 Query: Retrieve all the authors for the 3rd book  

 Query: Remove the first author of the 3rd book  

 Query: Add the 5th author as one of the authors of the 2nd book 

 Query: Find all the books that the 3rd author is part of  

 Query: Find all the authors that contributed to the 5th book  

 Submit your .txt file that contains all the queries you ran in the shell