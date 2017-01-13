""" The purpose of this module is to test the NetworkHint object """

# import pytest
# from unittests.mock import MagicMock

import unittest

from regioneer.core.hints import HintFactory, constants
from regioneer.core.hints.LocalityHint import LocalityHint
from regioneer.core.hints.NetworkHint import NetworkHint, WifiHint, EthernetHint
from regioneer.core.hints.PhysicalHint import PhysicalHint

from regioneer.unittests.constants import TEST_WIFI_REQS, TEST_ETHERNET_REQS, TEST_WIFI_SSID, \
                                          TEST_SURROUNDING_SSIDS


class TestLocationHint(unittest.TestCase):
    """ Test the NetworkHint object"""

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_hint_factory(self):
        """ This testcase is meant to test the HintFactory class to make sure it is instantiating
        the corrgect classes. """

        network_hint  = HintFactory.factory(constants.NETWORK, constants.NETWORK_HINT_REQS)
        locality_hint = HintFactory.factory(constants.LOCALITY, constants.LOCALITY_HINT_REQS)
        physical_hint = HintFactory.factory(constants.PHYSICAL, constants.PHYSICAL_HINT_REQS)

        assert isinstance(network_hint, NetworkHint)
        assert isinstance(locality_hint, LocalityHint)
        assert isinstance(physical_hint, PhysicalHint)


class TestWiFiHint(unittest.TestCase):
    """ Test the subclassed WiFiHint """

    def test_get_ssid(self):
        """" Test getting the ssid for a given device. """

        wifi_hint = WifiHint(requirements=TEST_WIFI_REQS)
        ssid = wifi_hint.get_connected_ssid()

        print("Method gives: {}".format(ssid))
        print("Constant gives: {}".format(TEST_WIFI_SSID))

        self.assertTrue( ssid == TEST_WIFI_SSID )

    def test_get_surround_ssids(self):
        """ Test getting the surrounding ssids """

        wifi_hint = WifiHint(requirements=TEST_WIFI_REQS)
        ssids = wifi_hint.get_surrounding_ssids()

        valid_ssids = [s for s in ssids if s in TEST_SURROUNDING_SSIDS]

        threshold = 4

        print(len(TEST_SURROUNDING_SSIDS) - len(valid_ssids))

        self.assertTrue(len(TEST_SURROUNDING_SSIDS) - len(valid_ssids) < threshold)


class TestEthernetHint(unittest.TestCase):
    """ Test teh subclassed EthernetHint """

    def test_network_check(self):
        """ Test the implementation of the NetworkHint abstract method """

