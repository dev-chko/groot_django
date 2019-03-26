# Generated by Django 2.1.4 on 2018-12-28 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('cert_idx', models.AutoField(primary_key=True, serialize=False)),
                ('term', models.IntegerField()),
                ('end_date', models.DateTimeField()),
                ('cert_tx', models.CharField(max_length=100)),
                ('c_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'Certificate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('cont_idx', models.AutoField(primary_key=True, serialize=False)),
                ('term', models.IntegerField()),
                ('end_date', models.DateTimeField()),
                ('c_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'Contract',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DocVf',
            fields=[
                ('doc_idx', models.AutoField(primary_key=True, serialize=False)),
                ('up_hash', models.CharField(max_length=100)),
                ('c_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'Doc_vf',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('enroll_idx', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('term', models.IntegerField()),
                ('enroll_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('enroll_tx', models.CharField(blank=True, max_length=100, null=True)),
                ('c_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Enrollment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('uuid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=100)),
                ('file_type', models.CharField(max_length=100)),
                ('file_hash', models.CharField(max_length=100)),
                ('m_date', models.DateTimeField()),
                ('c_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'File',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ItBoard',
            fields=[
                ('board_idx', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True, null=True)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('c_date', models.DateTimeField()),
                ('m_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'It_board',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('notice_idx', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True, null=True)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('c_date', models.DateTimeField()),
                ('m_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'Notice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SortMst',
            fields=[
                ('sort_idx', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Sort_MST',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('user_pw', models.CharField(max_length=100)),
                ('com_num', models.IntegerField()),
                ('com_name', models.CharField(max_length=100)),
                ('com_head', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone_num', models.IntegerField()),
                ('c_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'User',
                'managed': False,
            },
        ),
    ]