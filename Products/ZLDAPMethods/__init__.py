""" LDAP Filter Methods Package
"""
from .testing import ZLDAPMethodLayer
from . import LM


def initialize(context):
    """initialize.

    :param context:
    """
    context.registerClass(
        LM.LDAPFilter,
        constructors=(LM.manage_addZLDAPMethodForm,
                      LM.manage_addZLDAPMethod),
        icon="LDAP_Method_icon.gif",
        legacy=(LM.LDAPConnectionIDs,),
    )
    context.test_layer = ZLDAPMethodLayer
