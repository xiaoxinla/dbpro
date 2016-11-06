from django.db.models.fields.files import ImageField,ImageFieldFile
from PIL import Image
def _add_thumb(s):
    parts = s.split(".")
    parts.insert(-1,"thumb")
    if parts[-1].lower() not in ['jpeg','jpg']:
        parts[-1]='jpg'
    return ".".join(parts)
class ThumbnailImageFieldFile(ImageFieldFile):
    def _get_thumb_url(self):
        return _add_thumb(self.url)
    thumb_url = property(_get_thumb_url)

    def save(self,name,content,save=True):
        super(ThumbnailImageFieldFile, self).save(name,content,save)
    def delete(self,save=True):
        super(ThumbnailImageFieldFile, self).delete(save)


class ThumbnailImageField(ImageField):
    attr_class = ThumbnailImageFieldFile
    def __init__(self,*args,**kwargs):
        super(ThumbnailImageField, self).__init__(*args,**kwargs)
