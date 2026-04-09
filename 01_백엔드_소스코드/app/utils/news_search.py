# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: news_search.pyc (Python 3.11)

'''
뉴스 검색 유틸리티

사회문제 장르 제목 생성 시 최신 뉴스를 검색하여 컨텍스트 제공.
RSS 피드 기반으로 API 키 없이 동작.
'''
import feedparser
import logging
from datetime import datetime
from typing import List, Dict, Optional
from urllib.parse import quote
logger = logging.getLogger(__name__)
GOOGLE_NEWS_RSS_KR = 'https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko'
GOOGLE_NEWS_SEARCH_RSS_KR = 'https://news.google.com/rss/search?q={query}&hl=ko&gl=KR&ceid=KR:ko'

def search_news(query = None, max_results = None):
    '''
    뉴스 검색 (Google News RSS 활용)

    Args:
        query: 검색어 (예: "저출산", "주거 문제"). None이면 최신 뉴스 반환
        max_results: 최대 결과 수

    Returns:
        뉴스 목록 [{title, link, published, source}, ...]
    '''
    
    try:
        if query and query.strip():
            encoded_query = quote(query.strip())
            feed_url = GOOGLE_NEWS_SEARCH_RSS_KR.format(query = encoded_query)
        else:
            feed_url = GOOGLE_NEWS_RSS_KR
        feed = feedparser.parse(feed_url)
        if feed.bozo:
            logger.warning(f'''[NewsSearch] RSS 파싱 경고: {feed.bozo_exception}''')
        results = []
        for entry in feed.entries[:max_results]:
            results.append({
                'title': entry.get('title', ''),
                'link': entry.get('link', ''),
                'published': entry.get('published', ''),
                'source': _extract_source(entry.get('source', { }).get('title', '')) })
            logger.info(f'''[NewsSearch] \'{query}\' 검색 결과: {len(results)}건''')
            return results
            except Exception:
                e = None
                logger.error(f'''[NewsSearch] 검색 실패: {e}''')
                del e
                return None
                None = 
                del e



def get_social_issues_context(topic = None):
    '''
    사회문제 장르용 최신 뉴스 컨텍스트 생성

    Args:
        topic: 특정 토픽 (없으면 일반 사회 이슈 검색)

    Returns:
        AI 프롬프트에 추가할 컨텍스트 문자열
    '''
    today = datetime.now().strftime('%Y년 %m월 %d일')
    if topic and topic.strip():
        search_queries = [
            topic]
    else:
        search_queries = [
            '사회문제',
            '한국 이슈']
    all_news = []
    for query in search_queries:
        news = search_news(query, max_results = 3)
        all_news.extend(news)
        if not all_news:
            return f'''\n[최신 사회 이슈 정보]\n- 검색일: {today}\n- 참고: 최신 뉴스 검색에 실패했습니다. 일반적인 사회문제를 다뤄주세요.\n'''
        seen_titles = None()
        unique_news = []
        for item in all_news:
            if item['title'] not in seen_titles:
                seen_titles.add(item['title'])
                unique_news.append(item)
            news_lines = []
            for i, item in enumerate(unique_news[:5], 1):
                source = f''' ({item['source']})''' if item['source'] else ''
                news_lines.append(f'''{i}. {item['title']}{source}''')
                context = f'''\n[최신 사회 이슈 정보 - {today}]\n아래는 오늘 날짜 기준 최신 뉴스입니다. 이 이슈들을 참고하여 시의성 있는 제목을 생성하세요.\n\n{chr(10).join(news_lines)}\n\n위 뉴스 중 시청자 관심을 끌 수 있는 주제를 선택하거나, 관련 이슈를 확장하여 제목을 생성하세요.\n'''
                return context


def _extract_source(source_text = None):
    '''
    뉴스 소스에서 언론사 이름 추출

    Args:
        source_text: RSS의 source 텍스트

    Returns:
        정제된 언론사 이름
    '''
    if not source_text:
        return ''
    return None.strip()
