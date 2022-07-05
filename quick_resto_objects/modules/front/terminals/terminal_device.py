# from quick_resto_objects.modules.front.terminals.ipad.terminal import Terminal
from quick_resto_objects.quick_resto_object import QuickRestoObject


class TerminalDevice(QuickRestoObject):
    # @property
    # def terminal(self) -> Terminal:
    #     self._terminal

    def __init__(self, terminal: dict=None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.front.terminals.TerminalDevice"

        super().__init__(class_name, **kwargs)

        # if (terminal!=None):self._terminal = Terminal(**terminal)

