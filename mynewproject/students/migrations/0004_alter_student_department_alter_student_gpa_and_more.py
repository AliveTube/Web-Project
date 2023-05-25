# Generated by Django 4.2.1 on 2023-05-23 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_rename_date_student_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Department',
            field=models.CharField(choices=[('General', 'General'), ('IS', 'IS'), ('CS', 'CS'), ('IT', 'IT'), ('AI', 'AI'), ('DS', 'DS')], default='General', max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='GPA',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='student',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='Level',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], null=True),
        ),
    ]