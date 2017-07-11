"""This is a file download program via sakura.io."""
# -*- coding: utf-8 -*-
import sys
import time
#import struct
from datetime import datetime
from sakuraio.hardware.rpi import SakuraIOGPIO
#from sakuraio.hardware.rpi import SakuraIOSMBus

FILEID = 1
FILENAME = "downloaded_file"

def get_file_via_sakuraio(channel):
    """ Single file downlod function. """
    CHUNK_SIZE = [16]
    DELAY_SEC = 1
    filesize = 0
    receivedsize = 0
    filedata = []

    # インスタンス作成
    sakuraio = SakuraIOGPIO()
    #sakuraio = SakuraIOSMBus

    # 一連のファイルダウンロード処理を開始(センター側でダウンロードファイルを取得)
    sakuraio.start_file_download([channel])

    time.sleep(DELAY_SEC)

    # メタデータ(ファイルサイズ等)を取得
    try:
        response = sakuraio.get_file_metadata()
    except:
        #sakuraio.cancel_file_download()
        #del sakuraio
        #sys.exit()
        raise
    else:
        print('Get_file_metadata: Status: {0:x}'.format(response["status"]))
        if response["status"] == 0x81 or response["status"] == 0x82:
            sakuraio.cancel_file_download()
            del sakuraio
            sys.exit()

        filesize = response["size"]
        print('Get_file_metadata: Filesize: {0}'.format(filesize))
        print('Get_file_metadata: Timestamp: {0}'.format(datetime.utcfromtimestamp(response["timestamp"]/1000)))
    
    # ファイルの実体を取得
    while receivedsize < filesize:
        time.sleep(DELAY_SEC)
        try:
            result = sakuraio.get_file_data(CHUNK_SIZE)
        except:
            #sakuraio.cancel_file_download()
            #del sakuraio
            #sys.exit()
            raise
        else:
            filedata.extend(result["data"])
            receivedsize += len(result["data"])
            print('Get_file_data: Length: {0}'.format(len(result["data"])))
            print('Get_file_data: Receivedsize: {0}'.format(receivedsize))

    #print('Get_file_data: Received_data: {0}'.format(filedata))

    del sakuraio

    return filedata

if __name__ == "__main__":

    # ファイルIDを指定してファイル内容をダウンロード
    content = []
    content = get_file_via_sakuraio(FILEID)

    # 取得したファイルの中身を、指定したファイル名で書き込み
    with open(FILENAME, "wb") as fout:
        fout.write(bytearray(content))
