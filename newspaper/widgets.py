from django.forms.widgets import FileInput


class ImageCustomWidget(FileInput):
    template_name = 'newspaper/image_render_in_admin.html'
