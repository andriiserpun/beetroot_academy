from django.contrib.auth.models import User, Group

user1 = User.objects.get(username="petro")
user2 = User.objects.get(username="ilarion")
group = Group.objects.get(name="test_users")

user1.groups.add(group)
user2.groups.add(group)

user1.save()
user2.save()