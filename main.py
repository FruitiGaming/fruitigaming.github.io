import tkinter as tk

from tkinter import ttk

def boot_animation():
    root = tk.Tk()
    root.title("Boot Screen")
    root.geometry("800x600")

    # Create progress bar
    progress = ttk.Progressbar(root, length=300, mode="indeterminate")
    progress.pack(pady=50)

    # Animation loop
    def animate():
        progress.start(10)
        root.after(1000, animate)

    # Start the animation
    animate()

    root.mainloop()

# Run the boot screen
boot_animation()


# Function to open a new window for an application
def open_window(application):
    window = tk.Toplevel(root)
    window.title(application)
    window.geometry("400x300")
    window.configure(background="white")
    
    # Customize the window according to the application
    
    # Example: Command Prompt window
    if application == "Notepad":
        label = tk.Label(window, text="Notepad", font=("Arial", 14))
        label.pack(pady=20)
        entry = tk.Entry(window, width=40)
        entry.pack(pady=10)
        output = tk.Text(window, width=50, height=10)
        output.pack(pady=10)
      
        def execute_command():
            command = entry.get()
            # Execute the command and display the output in the output Text widget
            # Example: If the command is "help", display a help message in the output widget
            if command == "help":
                output.insert(tk.END, "This is the help message.\n")
        
        button = tk.Button(window, text="Execute", command=execute_command)
        button.pack(pady=10)

# Create the main window
root = tk.Tk()
root.title("FruitiOS  Home  About  File  Edit  Window")
root.geometry("800x600")
root.configure(background="Teal")

# Taskbar
taskbar = tk.Frame(root, height=40, bg="#c3c3c3")
taskbar.pack(side=tk.BOTTOM, fill=tk.X)

# Start Button
start_button = tk.Button(taskbar, text="Start", padx=10, pady=5)
start_button.pack(side=tk.LEFT)

# Start Menu
start_menu = tk.Menu(start_button, tearoff=0)
start_menu.add_command(label="Files", command=lambda: open_window("Files"))
start_menu.add_command(label="Internet Explorer", command=lambda: open_window("Internet Explorer"))
start_menu.add_command(label="Command Prompt", command=lambda: open_window("Command Prompt"))
start_menu.add_command(label="Notepad", 
command=lambda: open_window("Notepad"))
start_menu.add_command(label="Solitare", 
command=lambda: open_window("Solitare"))

def show_start_menu(event):
    start_menu.post(event.x_root, event.y_root)

start_button.bind("<Button-1>", show_start_menu)

root.mainloop()
