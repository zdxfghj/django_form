from django.db import models

SERVICE_CHOICES = (
    ('Ride hailing', 'Ride hailing'),
    ('Taxi', 'Taxi'),
    ('Executive cars', 'Executive cars'),
    ('Aiport shuttle', 'Aiport shuttle'),
    ('Bikes or motorbikes', 'Bikes or motorbikes'),
    ('Delivery', 'Delivery'),
    ('Other', 'Other'),
)


FUND_US_CHOICES = (
    ('Facebook', 'Facebook'),
    ('Google', 'Google'),
    ('Online media', 'Online media'),
    ('Other social media', 'Other social media'),
    ('Referred by customer', 'Referred by customer'),
    ('Delivery', 'Delivery'),
    ('Other', 'Other'),
)


class FeedBack(models.Model):
    first_name = models.CharField("Имя пользователя", max_length=50)
    last_name = models.CharField("Фамилия пользователя", max_length=50)
    email = models.EmailField("Email")
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES, default='Other')
    info = models.CharField(max_length=20, choices=FUND_US_CHOICES, default='Other')
    mark_communication = models.BooleanField(default=False)
    personalize_ads = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Форма обратной связи"
        verbose_name_plural = "Формы обратной связи"
