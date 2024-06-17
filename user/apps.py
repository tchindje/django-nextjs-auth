from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user"
    label = "user"

    # # launch the logic when django start
    # def ready(self) -> None:
    #     print(f"app {self.name} running in core.user.app.py ...")
    #     return super().ready()
