# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer

import Products.ZLDAPMedthod


class ZLDAPMedthodLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=Products.ZLDAPMedthod)


ZLDAPMedthod_FIXTURE = ZLDAPMedthodLayer()

ZLDAPMedthod_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ZLDAPMedthod_FIXTURE,),
    name='ZLDAPMedthodLayer:IntegrationTesting',
)
