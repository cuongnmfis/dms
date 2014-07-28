import floppyforms as forms

class ImageThumbnailFileInput(forms.ClearableFileInput):
    template_name = 'myapp/image_thumbnail.html'


class ImageForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('image',)
        widgets = {'image': ImageThumbnailFileInput}