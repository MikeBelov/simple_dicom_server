import os

from pynetdicom import AE, evt
from pynetdicom.presentation import AllStoragePresentationContexts
from pynetdicom.sop_class import VerificationSOPClass

import utils
from config import Config

config = Config()


def handle_connection(event):
    ae_title = utils.get_ae_title(event)
    print(ae_title, 'connected at', utils.get_date(TIME_FMT))

    return 0x0000


def handle_store(event):
    ae_title = utils.get_ae_title(event)
    ds = event.dataset

    # Patient Folder
    path = os.path.join(config.TMP_DIR, ds.PatientId)
    if not os.path.exists(path):
        os.mkdir(path)

    # Study Folder
    path = os.path.join(path, ds.StudyInstanceUID)
    if not os.path.exists(path):
        os.mkdir(path)

    # Series Folder
    path = os.path.join(path, ds.SeriesInstanceUID)
    if not os.path.exists(path):
        os.mkdir(path)

    path = os.path.join(path, ds.SOPInstanceUID + '.dcm')
    ds.save_as(path, write_like_original=False)
    print(ae_title, 'saved image at', path)

    return 0x0000


def handle_release(event):
    ae_title = utils.get_ae_title(event)
    print(ae_title, 'Released')

    return 0x0000


if __name__ == '__main__':
    ae = AE()
    ae.supported_contexts = AllStoragePresentationContexts
    ae.add_supported_context(VerificationSOPClass)
    handlers = [
        (evt.EVT_C_STORE, handle_store),
        (evt.EVT_ACCEPTED, handle_connection),
        (evt.EVT_RELEASED, handle_release)
    ]

    print("Starting server...")
    print("Waiting for connections...")
    ae.start_server(config.ADDRESS, ae_title=config.AE_TITLE, evt_handlers=handlers)
