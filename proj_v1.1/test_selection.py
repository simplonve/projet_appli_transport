from kivy.uix.listview import ListView, ListItemButton
from kivy.uix.boxlayout import BoxLayout
from kivy.adapters.listadapter import ListAdapter

class MainView(BoxLayout):

    def __init__(self, **kwargs):
        super(MainView, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.list_adapter = ListAdapter(
            data=["Item #{0}".format(i) for i in range(10)],
            cls=ListItemButton,
            sorted_keys=[],
            selection_mode='multiple',
            )
        self.list_adapter.bind(on_selection_change=self.selection_change)

        list_view = ListView(adapter=self.list_adapter)
        self.add_widget(list_view)


    def selection_change(self, adapter, *args):
        print ('-- selection change')
        for e in adapter.selection:
            x = e.index
            print (x, adapter.data[x])

if __name__ == '__main__':
    from kivy.base import runTouchApp
    runTouchApp(MainView(width=800))