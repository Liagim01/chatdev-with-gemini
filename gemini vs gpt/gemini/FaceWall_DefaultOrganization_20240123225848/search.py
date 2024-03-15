import tkinter as tk
class Search(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Create the search label
        self.search_label = tk.Label(self, text="Search")
        self.search_label.pack()
        # Create the search entry
        self.search_entry = tk.Entry(self)
        self.search_entry.pack()
        # Create the search button
        self.search_button = tk.Button(self, text="Search")
        self.search_button.pack()
        # Create the results list box
        self.results_list_box = tk.Listbox(self)
        self.results_list_box.pack()