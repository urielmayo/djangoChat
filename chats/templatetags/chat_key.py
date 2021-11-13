from django import template

register = template.Library()

@register.filter
def get_value(chat_dict : dict, key):
    return chat_dict.get(key, 'default')