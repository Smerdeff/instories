from django.contrib import admin
from django.utils.html import format_html
from .forms import PushesForm
from .models import Pushes, Option


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def delete_button(self, obj):
        return format_html('<a class="deletelink" href="{}/delete/">Удалить</a>', obj.id)

    delete_button.short_description = 'Удалить'

    actions = []
    list_display = ('name', 'value', 'delete_button')
    list_display_links = ('name',)
    list_editable = ('value',)


@admin.register(Pushes)
class PushesAdmin(admin.ModelAdmin):
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def delete_button(self, obj):
        return format_html('<a class="deletelink" href="{}/delete/">Удалить</a>', obj.id)

    delete_button.short_description = 'Удалить'
    actions = []
    list_display = ('title', 'created_at', 'sent_at', 'is_sent', 'delete_button',)

    form = PushesForm
    change_form_template = 'admin/pushes/change_form.html'
