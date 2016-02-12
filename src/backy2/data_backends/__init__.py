#!/usr/bin/env python
# -*- encoding: utf-8 -*-

class DataBackend():
    """ Holds BLOBs, never overwrites
    """

    # Does this filestore support partial reads of blocks?
    #
    # # Does this filestore support partial reads of blocks?
    _SUPPORTS_PARTIAL_READS = False
    _SUPPORTS_PARTIAL_WRITES = False

    def __init__(self, path):
        self.path = path


    def save(self, data):
        """ Saves data, returns unique ID """
        raise NotImplementedError()


    def read(self, uid, offset=0, length=None):
        """ Returns b'<data>' or raises FileNotFoundError.
        With length==None, all known data is read for this uid.
        """
        raise NotImplementedError()


    def rm(self, uid):
        """ Deletes a block """
        raise NotImplementedError()


    def get_all_blob_uids(self):
        """ Get all existing blob uids """
        raise NotImplementedError()


    def close(self):
        pass


