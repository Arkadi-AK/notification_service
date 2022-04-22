from django.contrib import admin

from notify_sender.models import Sender, Client, Message


class SenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_mailing', 'stop_mailing', 'text', 'filter')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'code_operator', 'teg', 'time_zone')
    list_display_links = ('id', 'phone_number')
    list_filter = ('phone_number',)
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
