from django.db.models.fields.files import ImageField, ImageFieldFile
from PIL import Image 
import os 

def _add_thumb(s):
    parts = s.split(".")
    parts.insert(-1, "thumb")
    if parts[-1].lower() not in ['jpeg','jpg']:
        parts[-1]='jpg'
    return ".".join(parts)

class ThumbnailImageFieldFile(ImageFieldFile): 
    def _get_thumb_path(self): 
        return _add_thumbs(self.path)
    thumb_path = property(_get_thumb_path)

    def _get_thumb_url(self):
        return _add_thumb(self.url)
    thumb_url = property(_get_thumb_url)

    def save(self ,name, content, save=True): 
        super(ThumbnailImageFieldFile,self).save(name,content,save)
        img = Image.open(self.path)
        size = (128, 128)
        img.thumbnail(size,Image.ANTIALIAS)
        background = Image.new('RGBA',size,(255,255,255,0))



    def delete(self,save=True):
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super(ThumbnailImageFieldFile, self).delete(save) 

class ThumbnailImageField(ImageField): 
    attr_class = ThumbnailImageFieldFile

    def __init__(self, thumb_width=128, thumb_height=128, *args, **kwargs):
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        super(ThumbnailImageField,self).__init__(*args,**kwargs)
