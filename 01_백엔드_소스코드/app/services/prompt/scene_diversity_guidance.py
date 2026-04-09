# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scene_diversity_guidance.pyc (Python 3.11)

__doc__ = '\nConservative scene diversity guidance helpers.\n\nKeeps character/style continuity while nudging shot/layout variety between scenes.\n'
from __future__ import annotations
import hashlib
from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional
from scene.scene_framing_policy import resolve_scene_composition_subject_count
SHOT_VARIANTS = [
    'wide shot',
    'medium wide shot',
    'medium shot',
    'medium close-up',
    'close-up',
    'extreme close-up']
ANGLE_VARIANTS = [
    'eye-level framing',
    'slightly low-angle framing',
    'slightly high-angle framing',
    'dutch angle framing',
    'over-the-shoulder framing',
    "bird's-eye framing"]
SUBJECT_PLACEMENT_VARIANTS = [
    'off-center rule-of-thirds placement',
    'motivated center placement',
    'diagonal staging with depth',
    'foreground framing element with depth']
SINGLE_ORIENTATION_VARIANTS = [
    'three-quarter orientation',
    'profile orientation',
    'back-three-quarter orientation',
    '45-degree turned stance']
GROUP_LAYOUT_VARIANTS = [
    'staggered depth blocking',
    'asymmetric spacing',
    'triangular blocking',
    'diagonal left-to-right blocking']
LIGHTING_MOOD_VARIANTS = [
    'soft side-key with gentle fill',
    'window-side natural key light',
    'subtle rim light with ambient fill',
    'soft overhead key with mild shadow falloff',
    'directional side light with strong silhouette separation']
CAMERA_MOVEMENT_VARIANTS = [
    'static',
    'pan',
    'tilt',
    'dolly']
SINGLE_SHOT_ROTATION = [
    'medium wide shot',
    'close-up',
    'wide shot',
    'medium close-up',
    'medium shot',
    'extreme close-up']
MULTI_SHOT_ROTATION = [
    'wide shot',
    'medium close-up',
    'medium shot',
    'close-up',
    'medium wide shot']
SINGLE_ANGLE_ROTATION = [
    'slightly low-angle framing',
    'over-the-shoulder framing',
    'slightly high-angle framing',
    'dutch angle framing',
    'eye-level framing',
    "bird's-eye framing"]
MULTI_ANGLE_ROTATION = [
    'over-the-shoulder framing',
    'slightly low-angle framing',
    'slightly high-angle framing',
    'eye-level framing',
    'dutch angle framing']
SINGLE_CAMERA_MOVEMENT_ROTATION = [
    'dolly',
    'pan',
    'tilt',
    'static',
    'dolly',
    'pan']
MULTI_CAMERA_MOVEMENT_ROTATION = [
    'pan',
    'dolly',
    'tilt',
    'static',
    'pan']
SINGLE_GAZE_VARIANTS = [
    'off-camera gaze toward a scene trigger',
    'object-focused gaze tied to a prop or evidence surface',
    'downward reflective gaze with attention on hands or page',
    'looking past camera line toward distant environment']
MULTI_GAZE_VARIANTS = [
    'reciprocal eye-line between characters',
    'one character initiates and another visibly reacts',
    'shared focus on a scene object between characters',
    'over-the-shoulder attention line instead of front-facing symmetry']
SINGLE_ACTION_BEAT_VARIANTS = [
    'reaching toward a scene object with visible weight shift',
    'turning mid-explanation with one hand indicating evidence',
    'leaning into a desk, window, or railing with one anchoring hand',
    'handling a book, page, model, or device instead of standing idle',
    'captured during a mid-turn or step transition rather than a static pose']
MULTI_ACTION_BEAT_VARIANTS = [
    'one character initiates a gesture while the other reacts in the same beat',
    'conversation staged through unequal gestures and staggered body angles',
    'shared interaction with a prop or document instead of parallel standing',
    'a visible push-pull of attention between characters and scene object']
DYNAMIC_MOVEMENT_VARIANTS = [
    'freeze-frame mid-gesture',
    'mid-turn transitional pose',
    'one-step weight shift',
    'hand-to-object interaction',
    'reaction beat with torso rotation']
