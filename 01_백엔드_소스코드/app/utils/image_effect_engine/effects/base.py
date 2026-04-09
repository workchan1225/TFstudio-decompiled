# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

'''
효과 베이스 클래스

모든 효과는 이 클래스를 상속받아 구현
핵심: cv2.warpAffine을 사용한 서브픽셀 정밀도 변환
'''
from abc import ABC, abstractmethod
from typing import Tuple
import numpy as np
import cv2
from easing import get_easing

class BaseEffect(ABC):
    '''
    모든 효과의 베이스 클래스

    서브클래스는 get_transform() 메서드를 구현하여
    특정 진행 시점의 affine 변환 행렬을 반환해야 함
    '''
    
    def __init__(self = None, settings = None):
        """
        Args:
            settings: 효과 설정 딕셔너리
                - easing: 이징 함수 이름 (기본: 'ease_in_out')
                - 기타 효과별 설정
        """
        self.settings = settings
        self.easing_name = settings.get('easing', 'ease_in_out')
        self._easing_fn = get_easing(self.easing_name)

    
    def ease(self = None, t = None):
        '''이징 함수 적용'''
        return self._easing_fn(t)

    get_transform = (lambda self = None, progress = None, image_size = abstractmethod, output_size = ('progress', float, 'image_size', Tuple[(int, int)], 'output_size', Tuple[(int, int)], 'return', np.ndarray): pass)()
    
    def apply(self = None, image = None, progress = None, output_size = (cv2.INTER_LANCZOS4,), interpolation = ('image', np.ndarray, 'progress', float, 'output_size', Tuple[(int, int)], 'interpolation', int, 'return', np.ndarray)):
        '''
        이미지에 효과 적용

        서브픽셀 정밀도를 위해 INTER_LANCZOS4 (고품질) 사용
        성능이 중요한 경우 INTER_LINEAR 사용 가능

        Args:
            image: 입력 이미지 (BGR 형식)
            progress: 효과 진행률 (0.0 ~ 1.0)
            output_size: 출력 크기 (width, height)
            interpolation: 보간 방법 (기본: LANCZOS4)

        Returns:
            효과가 적용된 이미지
        '''
        (h, w) = image.shape[:2]
        (out_w, out_h) = output_size
        transform = self.get_transform(progress, (w, h), output_size)
        return cv2.warpAffine(image, transform, (out_w, out_h), flags = interpolation, borderMode = cv2.BORDER_CONSTANT, borderValue = (0, 0, 0))

    
    def prepare_image(self = None, image = None, output_size = None, fit_mode = ('cover',)):
        """
        효과 적용 전 이미지 전처리

        Args:
            image: 원본 이미지
            output_size: 출력 크기 (width, height)
            fit_mode: 맞춤 모드 ('cover', 'contain', 'fill')

        Returns:
            전처리된 이미지
        """
        (h, w) = image.shape[:2]
        (out_w, out_h) = output_size
        if fit_mode == 'fill':
            return cv2.resize(image, (out_w, out_h), interpolation = cv2.INTER_LANCZOS4)
        scale_w = None / w
        scale_h = out_h / h
        if fit_mode == 'cover':
            scale = max(scale_w, scale_h)
        else:
            scale = min(scale_w, scale_h)
        new_w = int(w * scale)
        new_h = int(h * scale)
        resized = cv2.resize(image, (new_w, new_h), interpolation = cv2.INTER_LANCZOS4)
        canvas = np.zeros((out_h, out_w, 3), dtype = np.uint8)
        x_offset = (out_w - new_w) // 2
        y_offset = (out_h - new_h) // 2
        src_x1 = max(0, -x_offset)
        src_y1 = max(0, -y_offset)
        src_x2 = min(new_w, out_w - x_offset)
        src_y2 = min(new_h, out_h - y_offset)
        dst_x1 = max(0, x_offset)
        dst_y1 = max(0, y_offset)
        dst_x2 = dst_x1 + (src_x2 - src_x1)
        dst_y2 = dst_y1 + (src_y2 - src_y1)
        canvas[(dst_y1:dst_y2, dst_x1:dst_x2)] = resized[(src_y1:src_y2, src_x1:src_x2)]
        return canvas

    create_identity_transform = (lambda : np.array([
[
1,
0,
0],
[
0,
1,
0]], dtype = np.float32))()
    create_scale_transform = (lambda scale = None, center = None, output_size = staticmethod: (cx, cy) = center(out_w, out_h) = output_sizetx = out_w / 2 - cx * scalety = out_h / 2 - cy * scalenp.array([
[
scale,
0,
tx],
[
0,
scale,
ty]], dtype = np.float32))()
    create_rotation_transform = (lambda angle_deg = None, center = None, scale = staticmethod: cv2.getRotationMatrix2D(center, angle_deg, scale))()
