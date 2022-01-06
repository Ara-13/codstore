def code_generator():
    from . import models
    x = models.Account.objects.all().count()+1
    return int(x)
