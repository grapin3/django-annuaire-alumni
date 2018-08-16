from django.template import Library
from django.forms.utils import flatatt

register = Library()

@register.inclusion_tag("annuaire/bootstrap_forms/label.html")
def label(field, contents=None):
    widget = field.field.widget
    for_id = widget.id_for_label(widget.attrs.get('id') or field.auto_id)
    contents = contents or field.label
    return {'field':field, 'id': for_id, 'contents': contents}

@register.inclusion_tag("annuaire/bootstrap_forms/errors.html")
def errors(field):
    return {'field':field}

@register.inclusion_tag("annuaire/bootstrap_forms/help_text.html")
def help_text(field):
    return {'field':field}

@register.inclusion_tag("annuaire/bootstrap_forms/input_field.html")
def input_field(field, method, placeholder="", input_type="text", value=None, attrs=None):
    if isinstance(attrs, str):
        attrs = [tuple(pair).split('=') for pair in attrs.split(',')]
    attrs = dict(attrs or {})
    widget = field.field.widget
    for_id = widget.id_for_label(widget.attrs.get('id') or field.auto_id)
    name = field.html_name
    value = value or field.value
    post = method == "POST"
    return {'field':field, 'id':for_id, 'name':name, 'type':input_type,
            'value':value, 'placeholder':placeholder,
            'required':field.field.required, 'post':post,
            'attrs':flatatt(attrs),}
