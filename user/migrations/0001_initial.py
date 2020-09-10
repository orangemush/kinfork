from django.db import migrations, models
import django.db.models.deletion
import user.validator


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=64)),
                ('password', models.CharField(max_length=256, validators=[user.validator.password_validate])),
                ('user_name', models.CharField(max_length=32, null=True)),
                ('display_name', models.CharField(max_length=32, null=True)),
                ('real_name', models.CharField(max_length=32, null=True)),
                ('kakao_id', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.CharField(max_length=64)),
                ('company_name', models.CharField(max_length=64, null=True)),
                ('country_region', models.CharField(max_length=64)),
                ('street_address', models.CharField(max_length=512)),
                ('post_code', models.IntegerField()),
                ('town_city', models.CharField(max_length=32)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.account')),
            ],
        ),
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.CharField(max_length=64)),
                ('company_name', models.CharField(max_length=64, null=True)),
                ('country_region', models.CharField(max_length=64)),
                ('street_address', models.CharField(max_length=512)),
                ('post_code', models.IntegerField()),
                ('town_city', models.CharField(max_length=32)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.account')),
            ],
        ),
    ]
