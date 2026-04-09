# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: number_to_korean.pyc (Python 3.11)

__doc__ = '\n숫자 한글화 모듈 - TTS용 숫자 전처리\n\nGoogle TTS (Neural2, Chirp 3 HD)에서 숫자 오발음을 방지하기 위한\n숫자-한글 변환 유틸리티입니다.\n\n지원 기능:\n- 기수 변환: 123 -> "백이십삼"\n- 서수 변환: 1 -> "첫번째"\n- 전화번호: 010-1234-5678 -> "공일공 일이삼사 오륙칠팔"\n- 날짜: 2024-03-15 -> "이천이십사년 삼월 십오일"\n- 금액: 50,000원 -> "오만원"\n- 퍼센트: 50% -> "오십퍼센트"\n- 시간: 14:30 -> "십사시 삼십분"\n\n사용법:\n    from app.utils.number_to_korean import normalize_numbers_for_tts\n\n    # Chirp 3 HD용 (직접 한글 변환)\n    text = normalize_numbers_for_tts("오늘 010-1234-5678로 전화주세요.")\n    # -> "오늘 공일공 일이삼사 오륙칠팔로 전화주세요."\n'
import re
import logging
from typing import Optional
logger = logging.getLogger(__name__)
DIGIT_TO_KOREAN = {
    '0': '영',
    '1': '일',
    '2': '이',
    '3': '삼',
    '4': '사',
    '5': '오',
    '6': '육',
    '7': '칠',
    '8': '팔',
    '9': '구' }
DIGIT_TO_KOREAN_PHONE = {
    '0': '공',
    '1': '일',
    '2': '이',
    '3': '삼',
    '4': '사',
    '5': '오',
    '6': '륙',
    '7': '칠',
    '8': '팔',
    '9': '구' }
UNITS_SMALL = [
    '',
    '십',
    '백',
    '천']
UNITS_LARGE = [
    '',
    '만',
    '억',
    '조',
    '경']
ORDINAL_KOREAN = {
    1: '첫',
    2: '둘',
    3: '셋',
    4: '넷',
    5: '다섯',
    6: '여섯',
    7: '일곱',
    8: '여덟',
    9: '아홉',
    10: '열' }
MONTH_KOREAN = {
    1: '일',
    2: '이',
    3: '삼',
    4: '사',
    5: '오',
    6: '유',
    7: '칠',
    8: '팔',
    9: '구',
    10: '시',
    11: '십일',
    12: '십이' }

def number_to_korean_cardinal(num = None):
    """
    기수 변환: 정수를 한글 기수로 변환

    Args:
        num: 변환할 정수 (0 ~ 9999999999999999)

    Returns:
        한글 기수 문자열

    Examples:
        >>> number_to_korean_cardinal(0)
        '영'
        >>> number_to_korean_cardinal(123)
        '백이십삼'
        >>> number_to_korean_cardinal(50000)
        '오만'
        >>> number_to_korean_cardinal(12345678)
        '천이백삼십사만오천육백칠십팔'
    """
    if num == 0:
        return '영'
    if None < 0:
        return '마이너스 ' + number_to_korean_cardinal(abs(num))
    result = None
    str_num = str(num)
    length = len(str_num)
    groups = []
# WARNING: Decompyle incomplete


def _convert_four_digits(num = None):
    '''4자리 이하 숫자를 한글로 변환 (내부 함수)'''
    if num == 0:
        return ''
    result = None
    str_num = str(num).zfill(4)
    for i, digit in enumerate(str_num):
        if digit == '0':
            continue
        unit_idx = 3 - i
        digit_val = int(digit)
        if digit_val == 1 and unit_idx > 0:
            result.append(UNITS_SMALL[unit_idx])
            continue
        result.append(DIGIT_TO_KOREAN[digit] + UNITS_SMALL[unit_idx])
        return ''.join(result)


def number_to_korean_ordinal(num = None):
    '''
    서수 변환: 숫자를 한글 서수로 변환

    Args:
        num: 변환할 정수 (1 ~ )

    Returns:
        한글 서수 문자열 (예: "첫번째", "두번째")

    Examples:
        >>> number_to_korean_ordinal(1)
        \'첫번째\'
        >>> number_to_korean_ordinal(2)
        \'두번째\'
        >>> number_to_korean_ordinal(15)
        \'열다섯번째\'
    '''
    if num <= 0:
        return f'''{num}번째'''
    if None <= 10:
        return ORDINAL_KOREAN.get(num, f'''{num}''') + '번째'
    if None <= 19:
        ones = num - 10
        if ones == 0:
            return '열번째'
        return None + ORDINAL_KOREAN.get(ones, f'''{ones}''') + '번째'
    return None(num) + '번째'


def phone_to_korean(phone = None):
    '''
    전화번호를 한글로 변환 (0을 \'공\'으로 발음)

    Args:
        phone: 전화번호 문자열 (예: "010-1234-5678", "02-123-4567")

    Returns:
        한글 발음 문자열 (예: "공일공 일이삼사 오륙칠팔")

    Examples:
        >>> phone_to_korean("010-1234-5678")
        \'공일공 일이삼사 오륙칠팔\'
        >>> phone_to_korean("02-123-4567")
        \'공이 일이삼 사오륙칠\'
    '''
    parts = re.split('[-.\\s]', phone)
    result_parts = []
    for part in parts:
        if not part:
            continue
        korean_part = (lambda .0: pass# WARNING: Decompyle incomplete
)(part())
        result_parts.append(korean_part)
        return ' '.join(result_parts)


