from django.db import models

# Create your models here.
class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    nom_genero = models.CharField(max_length=200)
    descrip_genero = models.CharField(max_length=200)
    total_libros = models.IntegerField(default=0)

    def __str__(self):
        return self.nom_genero


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nom_usuario = models.CharField(max_length=200)
    apellido_usuario = models.CharField(max_length=200)
    email_usuario = models.CharField(max_length=200)
    telefono_cel_usuario = models.CharField(max_length=10)
    num_libros = models.IntegerField(default=0)

    def __str__(self):
        return self.nom_usuario + self.apellido_usuario
    

class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nom_autor = models.CharField(max_length=200)
    nacionalidad_autor = models.CharField(max_length=200)

    def __str__(self):
        return self.nom_autor

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"


class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    titulo_libro = models.CharField(max_length=200)
    estado_libro = models.CharField(max_length=200) #disponible, solicitado, prestado
    id_autor = models.ForeignKey(Autor,on_delete=models.CASCADE)    
    id_genero = models.ForeignKey(Genero,on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo_libro


class Intercambio(models.Model):
    id_intercambio = models.AutoField(primary_key=True)
    fecha_prestamo = models.DateTimeField(auto_now=True)
    fecha_entrega = models.DateTimeField()
    id_libro = models.ForeignKey(Libro,on_delete=models.CASCADE)
    id_usuario1 = models.ForeignKey(Usuario,on_delete=models.CASCADE, related_name="id_usuario1")
    id_usuario2 = models.ForeignKey(Usuario,on_delete=models.CASCADE, related_name="id_usuario2")
    
    def __str__(self):
        return self.id_libro,self.fecha_prestamo


class Calificacion(models.Model):
    id_calificacion = models.AutoField(primary_key=True)    
    calificacion = models.FloatField()
    comentario = models.CharField(max_length=200)
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"

    def __str__(self):
        return self.id_usuario + "("+ self.id_libro+": "+self.calificacion+")"


