from django.db import models
from .utils import gen_ref_code
from django.contrib.auth import get_user_model
User = get_user_model()

class SetRefReward(models.Model):
    refReward = models.IntegerField()
    maxRefs = models.IntegerField()

    def __str__(self):
        return f"{self.refReward} - {self.maxRefs}"

class Referal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=10 , blank=True)
    ref_by = models.ForeignKey(User , on_delete=models.CASCADE , blank=True , null=True , related_name='ref_by')

    def __str__(self):
        return f"{self.user.p_number}-{self.code}"
    
    def save(self , *args , **kwargs):
        if self.code == "":
            code = gen_ref_code()
            self.code = code
        super().save(*args , **kwargs)

class Reward_add(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    received = models.IntegerField(default=0)
    total_refs = models.IntegerField(default=0)