Hardware API
============

Common
------

.. automethod:: hardware.commands.common.CommonMixins.get_connection_status()
.. automethod:: hardware.commands.common.CommonMixins.get_is_online()
.. automethod:: hardware.commands.common.CommonMixins.get_connection_error()
.. automethod:: hardware.commands.common.CommonMixins.get_signal_quality()
.. automethod:: hardware.commands.common.CommonMixins.get_datetime()
.. automethod:: hardware.commands.common.CommonMixins.echoback()


Transmit
--------

.. automethod:: hardware.commands.transmit.TransmitMixins.enqueue_tx_raw(channel, type, data, offset=0)
.. automethod:: hardware.commands.transmit.TransmitMixins.send_immediate_raw(channel, type, data)
.. automethod:: hardware.commands.transmit.TransmitMixins.get_tx_queue_length()
.. automethod:: hardware.commands.transmit.TransmitMixins.clear_tx()
.. automethod:: hardware.commands.transmit.TransmitMixins.send()
.. automethod:: hardware.commands.transmit.TransmitMixins.get_tx_status()


Receive
-------

.. automethod:: hardware.commands.receive.ReceiveMixins.dequeue_rx_raw()
.. automethod:: hardware.commands.receive.ReceiveMixins.peek_rx_raw()
.. automethod:: hardware.commands.receive.ReceiveMixins.get_rx_queue_length()
.. automethod:: hardware.commands.receive.ReceiveMixins.clear_rx()


Operation
---------

.. automethod:: hardware.commands.operation.OperationMixins.get_product_id()
.. automethod:: hardware.commands.operation.OperationMixins.get_product_name()
.. automethod:: hardware.commands.operation.OperationMixins.get_unique_id()
.. automethod:: hardware.commands.operation.OperationMixins.get_firmware_version()
.. automethod:: hardware.commands.operation.OperationMixins.unlock()
.. automethod:: hardware.commands.operation.OperationMixins.update_firmware()
.. automethod:: hardware.commands.operation.OperationMixins.get_firmware_update_status()
.. automethod:: hardware.commands.operation.OperationMixins.reset()
