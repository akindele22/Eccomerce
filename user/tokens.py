from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

class AccountActivatorTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self,user,timestamp):
        return(
            six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.Account.email_confirmed)
        )
account_activator = AccountActivatorTokenGenerator()