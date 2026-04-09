# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: proxy_controller.pyc (Python 3.11)

'''
Proxy Controller
외부 이미지 프록시 (CORS 우회)

Endpoints:
- GET /api/proxy/image - 외부 이미지 가져오기
'''
from flask import Blueprint, request, Response
import requests
import logging
logger = logging.getLogger(__name__)
proxy_bp = Blueprint('proxy', __name__)
proxy_image = (lambda :
