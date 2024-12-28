from enum import Enum

from tortoise import fields
from tortoise.models import Model

from .table import BaseTierList


class Region(Enum):
    ZCIS = "ЗСНГ"
    VCIS = "ВСНГ"


class User(Model):
    id = fields.BigIntField(pk=True)
    nickname = fields.CharField(max_length=16, null=True)
    region = fields.CharEnumField(enum_type=Region, max_length=4)
    points = fields.IntField(default=0)
    tierlists: fields.ReverseRelation["BaseTierList"]

    class Meta:
        table = "users"
