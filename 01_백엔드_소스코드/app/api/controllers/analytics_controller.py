# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: analytics_controller.pyc (Python 3.11)

'''
Analytics API - 분석 통계 엔드포인트
'''
from flask import Blueprint, request, jsonify
from app.services.analytics_service import AnalyticsService
analytics_controller_bp = Blueprint('analytics', __name__)
get_overview = (lambda : period = request.args.get('period', 'month')if period not in ('week', 'month', 'year'):
period = 'month'try:
stats = AnalyticsService.get_overview_stats(period)(jsonify(stats), 200)except Exception:
e = Nonedel eNoneNone = del e)()
get_timeline = (lambda : period = request.args.get('period', 'month')if period not in ('week', 'month', 'year'):
period = 'month'try:
timeline = AnalyticsService.get_projects_timeline(period)(jsonify({
'timeline': timeline }), 200)except Exception:
e = Nonedel eNoneNone = del e)()
get_recent_projects = (lambda : try:
limit = int(request.args.get('limit', 10))limit = min(max(1, limit), 50)except ValueError:
limit = 10try:
projects = AnalyticsService.get_recent_projects(limit)(jsonify({
'projects': projects }), 200)except Exception:
e = Nonedel eNoneNone = del e)()
get_top_projects = (lambda : try:
limit = int(request.args.get('limit', 5))limit = min(max(1, limit), 20)except ValueError:
limit = 5try:
projects = AnalyticsService.get_top_projects(limit)(jsonify({
'projects': projects }), 200)except Exception:
e = Nonedel eNoneNone = del e)()
get_project_analytics = (lambda project_id: try:
analytics = AnalyticsService.get_project_analytics(project_id)if not analytics:
(jsonify({
'error': 'Project not found' }), 404)(None(analytics), 200)except Exception:
e = Nonedel eNoneNone = del e)()
get_resource_usage = (lambda : period = request.args.get('period', 'month')if period not in ('week', 'month', 'year'):
period = 'month'try:
usage = AnalyticsService.get_resource_usage(period)(jsonify(usage), 200)except Exception:
e = Nonedel eNoneNone = del e)()
get_productivity = (lambda : period = request.args.get('period', 'month')if period not in ('week', 'month', 'year'):
period = 'month'try:
stats = AnalyticsService.get_productivity_stats(period)(jsonify(stats), 200)except Exception:
e = Nonedel eNoneNone = del e)()
get_project_media_details = (lambda project_id: try:
details = AnalyticsService.get_project_media_details(project_id)if not details:
(jsonify({
'error': 'Project not found' }), 404)(None(details), 200)except Exception:
e = Nonedel eNoneNone = del e)()
get_project_history = (lambda project_id: try:
history = AnalyticsService.get_project_history(project_id)if not history:
(jsonify({
'error': 'Project not found' }), 404)(None(history), 200)except Exception:
e = Nonedel eNoneNone = del e)()
get_project_ai_usage = (lambda project_id: try:
usage = AnalyticsService.get_project_ai_usage(project_id)if not usage:
(jsonify({
'error': 'Project not found' }), 404)(None(usage), 200)except Exception:
e = Nonedel eNoneNone = del e)()
