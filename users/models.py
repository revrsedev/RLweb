from django.contrib.auth.models import User

class CustomUser(User):
    class Meta:
        proxy = True

    def get_reliable_full_name(self):
        # Returns the full name, or username if full name is not available
        full_name = self.get_full_name()
        return full_name if full_name else self.username