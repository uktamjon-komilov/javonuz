from django.contrib.auth.models import UserManager as BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, *args, **kwargs):
        user = self.model(username=username)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user