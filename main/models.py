from django.db import models

class Category(models.Model): # фильтр категорий
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)   # в ссылке заменяет пробелы на тире короче типа ./products/product-1

    class Meta:   # параметры с которыми будут работать база данных и админка
        ordering = ('name', )
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name   # категории в списке буду отображаться по имени в админке

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE) # ON_DELETE при удалении категории в админке, также удалит и все продукты с этой категорией
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=100)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True) # blank означает что поле может быть пустое
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2) # число с плавающей точкой; 2 параметр - округление до 2 символов после запятой
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name