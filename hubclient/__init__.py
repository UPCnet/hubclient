# -*- coding: utf-8 -*-
from maxclient.rest import MaxClient
from hubclient.routes import ROUTES


class HubClient(MaxClient):
    __routes__ = ROUTES
    __defaults__ = {}

