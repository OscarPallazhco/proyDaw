# Generated by Django 2.2 on 2019-12-26 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id_autor', models.AutoField(primary_key=True, serialize=False)),
                ('nom_autor', models.CharField(max_length=200)),
                ('naionalidad_autor', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.AutoField(primary_key=True, serialize=False)),
                ('nom_genero', models.CharField(max_length=200)),
                ('descrip_genero', models.CharField(max_length=200)),
                ('total_libros', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nom_usuario', models.CharField(max_length=200)),
                ('apellido_usuario', models.CharField(max_length=200)),
                ('email_usuario', models.CharField(max_length=200)),
                ('telefono_cel_usuario', models.CharField(max_length=10)),
                ('num_libros', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id_libro', models.AutoField(primary_key=True, serialize=False)),
                ('titulo_libro', models.CharField(max_length=200)),
                ('estado_libro', models.CharField(max_length=200)),
                ('id_autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sb_db_app.Autor')),
                ('id_genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sb_db_app.Genero')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sb_db_app.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Intercambio',
            fields=[
                ('id_intercambio', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_prestamo', models.DateTimeField(auto_now=True)),
                ('fecha_entrega', models.DateTimeField()),
                ('id_libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sb_db_app.Libro')),
                ('id_usuario1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_usuario1', to='sb_db_app.Usuario')),
                ('id_usuario2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_usuario2', to='sb_db_app.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id_calificacion', models.AutoField(primary_key=True, serialize=False)),
                ('calificacion', models.FloatField()),
                ('comentario', models.CharField(max_length=200)),
                ('id_libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sb_db_app.Libro')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sb_db_app.Usuario')),
            ],
        ),
    ]