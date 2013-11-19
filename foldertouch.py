import sublime, sublime_plugin, os.path, os

class FolderTouch(sublime_plugin.EventListener):

    def on_post_save(self, view):
        os.utime( os.path.dirname(view.file_name()), None )
