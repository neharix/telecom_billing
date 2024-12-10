from django.db.models import Model

exists_by_id = lambda id, model: model.objects.filter(id=id).exists()
