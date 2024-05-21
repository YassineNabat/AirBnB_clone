#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """A simple command interpreter using the cmd module.
       Customizes the prompt, handles the quit command, and ensures an empty line does nothing.
    """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def eof(self):
        """Handle EOF (Ctrl-D)."""
        return True

    def default(self, line):
        """Called on an input line when no explicit command matches."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
