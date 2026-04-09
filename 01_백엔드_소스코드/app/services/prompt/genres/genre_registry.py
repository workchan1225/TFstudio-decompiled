# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: genre_registry.pyc (Python 3.11)

'''
GenreRegistry - 장르 레지스트리

모든 장르를 등록하고 관리하는 싱글톤 레지스트리.
장르 코드로 장르 인스턴스를 조회하거나,
카테고리별 장르 목록을 가져올 수 있음.
'''
from typing import Dict, List, Optional
from base_genre import BaseGenre, GenreCategory
from drama_genres import DramaticGenre, RevengeGenre, TouchingGenre, ConfessionGenre, MysteryGenre, ThrillerGenre, SfFantasyGenre, HistoricalGenre, HeartWarmingGenre, JoseonFolktaleGenre, LifeLessonsGenre, LifeChallengeGenre, ConspiracyGenre, NationalPrideGenre, MunchkinGenre, MuhyupGenre
from info_genres import LifeKnowledgeGenre, OfficeSurvivalGenre, MoneySenseGenre, RelationshipEqGenre, PsychologyGenre, LifeChoicesGenre, KnowledgeBiteGenre
from docu_genres import TrueStoryGenre, DocumentaryGenre, NewsReportGenre, ReviewAnalysisGenre, VarietyGenre, HybridGenre

class GenreRegistry:
    pass
# WARNING: Decompyle incomplete

_registry = None

def get_genre_registry():
    '''
    GenreRegistry 싱글톤 인스턴스 가져오기

    Returns:
        GenreRegistry 인스턴스
    '''
    pass
# WARNING: Decompyle incomplete
