from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class ItemsParsed(models.Model):
    # cnt = models.CharField(max_length=1, blank=True, null=True)
    seller = models.CharField(max_length=1, blank=True, null=True)
    title = models.CharField(max_length=1, blank=True, null=True)
    brand = models.CharField(max_length=1, blank=True, null=True)
    product_description = models.CharField(max_length=1, blank=True, null=True)
    images = models.TextField(blank=True, null=True)  # This field type is a guess.
    images_count = models.IntegerField(blank=True, null=True)
    videos = models.TextField(blank=True, null=True)  # This field type is a guess.
    video_count = models.IntegerField(blank=True, null=True)
    star = models.FloatField(blank=True, null=True)
    reviews = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    price_old = models.IntegerField(blank=True, null=True)
    categories = models.TextField(blank=True, null=True)  # This field type is a guess.
    details = models.JSONField(blank=True, null=True)
    ship_from = models.CharField(max_length=1, blank=True, null=True)
    url = models.CharField(max_length=1, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    datetime = models.FloatField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    search_position = models.TextField(blank=True, null=True)  # This field type is a guess.
    keywords = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items_parsed'
        ordering = ['id']

