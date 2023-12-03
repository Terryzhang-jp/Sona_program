from django.apps import AppConfig


class UserPageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_page'

    def ready(self):
        import user_page.signals  # 导入信号