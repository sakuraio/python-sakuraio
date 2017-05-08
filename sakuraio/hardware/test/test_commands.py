import unittest
from unittest import mock
import datetime

from sakuraio.hardware.base import culc_parity
from sakuraio.hardware.commands import *
from sakuraio.hardware.dummy import DummySakuraIO
from sakuraio.hardware.exceptions import CommandError, ParityError


class CommandTest(unittest.TestCase):

    def _initial(self, status, response):
        payload = [status, len(response)] + response
        payload.append(culc_parity(payload))

        sakuraio = DummySakuraIO()
        sakuraio.initial(payload)

        return sakuraio

    def test_get_datetime(self):
        sakuraio = self._initial(0x01, [48, 78, 218, 39, 91, 1, 0, 0])
        # 2017-04-01 02:20:40
        self.assertEqual(sakuraio.get_datetime(), datetime.datetime(2017, 4, 1, 4, 51, 10))
        self.assertEqual(sakuraio.values, [CMD_GET_DATETIME, 0, CMD_GET_DATETIME])

    def test_echoback(self):
        values = [232, 143, 222, 88, 0, 0, 0, 0]
        sakuraio = self._initial(0x01, values)
        self.assertEqual(sakuraio.echoback(values), values)
        self.assertEqual(sakuraio.values, [CMD_ECHO_BACK, 8, 232, 143, 222, 88, 0, 0, 0, 0, 230])

    def test_get_adc(self):
        values = [0x54, 0x0b, 0x00, 0x00]
        sakuraio = self._initial(0x01, values)
        self.assertEqual(sakuraio.get_adc(1), 290.0)
        self.assertEqual(sakuraio.values, [CMD_READ_ADC, 1, 1, 16])

        values = [0x54, 0x0b, 0x00, 0x00]
        sakuraio = self._initial(0x01, values)
        self.assertEqual(sakuraio.get_adc(2), 290.0)
        self.assertEqual(sakuraio.values, [CMD_READ_ADC, 1, 2, 19])

    def test_enqueue_tx_raw(self):
        sakuraio = self._initial(0x01, [])
        sakuraio.enqueue_tx_raw(1, "i", [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08])
        self.assertEqual(sakuraio.values, [CMD_TX_ENQUEUE, 10, 1, 105, 1, 2, 3, 4, 5, 6, 7, 8, 74])

    def test_enqueue_tx_raw_with_offset(self):
        sakuraio = self._initial(0x01, [])
        sakuraio.enqueue_tx_raw(1, "i", [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08], -4321)
        self.assertEqual(sakuraio.values, [CMD_TX_ENQUEUE, 18, 1, 105, 1, 2, 3, 4, 5, 6, 7, 8, 31, 239, 255, 255, 255, 255, 255, 255, 162])

    def test_send_immediate_raw(self):
        sakuraio = self._initial(0x01, [])
        sakuraio.send_immediate_raw(1, "i", [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08])
        self.assertEqual(sakuraio.values, [CMD_TX_SENDIMMED, 10, 1, 105, 1, 2, 3, 4, 5, 6, 7, 8, 75])

    def test_get_tx_queue_length(self):
        sakuraio = self._initial(0x01, [23, 14])
        self.assertEqual(sakuraio.get_tx_queue_length(), {'queued': 14, 'available': 23})
        self.assertEqual(sakuraio.values, [CMD_TX_LENGTH, 0, CMD_TX_LENGTH])

    def test_clear_tx(self):
        sakuraio = self._initial(0x01, [])
        sakuraio.clear_tx()
        self.assertEqual(sakuraio.values, [CMD_TX_CLEAR, 0, CMD_TX_CLEAR])

    def test_send(self):
        sakuraio = self._initial(0x01, [])
        sakuraio.send()
        self.assertEqual(sakuraio.values, [CMD_TX_SEND, 0, CMD_TX_SEND])

    def test_get_tx_status(self):
        sakuraio = self._initial(0x01, [0x00, 0x01])
        self.assertEqual(sakuraio.get_tx_status(), {'immediate': 1, 'queue': 0})
        self.assertEqual(sakuraio.values, [CMD_TX_STAT, 0, CMD_TX_STAT])

    def test_dequeue_rx_raw(self):
        sakuraio = self._initial(0x01, [0x01, ord("b"), 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 31, 239, 255, 255, 255, 255, 255, 255])
        self.assertEqual(sakuraio.dequeue_rx_raw(), {'channel': 1, 'data': [1, 2, 3, 4, 5, 6, 7, 8], 'offset': -4321, 'type': 'b'})
        self.assertEqual(sakuraio.values, [CMD_RX_DEQUEUE, 0, CMD_RX_DEQUEUE])

    def test_peek_rx_raw(self):
        sakuraio = self._initial(0x01, [0x01, ord("b"), 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 31, 239, 255, 255, 255, 255, 255, 255])
        self.assertEqual(sakuraio.peek_rx_raw(), {'channel': 1, 'data': [1, 2, 3, 4, 5, 6, 7, 8], 'offset': -4321, 'type': 'b'})
        self.assertEqual(sakuraio.values, [CMD_RX_PEEK, 0, CMD_RX_PEEK])

    def test_get_rx_queue_length(self):
        sakuraio = self._initial(0x01, [23, 14])
        self.assertEqual(sakuraio.get_rx_queue_length(), {'queued': 14, 'available': 23})
        self.assertEqual(sakuraio.values, [CMD_RX_LENGTH, 0, CMD_RX_LENGTH])

    def test_clear_rx(self):
        sakuraio = self._initial(0x01, [])
        sakuraio.clear_rx()
        self.assertEqual(sakuraio.values, [CMD_RX_CLEAR, 0, CMD_RX_CLEAR])

    def test_get_product_id(self):
        sakuraio = self._initial(0x01, [0x02, 0x00])
        self.assertEqual(sakuraio.get_product_id(), 2)
        self.assertEqual(sakuraio.values, [CMD_GET_PRODUCT_ID, 0, CMD_GET_PRODUCT_ID])

    def test_get_product_name(self):
        sakuraio = self._initial(0x01, [0x01, 0x00])
        self.assertEqual(sakuraio.get_product_name(), "SCM-LTE-BETA")
        self.assertEqual(sakuraio.values, [CMD_GET_PRODUCT_ID, 0, CMD_GET_PRODUCT_ID])

        sakuraio = self._initial(0x01, [0x02, 0x00])
        self.assertEqual(sakuraio.get_product_name(), "SCM-LTE-01")
        self.assertEqual(sakuraio.values, [CMD_GET_PRODUCT_ID, 0, CMD_GET_PRODUCT_ID])

    def test_get_unique_id(self):
        sakuraio = self._initial(0x01, [49, 54, 66, 48, 49, 48, 48, 50, 54, 48])
        self.assertEqual(sakuraio.get_unique_id(), "16B0100260")
        self.assertEqual(sakuraio.values, [CMD_GET_UNIQUE_ID, 0, CMD_GET_UNIQUE_ID])

    def test_get_firmware_version(self):
        sakuraio = self._initial(0x01, [49, 54, 66, 48, 49, 48, 48, 50, 54, 48])
        self.assertEqual(sakuraio.get_firmware_version(), "16B0100260")
        self.assertEqual(sakuraio.values, [CMD_GET_FIRMWARE_VERSION, 0, CMD_GET_FIRMWARE_VERSION])

    def test_unlock(self):
        sakuraio = self._initial(0x01, [])
        sakuraio.unlock()
        self.assertEqual(sakuraio.values, [CMD_UNLOCK, 4, 83, 107, 114, 97, 135])

    def test_update_firmware(self):
        sakuraio = self._initial(0x01, [])
        sakuraio.update_firmware()
        self.assertEqual(sakuraio.values, [CMD_UPDATE_FIRMWARE, 0, CMD_UPDATE_FIRMWARE])

    def test_get_firmware_update_status(self):
        sakuraio = self._initial(0x01, [0x04])
        self.assertEqual(sakuraio.get_firmware_update_status(), {'inprogress': False, 'error': 0x04})
        self.assertEqual(sakuraio.values, [CMD_GET_FIRMWARE_UPDATE_STATUS, 0, CMD_GET_FIRMWARE_UPDATE_STATUS])

        sakuraio = self._initial(0x01, [0x80])
        self.assertEqual(sakuraio.get_firmware_update_status(), {'inprogress': True, 'error': 0x00})
        self.assertEqual(sakuraio.values, [CMD_GET_FIRMWARE_UPDATE_STATUS, 0, CMD_GET_FIRMWARE_UPDATE_STATUS])

    def test_reset(self):
        sakuraio = self._initial(0x01, [])
        sakuraio.reset()
        self.assertEqual(sakuraio.values, [CMD_SOFTWARE_RESET, 0, CMD_SOFTWARE_RESET])
