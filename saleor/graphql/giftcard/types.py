from textwrap import dedent

from graphene import relay

from ...giftcard import models
from ..core.connection import CountableDjangoObjectType


class GiftCard(CountableDjangoObjectType):
    class Meta:
        description = dedent(
            """
        The gift card is a prepaid electronic payment card accepted in store.
        They can be used during checkout by providing valid gift
        card codes. """
        )
        only_fields = [
            "code",
            "creator",
            "created",
            "start_date",
            "expiration_date",
            "last_used_on",
            "is_active",
            "initial_balance",
            "current_balance",
        ]
        interfaces = [relay.Node]
        model = models.GiftCard