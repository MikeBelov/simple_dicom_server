from string import ascii_letters, digits
from datetime import datetime

VALID_CHARS = "-_.() %s%s" % (ascii_letters, digits)
DATE_FMT = '%Y%m%d %H:%M'


def sanitize_filename(filename):
    return ''.join(c for c in filename if c in VALID_CHARS)


def get_date(fmt=DATE_FMT):
    return datetime.now().strftime(fmt)


def get_ae_title(event):
    return str(event.assoc.requestor.ae_title, encoding='utf-8').strip()
