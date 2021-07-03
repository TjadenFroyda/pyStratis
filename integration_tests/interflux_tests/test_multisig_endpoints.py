import pytest
from pystratis.api.multisig.responsemodels import *
from pystratis.core.types import Address, Money
from pystratis.core import Recipient, MultisigSecret
from pystratis.core.networks import StraxRegTest


@pytest.mark.skip(reason='Unable to test in regtest environment.')
@pytest.mark.integration_test
@pytest.mark.interflux_integration_test
def test_build_transaction(interflux_strax_node, generate_p2pkh_address):
    response = interflux_strax_node.multisig.build_transaction(
        recipients=[
            Recipient(
                destination_address=Address(address=generate_p2pkh_address(network=StraxRegTest()), network=StraxRegTest()),
                subtraction_fee_from_amount=True, amount=Money(5)
            )
        ],
        secrets=[MultisigSecret(mnemonic='mnemonic', passphrase='passphrase')]
    )
    assert isinstance(response, BuildTransactionModel)
