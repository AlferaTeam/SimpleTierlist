from tortoise import fields
from tortoise.models import Model


class BaseTierList(Model):
    user = fields.ForeignKeyField("models.User", related_name="tierlists")

    class Meta:
        abstract = True


class SwordTierList(BaseTierList):
    tier = fields.CharField(max_length=3, null=True)

    class Meta:
        table = "sword_tierlist"


class VanillaTierList(BaseTierList):
    tier = fields.CharField(max_length=3, null=True)

    class Meta:
        table = "vanilla_tierlist"


class NetheriteTierList(BaseTierList):
    tier = fields.CharField(max_length=3, null=True)

    class Meta:
        table = "netherite_tierlist"
