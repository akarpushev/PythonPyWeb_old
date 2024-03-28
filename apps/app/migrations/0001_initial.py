# Generated by Django 4.2.5 on 2024-03-28 15:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, help_text='Короткая биография', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='author_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль автора',
                'verbose_name_plural': 'Профили авторов',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название блога уникальное. Ограничение 100 знаков', max_length=100, unique=True, verbose_name='Название блога')),
                ('slug_name', models.SlugField(help_text='Название написанное транслитом, для человекочитаемости. Название уникальное.', unique=True, verbose_name='Slug поле названия')),
                ('headline', models.TextField(blank=True, help_text='Ограничение 255 символов.', max_length=255, null=True, verbose_name='Короткий слоган')),
                ('description', models.TextField(blank=True, help_text='О чем этот блог? Для кого он, в чем его ценность?', null=True, verbose_name='Описание блога')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
                'unique_together': {('name', 'slug_name')},
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ограничение на 50 символов', max_length=50, verbose_name='Имя тега')),
                ('slug_name', models.SlugField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, default='avatars/unnamed.png', null=True, upload_to='avatars/')),
                ('phone_number', models.CharField(blank=True, help_text='Формат +79123456789', max_length=12, null=True, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+79123456789'.", regex='^\\+79\\d{9}$')])),
                ('city', models.CharField(blank=True, help_text='Город проживания', max_length=120, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255, verbose_name='заголовок статьи')),
                ('slug_headline', models.SlugField(blank=True, editable=False, help_text='Если не указать, \n        то конвертирует самостоятельно, если указать, то запишет, \n        что указали (slug значение)', max_length=255, null=True, verbose_name='slug заголовок')),
                ('summary', models.TextField(verbose_name='краткое описание')),
                ('body_text', tinymce.models.HTMLField(blank=True, default='', verbose_name='текст статьи')),
                ('image', models.ImageField(blank=True, default='image_entry/default.jpg', null=True, upload_to='image_entry', verbose_name='картинка')),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='дата публикации')),
                ('status', models.CharField(blank=True, choices=[('draft', 'Черновик'), ('published', 'Опубликовано'), ('scheduled', 'Отложено')], default='published', max_length=20)),
                ('mod_date', models.DateField(auto_now=True)),
                ('number_of_comments', models.IntegerField(blank=True, default=0)),
                ('number_of_pingbacks', models.IntegerField(blank=True, default=0)),
                ('rating', models.FloatField(blank=True, default=0.0)),
                ('authors', models.ManyToManyField(help_text='Укажите \n                                     автора и соавторов, если они есть.\n                                     Зажмите Ctrl, чтобы выделить несколько \n                                     авторов', related_name='entrys', to='app.authorprofile', verbose_name='авторы')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entryes', to='app.blog', verbose_name='блог')),
                ('tags', models.ManyToManyField(to='app.tag', verbose_name='теги статьи')),
            ],
            options={
                'ordering': ('-pub_date',),
                'permissions': [('can_view_entry', 'Может просматривать статью'), ('can_add_entry', 'Может создать статью'), ('can_change_entry', 'Может изменять статью'), ('can_delete_entry', 'Может удалять статью')],
                'unique_together': {('blog', 'headline', 'slug_headline')},
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('entry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='app.entry')),
                ('parent', models.ForeignKey(blank=True, help_text='Комментарий с которого началась новая ветка', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='app.comment', verbose_name='родительский комментарий')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
