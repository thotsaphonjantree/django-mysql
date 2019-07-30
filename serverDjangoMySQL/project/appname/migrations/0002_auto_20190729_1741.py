# Generated by Django 2.2.3 on 2019-07-29 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='University',
            new_name='Major',
        ),
        migrations.AlterModelOptions(
            name='major',
            options={'verbose_name': 'Major', 'verbose_name_plural': 'Majors'},
        ),
        migrations.RenameField(
            model_name='major',
            old_name='name',
            new_name='major_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='university',
            new_name='major',
        ),
        migrations.AddField(
            model_name='student',
            name='student_code',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]