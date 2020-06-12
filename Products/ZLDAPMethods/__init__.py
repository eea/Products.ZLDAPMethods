""" LDAP Filter Methods Package
"""
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
