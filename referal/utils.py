import uuid
from . import models

def gen_ref_code():
    code = str(uuid.uuid4()).replace("-","")[:6]
    return code

def ref_count(user):
    ref_count = models.Referal.objects.filter(ref_by = user).count()
    return ref_count

def referances(User):
    refs = models.Referal.objects.filter(ref_by = User)
    refers = refs.user
    return refers