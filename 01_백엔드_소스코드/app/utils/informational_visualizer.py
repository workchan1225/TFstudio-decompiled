# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: informational_visualizer.pyc (Python 3.11)

__doc__ = "\nInformational Visualizer - 정보성 콘텐츠 동적 시각화 엔진\n\n나레이션 내용을 분석하여 최적의 시각화 전략을 결정:\n- 30개 이상의 세분화된 시각화 카테고리\n- 카테고리별 시각화 프로필 (객체, 구도, 조명, 색상)\n- 장르별 최적화된 시각화 선호도\n- 동적 프롬프트 생성\n\nUsage:\n    from app.utils.informational_visualizer import InformationalSceneAnalyzer, DynamicPromptBuilder\n\n    analysis = InformationalSceneAnalyzer.analyze(narration, genre='PSYCHOLOGY')\n    prompt_result = DynamicPromptBuilder.build_prompt(analysis, scene_position='body')\n"
from typing import Dict, List, Optional, TypedDict
from enum import Enum
import random
import re

class VisualCategory(Enum, str):
    '''세분화된 시각화 카테고리 (30개+)'''
    ECONOMY_INFLATION = 'economy_inflation'
    ECONOMY_INVESTMENT = 'economy_investment'
    ECONOMY_SAVINGS = 'economy_savings'
    ECONOMY_REAL_ESTATE = 'economy_real_estate'
    ECONOMY_BUSINESS = 'economy_business'
    ECONOMY_EMPLOYMENT = 'economy_employment'
    SCIENCE_PHYSICS = 'science_physics'
    SCIENCE_CHEMISTRY = 'science_chemistry'
    SCIENCE_BIOLOGY = 'science_biology'
    SCIENCE_NEUROSCIENCE = 'science_neuroscience'
    SCIENCE_ASTRONOMY = 'science_astronomy'
    TECH_AI = 'tech_ai'
    TECH_DIGITAL = 'tech_digital'
    TECH_INNOVATION = 'tech_innovation'
    PSYCHOLOGY_EMOTION = 'psychology_emotion'
    PSYCHOLOGY_COGNITIVE = 'psychology_cognitive'
    PSYCHOLOGY_BEHAVIOR = 'psychology_behavior'
    PSYCHOLOGY_TRAUMA = 'psychology_trauma'
    RELATIONSHIP_FAMILY = 'relationship_family'
    RELATIONSHIP_SOCIAL = 'relationship_social'
    RELATIONSHIP_ROMANTIC = 'relationship_romantic'
    HEALTH_NUTRITION = 'health_nutrition'
    HEALTH_EXERCISE = 'health_exercise'
    HEALTH_MENTAL = 'health_mental'
    HEALTH_DISEASE = 'health_disease'
    HEALTH_AGING = 'health_aging'
    HISTORY_ANCIENT = 'history_ancient'
    HISTORY_MEDIEVAL = 'history_medieval'
    HISTORY_MODERN = 'history_modern'
    HISTORY_WAR = 'history_war'
    CULTURE_TRADITION = 'culture_tradition'
    CULTURE_ART = 'culture_art'
    CULTURE_RELIGION = 'culture_religion'
    NATURE_WEATHER = 'nature_weather'
    NATURE_ECOLOGY = 'nature_ecology'
    NATURE_DISASTER = 'nature_disaster'
    NATURE_WILDLIFE = 'nature_wildlife'
    LIFE_WORK = 'life_work'
    LIFE_EDUCATION = 'life_education'
    LIFE_HOME = 'life_home'
    LIFE_TRAVEL = 'life_travel'
    LIFE_FOOD = 'life_food'
    LIFE_HOBBY = 'life_hobby'
    SOCIETY_CRIME = 'society_crime'
    SOCIETY_JUSTICE = 'society_justice'
    SOCIETY_POLITICS = 'society_politics'
    SOCIETY_MEDIA = 'society_media'
    ABSTRACT_TIME = 'abstract_time'
    ABSTRACT_SUCCESS = 'abstract_success'
    ABSTRACT_FAILURE = 'abstract_failure'
    ABSTRACT_CHANGE = 'abstract_change'
    GENERAL = 'general'

# WARNING: Decompyle incomplete
