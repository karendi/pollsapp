from PIL import Image

from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save


class Country(models.Model):
    Name = models.CharField(max_length=20)
    Slug = models.SlugField(unique = True)

    def __str__(self):
        return self.Name

    def save(self , *args , **kwargs):
        self.Slug = slugify(self.Name)
        super(Country , self).save(*args , **kwargs)




class County(models.Model):
    Country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="")
    Name = models.CharField(max_length=20)
    Slug = models.SlugField(unique= True )

    def __str__(self):
        return self.Name

    def save(self, *args, **kwargs):
        self.Slug = slugify(self.Name)
        super(County , self).save(*args , **kwargs)


class Constituency(models.Model):
    County = models.ForeignKey(County, on_delete=models.CASCADE)
    Name = models.CharField(max_length=20)
    Slug = models.SlugField(unique= True)

    def __str__(self):
        return self.Name

    def save(self, *args, **kwargs):
        self.Slug = slugify(self.Name)
        super(Constituency, self).save(*args, **kwargs)


class Ward(models.Model):
    Constituency = models.ForeignKey(Constituency, on_delete=models.CASCADE)
    Name = models.CharField(max_length=20)
    Slug = models.SlugField(unique= True)

    def __str__(self):
        return self.Name

    def save(self, *args, **kwargs):
        self.Slug = slugify(self.Name)
        super(Ward, self).save(*args, **kwargs)


# rally dates
class RallyDate(models.Model):
    Date = models.DateTimeField()
    Location = models.CharField(max_length=50)

    def __str__(self):
        return self.Location + str(self.Date)


# the party
class Party(models.Model):
    Name = models.CharField(max_length=20)
    Slug = models.SlugField(unique= True)
    Icon = models.FileField(blank = True , null = True)
    Twitter = models.URLField()
    Facebook = models.URLField()
    Manifesto = models.TextField()

    def __str__(self):
        return self.Name

    def save(self):
        self.Slug = slugify(self.Name)
        super(Party ,self).save()




# the candidates
class President(models.Model):
    Country = models.ForeignKey(Country, on_delete=models.CASCADE)
    Party = models.ForeignKey(Party, on_delete=models.CASCADE)
    RallyDate = models.ForeignKey(RallyDate, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=20)
    Middle_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Image = models.ImageField(
                              blank = True ,
                              null = True,
                              height_field="height_field",
                              width_field="width_field",

                              )
    height_field = models.IntegerField(default = 290)
    width_field = models.IntegerField(default = 470)
    MyStand = models.TextField()
    Slug = models.SlugField()
    Vote = models.BooleanField()
    Twitter = models.URLField()
    Facebook = models.URLField()

    def __str__(self):
        return self.First_name + '-' + self.Party.Name



class Governor(models.Model):
    County = models.ForeignKey(County, on_delete=models.CASCADE)
    Party = models.ForeignKey(Party, on_delete=models.CASCADE)
    RallyDate = models.ForeignKey(RallyDate, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=20)
    Middle_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Image = models.FileField(blank = True , null= True)
    MyStand = models.TextField(blank = True)
    Slug = models.SlugField(unique = True)
    Vote = models.BooleanField()
    Twitter = models.URLField(blank = True)
    Facebook = models.URLField(blank = True)

    def __str__(self):
        return self.First_name + '-' + self.Party.Name

    def save(self, *args, **kwargs):
        self.Slug = slugify(self.First_name + self.Middle_name + self.Last_name)
        super(Governor, self).save(*args, **kwargs)


class Senator(models.Model):
    County = models.ForeignKey(County, on_delete=models.CASCADE)
    Party = models.ForeignKey(Party, on_delete=models.CASCADE)
    RallyDate = models.ForeignKey(RallyDate, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=20)
    Middle_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Image = models.FileField(blank = True , null= True)
    MyStand = models.TextField()
    Slug = models.SlugField(unique= True)
    Vote = models.BooleanField()
    Twitter = models.URLField()
    Facebook = models.URLField()

    def __str__(self):
        return self.First_name + '-' + self.Party.Name

    def save(self, *args, **kwargs):
        self.Slug = slugify(self.First_name + self.Middle_name + self.Last_name)
        super(Senator, self).save(*args, **kwargs)


class Memberofparliament(models.Model):
    Constituency = models.ForeignKey(Constituency, on_delete=models.CASCADE)
    Party = models.ForeignKey(Party, on_delete=models.CASCADE)
    RallyDate = models.ForeignKey(RallyDate, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=20)
    Middle_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Image = models.FileField(blank = True , null= True)
    MyStand = models.TextField()
    Slug = models.SlugField(unique = True)
    Vote = models.BooleanField()
    Twitter = models.URLField()
    Facebook = models.URLField()

    def __str__(self):
        return self.First_name + '-' + self.Party.Name

    def save(self, *args, **kwargs):
        self.Slug = slugify(self.First_name + self.Middle_name + self.Last_name)
        super(Memberofparliament, self).save(*args, **kwargs)


class Womensrep(models.Model):
    County = models.ForeignKey(County, on_delete=models.CASCADE)
    Party = models.ForeignKey(Party, on_delete=models.CASCADE)
    RallyDate = models.ForeignKey(RallyDate, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=20)
    Middle_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Image = models.FileField(blank = True , null = True)
    MyStand = models.TextField()
    Slug = models.SlugField(unique = True)
    Vote = models.BooleanField()
    Twitter = models.URLField()
    Facebook = models.URLField()

    def __str__(self):
        return self.First_name + '-' + self.Party.Name

    def save(self, *args, **kwargs):
        self.Slug = slugify(self.First_name + self.Middle_name + self.Last_name)
        super(Womensrep, self).save(*args, **kwargs)


class MemberofCountyAssembly(models.Model):
    Ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    Party = models.ForeignKey(Party, on_delete=models.CASCADE)
    RallyDate = models.ForeignKey(RallyDate, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=20)
    Middle_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Image = models.FileField(blank = True , null= True)
    MyStand = models.TextField()
    Slug = models.SlugField(unique= True )
    Vote = models.BooleanField()
    Twitter = models.URLField()
    Facebook = models.URLField()

    def __str__(self):
        return self.First_name + '-' + self.Party.Name

    def save(self, *args, **kwargs):
        self.Slug = slugify(self.First_name + self.Middle_name + self.Last_name)
        super(MemberofCountyAssembly, self).save(*args, **kwargs)