def date_to_korean(date_str = None):
    '''
    날짜를 한글로 변환

    Args:
        date_str: 날짜 문자열 (예: "2024-03-15", "2024년 3월 15일")

    Returns:
        한글 발음 문자열 (예: "이천이십사년 삼월 십오일")

    Examples:
        >>> date_to_korean("2024-03-15")
        \'이천이십사년 삼월 십오일\'
        >>> date_to_korean("2024년 3월 15일")
        \'이천이십사년 삼월 십오일\'
    '''
    match = re.match('(\\d{4})[-/.](\\d{1,2})[-/.](\\d{1,2})', date_str)
    if match:
        day = int(match.group(3))
        month = int(match.group(2))
        year = int(match.group(1))
        return f'''{number_to_korean_cardinal(year)}년 {MONTH_KOREAN.get(month, number_to_korean_cardinal(month))}월 {number_to_korean_cardinal(day)}일'''
    match = None.match('(\\d{4})년\\s*(\\d{1,2})월\\s*(\\d{1,2})일', date_str)
    if match:
        day = int(match.group(3))
        month = int(match.group(2))
        year = int(match.group(1))
        return f'''{number_to_korean_cardinal(year)}년 {MONTH_KOREAN.get(month, number_to_korean_cardinal(month))}월 {number_to_korean_cardinal(day)}일'''


def money_to_korean(money_str = None):
    '''
    금액을 한글로 변환

    Args:
        money_str: 금액 문자열 (예: "50,000원", "1,234,567원", "100만원")

    Returns:
        한글 발음 문자열 (예: "오만원", "백이십삼만사천오백육십칠원")

    Examples:
        >>> money_to_korean("50,000원")
        \'오만원\'
        >>> money_to_korean("1,234,567원")
        \'백이십삼만사천오백육십칠원\'
        >>> money_to_korean("100만원")
        \'백만원\'
    '''
    clean = money_str.replace(',', '')
    match = re.match('(\\d+)(만|억|조)원', clean)
    if match:
        num = int(match.group(1))
        unit = match.group(2)
        return number_to_korean_cardinal(num) + unit + '원'
    match = None.match('(\\d+)원', clean)
    if match:
        num = int(match.group(1))
        return number_to_korean_cardinal(num) + '원'
    match = None.match('(\\d+)', clean)
    if match:
        num = int(match.group(1))
        return number_to_korean_cardinal(num)


def percent_to_korean(percent_str = None):
    '''
    퍼센트를 한글로 변환

    Args:
        percent_str: 퍼센트 문자열 (예: "50%", "3.14%")

    Returns:
        한글 발음 문자열 (예: "오십퍼센트", "삼점일사퍼센트")

    Examples:
        >>> percent_to_korean("50%")
        \'오십퍼센트\'
        >>> percent_to_korean("3.14%")
        \'삼점일사퍼센트\'
    '''
    match = re.match('(\\d+)(?:\\.(\\d+))?%', percent_str)
    if match:
        integer_part = int(match.group(1))
        decimal_part = match.group(2)
        result = number_to_korean_cardinal(integer_part)
        if decimal_part:
            result += '점'
            for digit in decimal_part:
                result += DIGIT_TO_KOREAN[digit]
                return result + '퍼센트'
                return percent_str


def time_to_korean(time_str = None):
    '''
    시간을 한글로 변환

    Args:
        time_str: 시간 문자열 (예: "14:30", "9시 30분")

    Returns:
        한글 발음 문자열 (예: "십사시 삼십분", "아홉시 삼십분")

    Examples:
        >>> time_to_korean("14:30")
        \'십사시 삼십분\'
        >>> time_to_korean("9:05")
        \'아홉시 오분\'
    '''
    match = re.match('(\\d{1,2}):(\\d{2})', time_str)
    if match:
        minute = int(match.group(2))
        hour = int(match.group(1))
        result = number_to_korean_cardinal(hour) + '시'
        if minute > 0:
            result += ' ' + number_to_korean_cardinal(minute) + '분'
        return result
    match = None.match('(\\d{1,2})시\\s*(\\d{1,2})분', time_str)
    if match:
        minute = int(match.group(2))
        hour = int(match.group(1))
        return number_to_korean_cardinal(hour) + '시 ' + number_to_korean_cardinal(minute) + '분'


def digits_to_korean_individual(digits = None):
    '''
    숫자를 개별 발음으로 변환 (전화번호 스타일)

    Args:
        digits: 숫자 문자열 (예: "1234")

    Returns:
        개별 발음 문자열 (예: "일이삼사")

    Examples:
        >>> digits_to_korean_individual("1234")
        \'일이삼사\'
        >>> digits_to_korean_individual("007")
        \'공공칠\'
    '''
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(digits())

# WARNING: Decompyle incomplete
