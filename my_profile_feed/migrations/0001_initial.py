# Generated by Django 2.1.7 on 2019-04-25 15:02

from django.db import migrations, models
import djongo.models.fields
import my_profile_feed.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locality', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=6)),
                ('state', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Certifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certification_name', models.CharField(max_length=200)),
                ('authority', models.CharField(max_length=200)),
                ('cert_from', models.DateField(blank=True)),
                ('cert_to', models.DateField(blank=True)),
                ('cert_pic', models.ImageField(blank=True, upload_to='certificate_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=50)),
                ('sender_email', models.EmailField(max_length=254)),
                ('receiver_name', models.CharField(max_length=50)),
                ('receiver_email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=200)),
                ('created_on', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=50)),
                ('school_from', models.DateField(blank=True)),
                ('school_to', models.DateField(blank=True)),
                ('degree', models.CharField(max_length=50)),
                ('study_field', models.CharField(max_length=50)),
                ('descriptionEdu', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('work_field', models.CharField(max_length=200)),
                ('from_date', models.DateField(blank=True)),
                ('to_date', models.DateField(blank=True)),
                ('descriptionExp', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FollowNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.EmailField(max_length=254)),
                ('text', models.TextField(max_length=200)),
                ('created_on', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=50)),
                ('post_author', models.EmailField(max_length=254)),
                ('author', models.EmailField(max_length=254)),
                ('text', models.TextField(max_length=200)),
                ('created_on', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_email', models.EmailField(max_length=254)),
                ('overview', models.TextField()),
                ('experience', djongo.models.fields.ArrayModelField(model_container=my_profile_feed.models.Experience)),
                ('address', djongo.models.fields.EmbeddedModelField(model_container=my_profile_feed.models.Address, null=True)),
                ('skills', djongo.models.fields.ArrayModelField(model_container=my_profile_feed.models.Skill)),
                ('interests', djongo.models.fields.ArrayModelField(model_container=my_profile_feed.models.Interest)),
                ('education_details', djongo.models.fields.ArrayModelField(model_container=my_profile_feed.models.Education_details)),
                ('certifications', djongo.models.fields.ArrayModelField(model_container=my_profile_feed.models.Certifications)),
                ('notification', djongo.models.fields.ArrayModelField(model_container=my_profile_feed.models.Notification)),
                ('follow_notification', djongo.models.fields.ArrayModelField(model_container=my_profile_feed.models.FollowNotification)),
                ('chats', djongo.models.fields.ArrayModelField(model_container=my_profile_feed.models.Chats)),
            ],
        ),
    ]
