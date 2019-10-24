from django.apps import AppConfig

class AccountsConfig(AppConfig):
    name = 'accounts'
    
    def ready(self):
        """
        Import the signals from signals.py to trigger the profile creation functions
        """
        import accounts.signals