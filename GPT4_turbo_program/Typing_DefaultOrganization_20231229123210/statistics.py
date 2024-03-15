'''
This file contains the StatisticsViewer class, which provides detailed statistics and visualizations of user progress.
'''
import matplotlib.pyplot as plt
class StatisticsViewer:
    def __init__(self):
        self.statistics_data = {
            'accuracy': [],
            'speed': [],
            'timestamp': []
        }
    def update_statistics(self, accuracy, speed, timestamp):
        '''
        Update the statistics with new data.
        :param accuracy: The current accuracy percentage.
        :param speed: The current typing speed (words per minute).
        :param timestamp: The timestamp of the recorded session.
        '''
        self.statistics_data['accuracy'].append(accuracy)
        self.statistics_data['speed'].append(speed)
        self.statistics_data['timestamp'].append(timestamp)
    def display_statistics(self):
        '''
        Display the statistics to the user using matplotlib for visualizations.
        '''
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        # Plot accuracy over time
        ax1.plot(self.statistics_data['timestamp'], self.statistics_data['accuracy'], marker='o', linestyle='-', color='blue')
        ax1.set_title('Typing Accuracy Over Time')
        ax1.set_xlabel('Session Timestamp')
        ax1.set_ylabel('Accuracy (%)')
        ax1.grid(True)
        # Plot speed over time
        ax2.plot(self.statistics_data['timestamp'], self.statistics_data['speed'], marker='x', linestyle='-', color='red')
        ax2.set_title('Typing Speed Over Time')
        ax2.set_xlabel('Session Timestamp')
        ax2.set_ylabel('Speed (WPM)')
        ax2.grid(True)
        # Adjust layout to prevent overlap
        plt.tight_layout()
        # Show the plot
        plt.show()
    def get_statistics(self):
        '''
        Return the current statistics data.
        :return: dict of the current statistics data
        '''
        return self.statistics_data