from django_slots import Library, Component

register = Library()


@register.block_component
class Popups(Component):
    pass
