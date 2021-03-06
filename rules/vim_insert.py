import dragonfly
from dragonfly import *

class VimInsertRules(MappingRule):
	name = "vim_insert"
	mapping = {
		'escape | normal mode | cancel':  Key("escape"),

		# Formatting
		"parns":  Text("()") + Key("left"),
		"brax":   Text("[]") + Key("left"),
		"curly":  Text("{}") + Key("left"),
		"string":  Text("\"\"") + Key("left"),
                "number <num>" : Text("%(num)d"),

                # Editing
                "(<num> delete | delete <num>)" : Key("delete:%(num)d"),
                "back <num>" : Key("backspace:%(num)d"),
                "backspace <num>" : Key("backspace:%(num)d"),

                # Quirks
                'cut' : Text("cut"),
                'paste'  : Text("paste"),
                'undo' : Text("undo"),
                'redo' : Text("redo"),
                'save' : Text("save"),
                'quit' : Text("quit")
		}
	extras = [IntegerRef("num", -20000, 20000)]
        defaults = {"num":1}

	def _process_recognition(self, value, extras):
                action = value._action
		print("INST: %s" % str(action))
		if isinstance(action, dragonfly.actions.action_key.Key) and action._spec == "escape":
			self.parent.handle_event("normal")

		value.execute(extras)
