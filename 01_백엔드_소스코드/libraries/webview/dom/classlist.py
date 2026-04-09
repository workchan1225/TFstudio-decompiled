# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: classlist.pyc (Python 3.11)


class ClassList:
    
    def __init__(self, element, classes = (None,)):
        self._ClassList__element = element
        if classes:
            classes = ' '.join(classes)
            self._ClassList__element._window.evaluate_js(f'''{self._ClassList__element._query_command}; element.className = \'{classes}\'''')
            return None

    
    def append(self, cls):
        self._ClassList__element._window.run_js(f'''{self._ClassList__element._query_command}; element.classList.add(\'{cls}\')''')

    
    def remove(self, cls):
        self._ClassList__element._window.run_js(f'''{self._ClassList__element._query_command}; element.classList.remove(\'{cls}\')''')

    
    def toggle(self, cls):
        self._ClassList__element._window.run_js(f'''{self._ClassList__element._query_command}; element.classList.toggle(\'{cls}\')''')

    
    def __get_classes(self):
        classes = self._ClassList__element._window.evaluate_js(f'''{self._ClassList__element._query_command}; element.className''').split(' ')
        return classes()

    
    def __getitem__(self, index):
        classes = self.__get_classes()
        return classes[index]

    
    def __len__(self):
        classes = self.__get_classes()
        return len(classes)

    
    def __str__(self):
        classes = self.__get_classes()
        return str(classes)

    
    def __repr__(self):
        classes = self.__get_classes()
        return repr(classes)

    
    def clear(self):
        self._ClassList__element._window.run_js(f'''{self._ClassList__element._query_command}; element.className = \'\'''')
