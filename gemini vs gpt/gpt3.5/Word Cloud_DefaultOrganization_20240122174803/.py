try:
    from wordcloud import WordCloud
    from tkinter import messagebox
    import matplotlib.pyplot as plt
except ImportError as e:
    messagebox.showerror("Error", f"Failed to import required libraries: {e}")
    sys.exit(1)