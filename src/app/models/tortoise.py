from tortoise.models import Model
from beartype import beartype
from tortoise.fields import TextField, DatetimeField


class TextSummary(Model):
    url = TextField()
    summary = TextField()
    created_at = DatetimeField(auto_now_add=True)

    @beartype
    def __str__(self) -> str:
        return self.url
