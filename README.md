# django_tutorial

1. First level tutorials
a). templates, urls, static files, view

2. Second level tutorials
a). models, database connection, register model
 python manage.py shell
>>> t = Topic(topic_name="Social Network")
>>> t.save()
>>> print(Topic.objects.all())
b). create super users 