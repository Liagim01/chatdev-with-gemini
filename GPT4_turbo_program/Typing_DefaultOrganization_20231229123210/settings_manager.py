'''
This file contains the SettingsManager class, which manages the customizable settings for the typing practice application.
'''
class SettingsManager:
    def __init__(self):
        self.exercise_settings = {
            'time_limit': 60,  # Default time limit for typing exercises
            'keyboard_layout': 'QWERTY',  # Default keyboard layout
            'difficulty_level': 'Beginner'  # Default difficulty level
        }
    def update_settings(self, new_settings):
        '''
        Update the settings based on user input.
        :param new_settings: dict with keys 'time_limit', 'keyboard_layout', 'difficulty_level'
        '''
        if 'time_limit' in new_settings:
            self.exercise_settings['time_limit'] = new_settings['time_limit']
        if 'keyboard_layout' in new_settings:
            self.exercise_settings['keyboard_layout'] = new_settings['keyboard_layout']
        if 'difficulty_level' in new_settings:
            self.exercise_settings['difficulty_level'] = new_settings['difficulty_level']
    def get_settings(self):
        '''
        Return the current settings.
        :return: dict of the current settings
        '''
        return self.exercise_settings