# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: manim_service.pyc (Python 3.11)

'''
Manim Service

Generates motion graphics and math animations using Manim library.
Outputs transparent WebM videos for compositing.
'''
import os
import sys
import subprocess
import uuid
from pathlib import Path

class ManimService:
    '''Service for generating Manim animations'''
    generate_animation = (lambda template_type = None, params = None: get_data_path = get_data_pathimport app.config.pathsoutput_dir = get_data_path() / 'manim_outputs'output_dir.mkdir(parents = True, exist_ok = True)file_id = str(uuid.uuid4())[:8]output_filename = f'''{file_id}.webm'''code = ManimService._get_template_code(template_type, params)script_path = output_dir / f'''scene_{file_id}.py'''f = open(script_path, 'w', encoding = 'utf-8')f.write(code)None(None, None)# WARNING: Decompyle incomplete
)()
    _get_template_code = (lambda template_type = None, params = None: text = params.get('text', 'Hello World')color = params.get('color', 'BLUE')if template_type == 'text_motion':
f'''\nfrom manim import *\n\nclass GenScene(Scene):\n    def construct(self):\n        # Transparent background for compositing\n        self.camera.background_color = None\n\n        t = Text("{text}", color={color}).scale(2)\n        self.play(Write(t))\n        self.wait(1)\n        self.play(FadeOut(t))\n'''if None == 'math_graph':
formula = params.get('formula', 'x**2')f'''\nfrom manim import *\nimport numpy as np\n\nclass GenScene(Scene):\n    def construct(self):\n        # Transparent background for compositing\n        self.camera.background_color = None\n\n        axes = Axes(\n            x_range=[-3, 3, 1],\n            y_range=[-1, 9, 1],\n            axis_config={{"color": WHITE}}\n        )\n        graph = axes.plot(lambda x: {formula}, color={color})\n\n        self.play(Create(axes), run_time=1)\n        self.play(Create(graph), run_time=2)\n        self.wait(1)\n'''if None == 'circle_animation':
f'''\nfrom manim import *\n\nclass GenScene(Scene):\n    def construct(self):\n        self.camera.background_color = None\n\n        circle = Circle(radius=2, color={color})\n        self.play(Create(circle))\n        self.wait(0.5)\n        self.play(circle.animate.scale(0.5))\n        self.wait(0.5)\n        self.play(FadeOut(circle))\n''')()
    get_available_templates = (lambda : [
{
'id': 'text_motion',
'name': 'Text Motion',
'description': 'Animated text with write effect',
'params': [
'text',
'color'] },
{
'id': 'math_graph',
'name': 'Math Graph',
'description': 'Animated mathematical function graph',
'params': [
'formula',
'color'] },
{
'id': 'circle_animation',
'name': 'Circle Animation',
'description': 'Animated circle creation and scaling',
'params': [
'color'] }])()
