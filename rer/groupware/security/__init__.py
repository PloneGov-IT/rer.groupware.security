# -*- coding: utf-8 -*-

import logging
from zope.i18nmessageid import MessageFactory

groupwaresecurityMessageFactory = MessageFactory('rer.groupware.security')
logger = logging.getLogger('rer.groupware.security')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
