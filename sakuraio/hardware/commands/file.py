import struct
import datetime

# File Download
CMD_START_FILE_DOWNLOAD = 0x40
CMD_GET_FILE_METADATA = 0x41
CMD_GET_FILE_DOWNLOAD_STATUS = 0x42
CMD_CANCEL_FILE_DOWNLOAD = 0x43
CMD_GET_FILE_DATA = 0x44


class FileMixins(object):

    def start_file_download(self, fileid):
        """Start file download

        :param list fileid:
            FileID. List length must be 1, the Value fileid[0] must be 1 to 5.

        """

        fileid += [0x00] * 2
        self.execute_command(CMD_START_FILE_DOWNLOAD, fileid[:2])

    def get_file_metadata(self):
        """Get file metadata

        :return: Dict of file metadata (status, filesize, timestamp, checksum).
        :rtype: dict
        """

        response = self.execute_command(CMD_GET_FILE_METADATA)
        return {
            "status": response[0],
            "size": struct.unpack("<i", struct.pack("4B", *response[1:5]))[0],
            "timestamp": struct.unpack("<q", struct.pack("8B", *response[5:13]))[0],
            "checksum": response[13:17],
        }

    def get_file_download_status(self):
        """Get file download status

        :return: Dict of download status and received datasize.
        :rtype: dict
        """

        response = self.execute_command(CMD_GET_FILE_DOWNLOAD_STATUS)
        return {
            "status": response[0],
            "size": struct.unpack("<i", struct.pack("4B", *response[1:5]))[0],
        }

    def cancel_file_download(self):
        """Cancel file download"""

        self.execute_command(CMD_CANCEL_FILE_DOWNLOAD)

    def get_file_data(self, rsize):
        """Get file data

        :return: Dict of download file body.abs
        :rtype: dict
        """

        response = self.execute_command(CMD_GET_FILE_DATA, rsize[0:1])
        return {
            "data": response[0:]
        }
