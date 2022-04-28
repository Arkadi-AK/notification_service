from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext

from api.post_sender import send_message
from notify_sender.models import Sender, Client, Message


class SenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_mailing', 'stop_mailing', 'text', 'filter')

    actions = ['start_mailing']

    def start_mailing(self, request, queryset):
        updated = send_message(request)
        # updated = queryset.update(status='p')
        updated = queryset.update
        self.message_user(request, ngettext(
            '%d story was successfully marked as published.',
            '%d stories were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'code_operator', 'teg', 'time_zone')
    list_display_links = ('id', 'phone_number')
    list_filter = ('code_operator',)
    save_on_top = True


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'status', 'id_mailing', 'id_client')
    list_display_links = ('id',)
    list_filter = ('status',)
    save_on_top = True


admin.site.register(Sender, SenderAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Message, MessageAdmin)

admin.site.site_header = 'Управление рассылками'
