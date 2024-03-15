import tkinter as tk
class ReminderEntry(tk.Frame):
    '''Reminder entry in the reminder app.'''
    def __init__(self, root, reminder):
        '''Initialize the reminder entry.'''
        super().__init__(root)
        self.root = root
        self.reminder = reminder
        self.conversation_topics = []
        self.pack()
        # Create the label for the reminder.
        self.reminder_label = tk.Label(self, text=reminder)
        self.reminder_label.pack()
        # Create the checkbox for the reminder.
        self.reminder_checkbox = tk.Checkbutton(self)
        self.reminder_checkbox.pack()
        # Create the entry for the conversation topic.
        self.conversation_topic_entry = tk.Entry(self)
        self.conversation_topic_entry.pack()
        # Create the button to add the conversation topic.
        self.add_conversation_topic_button = tk.Button(self, text="Add Conversation Topic", command=self.add_conversation_topic)
        self.add_conversation_topic_button.pack()
    def add_conversation_topic(self):
        '''Add a new conversation topic to the list.'''
        conversation_topic = self.conversation_topic_entry.get()
        self.conversation_topic_entry.delete(0, tk.END)
        self.conversation_topics.append(conversation_topic)