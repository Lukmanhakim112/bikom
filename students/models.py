from django.db import models
from django.utils.translation import ugettext_lazy as _




FULL_NAME = models.CharField(_('Full Name'), max_length=100)

class BestFriends(models.Model):
    full_name = FULL_NAME
    phone_number = models.CharField(_('Phone Number'), max_length=15)

    def __str__(self):
        return self.full_name


class StudentProfile(models.Model):
    instagram = models.CharField(
        _('Instagram Account'), max_length=35,
        help_text=_("Enter your instagram username with the @, i.e: @ziyk123.")
    )
    chield_number = models.CharField(
        _('Chield Number'), max_length=2,
    )
    number_of_sibling = models.CharField(
        _('Number of sibling(s).'), max_length=2,
    )
    # klass == class
    klass = models.CharField(
        _('Class'), max_length=13,
        help_text=_('Enter your class name, i.e: XII TJAT-2. HARUS tulis seperti contoh.')
    )
    friend = models.ManyToManyField(BestFriends, verbose_name=_('Best Friends'))

class ParentBaseModels(models.Model):
    """
    Create blueprint for both Father and Mother models,
    https://docs.djangoproject.com/en/3.2/topics/db/models/#abstract-base-classes
    """
    full_name = FULL_NAME
    jobs = models.CharField(_('Jobs'), max_length=100)
    chield = models.OneToOneField(StudentProfile, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.full_name


class FatherStudentModels(ParentBaseModels):
    """
    The actual models that being used
    """
    pass

class MotherStudentModels(ParentBaseModels):
    """
    The actual models that being used
    """
    pass

