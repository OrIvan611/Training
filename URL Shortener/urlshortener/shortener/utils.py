from .models import Url
import uuid
from .consts import SHORT_URL_LENGTH


def get_unique_uid():
    """
    Returns a uid that doesn't exist in the database.
    """
    uid = str(uuid.uuid4())[:SHORT_URL_LENGTH]
    while len(Url.objects.filter(short_url=uid)) != 0:
        uid = str(uuid.uuid4())[:SHORT_URL_LENGTH]
    return uid


def create_dummy_obj():
    """
    Creates a dummy Url object.
    Used for testing.
    """
    dummy_obj = Url(original_url="https://ravkavonline.co.il", short_url=get_unique_uid(), counter=0)
    dummy_obj.save()
    return dummy_obj