from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200, default="O mnie")
    content = models.TextField(help_text="Opis kim jestem i moje doświadczenie")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "O mnie"
        verbose_name_plural = "O mnie"

    @classmethod
    def get_about(cls):
        about, created = cls.objects.get_or_create(pk=1)
        return about
    

class Technology(models.Model):
    name = models.CharField(max_length=100, help_text="Nazwa technologii (np. Python, Django)")
    icon = models.ImageField(upload_to="technologies/", blank=True, null=True, help_text="Logo lub ikona technologii")
    description = models.TextField(help_text="Krótki opis technologii")
    order = models.IntegerField(default=0, help_text="Kolejność wyświetlania")

    class Meta:
        verbose_name = "Technologia"
        verbose_name_plural = "Technologie"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=200, help_text="Tytuł projektu")
    description = models.TextField(help_text="Opis projektu")
    image = models.ImageField(upload_to='projects/', blank=True, null=True, help_text="Zrzut ekranu projektu")
    github_link = models.URLField(blank=True, help_text="Link do repozytorium GitHub")
    live_link = models.URLField(blank=True, help_text="Link do działającej wersji")
    technologies = models.ManyToManyField(Technology, blank=True, help_text="Technologie uzyte w projekcie")
    order = models.IntegerField(default=0, help_text="Kolejność wyświetlnia")
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Projekt"
        verbose_name_plural = "Projekty"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Imię")
    email = models.EmailField(verbose_name="E-mail")
    message = models.TextField(verbose_name="Tresc wiadomości")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data wysłania")
    is_read = models.BooleanField(default=False, verbose_name="Przeczytana")

    class Meta:
        verbose_name = "Wiadomość kontaktowa"
        verbose_name_plural = "Wiadomości kontaktowe"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.email} ({self.created_at.strftime('%Y-%m-%d')})"

    


