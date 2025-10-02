from datetime import datetime
from enum import Enum

from passlib.hash import bcrypt
from tortoise import fields, models


class UserRole(str, Enum):
    ANON = "anon"
    TEMP = "temp"
    STANDARD = "standard"
    ADMIN = "admin"
    SUPERUSER = "superuser"

class UserTier(str, Enum):
    FREE = "free"
    PRO = "pro"
    BASIC = "basic"
    ENTERPRISE = "enterprise"

class User(models.Model):
    user_id = fields.IntField(primary_key=True)

    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=255, unique=True)
    email_normalized = fields.CharField(
        max_length=255, null=True
    )  # TODO: Need to copy over

    fname = fields.CharField(max_length=50)
    lname = fields.CharField(max_length=50)

    digest = fields.CharField(max_length=128)

    activated_at = fields.DatetimeField(null=True)