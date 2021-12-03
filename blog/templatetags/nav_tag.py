from django import template
register = template.Library()

from blog import models as BMODEL

@register.simple_tag
def categoryfornav():
    cat = BMODEL.category.objects.all()
    # print(f"nav category: {cat}")
    return cat