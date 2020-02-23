
# mobile = models.CharField(max_length=20)
# phone = models.CharField(max_length=20)
# email = models.EmailField()
# opening_hour_mon = models.CharField(max_length=20)
# opening_hour_tue = models.CharField(max_length=20)
# opening_hour_wed = models.CharField(max_length=20)
# opening_hour_thu = models.CharField(max_length=20)
# opening_hour_fri = models.CharField(max_length=20)
# opening_hour_sat = models.CharField(max_length=20)
# opening_hour_sun = models.CharField(max_length=20)

from django.db import migrations

def add_initial_data(apps, schema_editor):
    ContactDetail = apps.get_model('pages', 'ContactDetail')
    initialData = ContactDetail(
        mobile='123-346-7890',
        phone='123-346-7890',
        email='initial@test.com',
        opening_hour_mon='10:00 - 18:00',
        opening_hour_tue='10:00 - 18:00',
        opening_hour_wed='Closed',
        opening_hour_thu='10:00 - 18:00',
        opening_hour_fri='10:00 - 18:00',
        opening_hour_sat='10:00 - 18:00',
        opening_hour_sun='10:00 - 18:00'
    )
    initialData.save()

class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_contactdetail'),
    ]

    operations = [
        migrations.RunPython(add_initial_data)
    ]
