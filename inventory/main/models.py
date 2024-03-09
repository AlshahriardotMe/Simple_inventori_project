from django.db import models

# Create your models here.
# vendor
class Vendor(models.Model):
    full_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="images/")
    address = models.TextField()
    mobile = models.CharField(max_length=20)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = '1. Vendors'

    def __str__(self):
        return self.full_name



# coustomer
class Coustomer(models.Model):
    customer_name = models.CharField(max_length=50, blank=True)
    customer_mobile = models.CharField(max_length=20)
    customer_address = models.TextField()

    def __str__(self):
        return self.customer_name
    
    class Meta:
        verbose_name_plural = '2. Coustomers'


# unit 
class Unit(models.Model):
    title = models.CharField(max_length=50)
    short_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = '3. Units'
    
    def __str__(self):
        return self.title

# Product
class Product(models.Model):
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="product_image/")
    detail = models.TextField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = '4. Products'

    def __str__(self):
        return self.title



# Purchace
class Purchace(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    quality = models.FloatField()
    price = models.FloatField()
    total_amount = models.FloatField()
    purchace_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '5. Purchaces'
    

    
    def save(self, *args, **kwargs):
        self.total_amount=self.quality*self.price
        super(Purchace, self).save(*args,**kwargs)


        # Iventory Effect
        inventory = Inventory.objects.filter(product=self.product).order_by('-id').first()
        if inventory:
            total_balance = inventory.total_balance_quality+self.quality
        else:
            total_balance =self.quality

        Inventory.objects.create(
            product= self.product,
            purchace= self,
            sell= None,
            puechace_quality =self.quality,
            sell_quality = None ,
            total_balance_quality= total_balance
        )

# Sell
class Sell(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    coustomer = models.ForeignKey(Coustomer, on_delete=models.CASCADE,null=True)
    quality = models.FloatField()
    price = models.FloatField()
    total_amount = models.FloatField(editable=False)
    sell_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = '6. Sells'

    def save(self, *args, **kwargs):
        self.total_amount=self.quality*self.price
        super(Sell, self).save(*args,**kwargs)


        # Iventory Effect
        inventory = Inventory.objects.filter(product=self.product).order_by('-id').first()
        if inventory:
            total_balance = inventory.total_balance_quality-self.quality


        Inventory.objects.create(
            product= self.product,
            purchace= None,
            sell= self,
            puechace_quality =None ,
            sell_quality = self.quality,
            total_balance_quality= total_balance

        )


# Inventory 
class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchace = models.ForeignKey(Purchace, on_delete=models.CASCADE, default=0, null=True)
    sell = models.ForeignKey(Sell, on_delete=models.CASCADE,default=0, null=True)
    puechace_quality = models.FloatField(default=0, null=True)
    sell_quality = models.FloatField(default=0, null=True)
    total_balance_quality = models.FloatField()
    

    class Meta:
        verbose_name_plural = '7. Inventorys'
    



    def product_unit(self):
        return self.product.unit.title
        

    def purchace_date(self):
        if self.purchace:
            return self.purchace.purchace_date
        

    def sell_date(self):
        if self.sell:
            return self.sell.sell_date
