from .models import MainCategory


def categories(request):
    """Expose some categories in templates."""
    return {"main_categories": MainCategory.objects.filter()}
