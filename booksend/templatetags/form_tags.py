from django import template
register = template.Library()

@register.filter(name="add_class")
def add_class(field, css):
    # รวม class เดิม (ถ้ามี) + class ใหม่
    existing = field.field.widget.attrs.get("class", "")
    new = (existing + " " + css).strip()
    # คง attrs เดิมอื่น ๆ ไว้ด้วย
    return field.as_widget(attrs={**field.field.widget.attrs, "class": new})
