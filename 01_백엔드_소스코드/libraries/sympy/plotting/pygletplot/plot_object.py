# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: plot_object.pyc (Python 3.11)


class PlotObject:
    '''
    Base class for objects which can be displayed in
    a Plot.
    '''
    visible = True
    
    def _draw(self):
        if self.visible:
            self.draw()
            return None

    
    def draw(self):
        '''
        OpenGL rendering code for the plot object.
        Override in base class.
        '''
        pass
