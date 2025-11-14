from django.db import models

class Materiel(models.Model):
    nom = models.CharField(max_length=100)
    categorie = models.CharField(max_length=50)
    quantite = models.PositiveIntegerField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    etat = models.CharField(max_length=50, choices=[
        ('Neuf', 'Neuf'),
        ('Bon', 'Bon'),
        ('Endommagé', 'Endommagé'),
    ])

    def __str__(self):
        return self.nom
