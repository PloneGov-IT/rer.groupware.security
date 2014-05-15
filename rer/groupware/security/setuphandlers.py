# -*- coding: utf-8 -*-

from Products.CMFCore.utils import getToolByName
from rer.groupware.security import logger


PROFILE_ID = 'profile-rer.groupware.security:default'

def migrateTo1010(context):
    setup_tool = getToolByName(context, 'portal_setup')
    setup_tool.runAllImportStepsFromProfile('profile-rer.groupware.security:to_1010')
    logger.info('Migrated to version 2.1.2')
