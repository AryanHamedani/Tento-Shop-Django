from django.db.models import Manager


class SubCategoriesManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(sub_category__isnull=True)
