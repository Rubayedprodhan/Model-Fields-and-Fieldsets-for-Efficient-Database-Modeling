from django.db import models

class OtherModel(models.Model):
    field_name = models.CharField(max_length=100)

    def __str__(self):
        return self.field_name

class AnotherModel(models.Model):
    field_name = models.CharField(max_length=100)

    def __str__(self):
        return self.field_name

class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20)
    address = models.TextField(max_length=50)
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField(default=False)
    char_field = models.CharField(max_length=255)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=10, decimal_places=2)
    duration_field = models.DurationField()
    email_field = models.EmailField()
    float_field = models.FloatField()

    foreign_key = models.ForeignKey(OtherModel, on_delete=models.CASCADE, related_name='students_foreign_key')
    one_to_one_field = models.OneToOneField(OtherModel, on_delete=models.CASCADE, related_name='student_one_to_one')
    generic_ip_address_field = models.GenericIPAddressField()
    image_field = models.ImageField(upload_to='images/')
    integer_field = models.IntegerField()
    json_field = models.JSONField()
    many_to_many_field = models.ManyToManyField(AnotherModel)
    null_boolean_field = models.BooleanField(null=True)
    positive_big_integer_field = models.PositiveBigIntegerField()
    positive_integer_field = models.PositiveIntegerField()
    positive_small_integer_field = models.PositiveSmallIntegerField()
    slug_field = models.SlugField()
    small_integer_field = models.SmallIntegerField()
    text_field = models.TextField()
    time_field = models.TimeField()
    url_field = models.URLField()
    uuid_field = models.UUIDField()

    def __str__(self):
        return f"Name: {self.name}"
