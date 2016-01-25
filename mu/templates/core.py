"""
Core functionality relating to the specification and management of project
templates within Mu.
"""

class Project:
    """
    Base class for all projects.
    """

    def build_ui(self, parent=None):
        """
        Build the most basic generic UI for a project.
        """
        pass


    def build_buttons(self, button_bar):
        """
        Build the most basic buttons for a project.
        """
        pass

    def build_custom_ui(self):
        """
        Adds UI elements specific to the project template.

        Overridden by any child class.
        """
        pass

    def build_custom_buttons(self, button_bar):
        """
        Adds buttons specific to the project template.

        Overridden by any child class.
        """
        pass
