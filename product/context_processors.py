from .models import Category

def menu(request):
    links = Category.objects.all()
    return {'links': links}
