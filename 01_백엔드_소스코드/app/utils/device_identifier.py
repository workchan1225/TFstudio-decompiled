# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: device_identifier.pyc (Python 3.11)

'''
Device Identifier - 기기 고유 식별자 생성
동시접속 방지를 위한 컴퓨터별 고유 ID 생성
'''
import uuid
import hashlib
import platform
import logging
from pathlib import Path
from typing import Tuple
logger = logging.getLogger(__name__)

def _get_mac_address():
    '''MAC 주소 가져오기'''
    
    try:
        mac = uuid.getnode()
        if (mac >> 40) % 2 == 0:
            return format(mac, '012x')
    except Exception:
        e = None
        logger.warning(f'''Failed to get MAC address: {e}''')
        e = None
        del e
    except:
        e = None
        del e

    return ''


def _get_machine_guid():
    '''Windows Machine GUID 가져오기 (레지스트리)'''
    
    try:
        if platform.system() == 'Windows':
            import winreg
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\Cryptography', 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY)
            (machine_guid, _) = winreg.QueryValueEx(key, 'MachineGuid')
            winreg.CloseKey(key)
            return machine_guid
    except Exception:
        e = None
        logger.warning(f'''Failed to get Machine GUID: {e}''')
        e = None
        del e
    except:
        e = None
        del e

    return ''


def _get_install_uuid(data_dir = None):
    '''앱 설치 UUID (최초 설치 시 생성)'''
    uuid_file = data_dir / 'device_uuid'
    
    try:
        if uuid_file.exists():
            return uuid_file.read_text(encoding = 'utf-8').strip()
        new_uuid = None(uuid.uuid4())
        uuid_file.parent.mkdir(parents = True, exist_ok = True)
        uuid_file.write_text(new_uuid, encoding = 'utf-8')
        logger.info(f'''Created new device UUID: {new_uuid[:8]}...''')
        return new_uuid
    except Exception:
        e = None
        logger.error(f'''Failed to get/create install UUID: {e}''')
        del e
        return None
        None = 
        del e



def get_device_id():
    '''
    고유 기기 ID 생성

    조합: MAC 주소 + Machine GUID + 설치 UUID
    해시하여 64자 hex string 반환

    Returns:
        str: 64자 hex string (SHA-256)
    '''
    get_data_path = get_data_path
    import app.config.paths
    mac = _get_mac_address()
    machine_guid = _get_machine_guid()
    install_uuid = _get_install_uuid(get_data_path())
    combined = f'''{mac}:{machine_guid}:{install_uuid}'''
    device_id = hashlib.sha256(combined.encode('utf-8')).hexdigest()
    logger.debug(f'''Generated device ID: {device_id[:16]}...''')
    return device_id


def get_device_name():
    '''
    기기 이름 생성 (사용자에게 표시용)

    형식: "Windows PC - ComputerName"

    Returns:
        str: 기기 이름
    '''
    
    try:
        os_name = platform.system()
        if not platform.node():
            node_name = 'Unknown'
            if os_name == 'Windows':
                return f'''Windows PC - {node_name}'''
            if None == 'Darwin':
                return f'''Mac - {node_name}'''
            if None == 'Linux':
                return f'''Linux - {node_name}'''
            return f'''{None} - {node_name}'''
        except Exception:
            e = None
            logger.error(f'''Failed to get device name: {e}''')
            e = None
            del e
            return 'Unknown Device'
            e = None
            del e



def get_device_info():
    '''
    기기 ID와 이름을 함께 반환

    Returns:
        tuple: (device_id, device_name)
    '''
    return (get_device_id(), get_device_name())