DETAIL_FOCUS_VARIANTS = [
    'hands interacting with a key prop',
    'screen, page, or chart detail while keeping subject presence',
    'reflection or glass-layer composition',
    'micro-expression and eye-line detail',
    'foreground prop depth anchor near the subject']
ENVIRONMENT_ANCHOR_VARIANTS = [
    'keep the same story domain while varying foreground and depth planes',
    'preserve the location family but change the active surface or prop lane',
    'anchor variation around the same environment with a different action hotspot',
    'change framing grammar without changing the world, topic, or set logic']
STORY_READABILITY_VARIANTS = [
    'one clear subject-action-object chain should explain the scene at a glance',
    'human action must read before atmosphere or decorative props',
    'the frame should communicate readable cause-and-effect in a single glance',
    'one dominant event lane should explain who is doing what and why this moment matters']
WEAK_ACTION_MARKERS = ('stand', 'standing', 'sit', 'sitting', 'look', 'looking', 'watching', 'talk', 'talking', 'speak', 'speaking', 'being', '있다', '서있', '서 있다', '앉아있', '앉아 있다', '바라보', '쳐다보', '말하', '대화하')
STRONG_ACTION_MARKERS = ('reach', 'reaching', 'point', 'pointing', 'lean', 'leaning', 'turn', 'turning', 'hold', 'holding', 'touch', 'touching', 'press', 'pressing', 'open', 'opening', 'close', 'closing', 'write', 'writing', 'type', 'typing', 'flip', 'flipping', 'step', 'stepping', 'adjust', 'adjusting', 'grab', 'grabbing', 'read', 'reading', 'page', 'screen', 'monitor', 'window', 'glass', 'book', 'document', 'chart', 'model', '짚', '기대', '들고', '넘기', '가리키', '조작', '만지', '펴', '집어', '돌리', '기울', '읽', '쓰')
NON_FRONTAL_MARKERS = ('three-quarter', 'profile', 'back-three-quarter', '45-degree', '45 degree', 'side angle', 'over-the-shoulder', 'turned', 'diagonal', '측면', '옆', '45도', '비스듬', '등진', '어깨 너머')
FRONTAL_MARKERS = ('front-facing', 'front view', 'facing camera', 'looking at camera', 'center of frame', '정면', '카메라를 바라', '정중앙', '화면 중앙')
EMOTION_CAMERA_HINTS: 'Dict[str, Dict[str, str]]' = {
    'fear': {
        'angle': 'slightly high-angle framing',
        'shot': 'medium wide shot',
        'reason': 'high angle makes character look small and vulnerable' },
    'panic': {
        'angle': 'slightly high-angle framing',
        'shot': 'medium close-up',
        'reason': 'tight high angle emphasizes panic and claustrophobia' },
    'anger': {
        'angle': 'over-the-shoulder framing',
        'shot': 'medium shot',
        'reason': 'over-shoulder confrontation composition intensifies conflict' },
    'confrontation': {
        'angle': 'over-the-shoulder framing',
        'shot': 'medium close-up',
        'reason': 'opposing angle emphasizes face-to-face tension' },
    'surprise': {
        'angle': 'dutch angle framing',
        'shot': 'medium close-up',
        'reason': 'tilted frame conveys instability and disorientation' },
    'confusion': {
        'angle': 'dutch angle framing',
        'shot': 'medium shot',
        'reason': 'dutch angle amplifies sense of confusion and unbalance' },
    'despair': {
        'angle': 'slightly high-angle framing',
        'shot': 'wide shot',
        'reason': 'high wide angle shows isolation and overwhelming situation' },
    'determination': {
        'angle': 'slightly low-angle framing',
        'shot': 'medium shot',
        'reason': 'low angle conveys strength and resolve' },
    'joy': {
        'angle': 'eye-level framing',
        'shot': 'medium shot',
        'reason': 'eye-level creates warmth and connection with viewer' },
    'sadness': {
        'angle': 'slightly high-angle framing',
        'shot': 'medium close-up',
        'reason': 'subtle high angle conveys vulnerability without overwhelming' },
    'tension': {
        'angle': 'slightly low-angle framing',
        'shot': 'medium close-up',
        'reason': 'low close-up builds suspense and unease' },
    'intimidation': {
        'angle': 'slightly low-angle framing',
        'shot': 'medium shot',
        'reason': 'low angle from victim perspective makes aggressor loom larger' } }
# WARNING: Decompyle incomplete
