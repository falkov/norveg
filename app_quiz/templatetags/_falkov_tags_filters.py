from django import template

register = template.Library()

# if List = [['a','b','c'], ['d','e','f']], вы можете использовать {{ List|index:x|index:y }} в шаблоне, чтобы получить List[x][y]
# Он отлично работает с "for": {{ List|index:forloop.counter0 }}


@register.filter
def index(lst, ind):
    """
    if List = [['a','b','c'], ['d','e','f']], можно использовать {{ List|index:x|index:y }} в шаблоне, чтобы получить List[x][y]
    Он отлично работает с "for": {{ List|index:forloop.counter0 }}
    """
    return lst[int(ind)]


@register.filter
def index_dec(lst, ind):
    """
    возвращает элемент списка по индексу - 1
    """
    return lst[int(ind-1)]


@register.filter
def inc(val):
    return int(val+1)


@register.filter
def qnum_to_string(val):
    """
    1-9 => '01'-'09', 12... => '12'...
    """
    if str(val).isdecimal():
        if len(str(val)) == 1:
            return '0' + str(val)
        else:
            return str(val)
