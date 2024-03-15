import tkinter as tk
from task_list import TaskList
from schedule import Schedule
from search import Search
from briefnote import BriefNote
def main():
    window = tk.Tk()
    window.title("FaceWall")
    window.geometry("800x600")
    # Create the task list frame
    task_list_frame = tk.Frame(window)
    task_list_frame.pack(side=tk.LEFT)
    # Create the task list object
    task_list = TaskList(task_list_frame)
    # Create the schedule frame
    schedule_frame = tk.Frame(window)
    schedule_frame.pack(side=tk.RIGHT)
    # Create the schedule object
    schedule = Schedule(schedule_frame)
    # Create the search frame
    search_frame = tk.Frame(window)
    search_frame.pack(side=tk.BOTTOM)
    # Create the search object
    search = Search(search_frame)
    # Create the brief note frame
    brief_note_frame = tk.Frame(window)
    brief_note_frame.pack(side=tk.TOP)
    # Create the brief note object
    brief_note = BriefNote(brief_note_frame)
    # Start the main loop
    window.mainloop()
if __name__ == "__main__":
    main()