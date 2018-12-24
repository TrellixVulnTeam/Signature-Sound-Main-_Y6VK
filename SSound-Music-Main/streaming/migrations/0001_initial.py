# Generated by Django 2.1.2 on 2018-12-24 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('user_password', models.CharField(max_length=40, verbose_name='패스워드')),
                ('authority_code', models.IntegerField(verbose_name='권한부여코드')),
                ('nickname', models.CharField(max_length=30, verbose_name='닉네임')),
                ('profile_url', models.CharField(max_length=50, verbose_name='이미지 경로')),
                ('own_coin', models.IntegerField(verbose_name='소유하고 있는 코인')),
                ('country_code', models.IntegerField(verbose_name='국적코드')),
            ],
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_code', models.IntegerField()),
                ('more_code', models.IntegerField()),
                ('code_label', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.IntegerField()),
                ('company_name', models.IntegerField()),
                ('compnay_representation', models.IntegerField()),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='streaming.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_number', models.IntegerField()),
                ('album', models.IntegerField()),
                ('title', models.CharField(max_length=30)),
                ('genre', models.IntegerField()),
                ('Release_Date', models.DateField(auto_now_add=True)),
                ('songwriting', models.CharField(max_length=30, verbose_name='작사가')),
                ('composer', models.CharField(max_length=30, verbose_name='작곡가')),
                ('music_arranger', models.CharField(max_length=30, verbose_name='편곡가')),
                ('music_length', models.IntegerField()),
                ('sound_quality', models.CharField(max_length=10)),
                ('music_images_url', models.CharField(max_length=30, verbose_name='이미지 경로')),
                ('video_path', models.CharField(max_length=40, verbose_name='파일 경로')),
                ('total_streaming', models.IntegerField(verbose_name='총 재생수')),
                ('music_price', models.IntegerField(verbose_name='음원가격')),
                ('total_profit', models.IntegerField(verbose_name='총 음원수익')),
                ('entainment', models.CharField(max_length=30, verbose_name='기획사')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='streaming.Artist')),
            ],
        ),
    ]
