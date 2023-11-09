import tkinter as tk
import time

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.start_time = None
        self.text_to_type = "The quick brown fox jumps over the lazy dog."
        self.user_input = tk.StringVar()
        self.mistakes = 0

        self.create_widgets()

    def create_widgets(self):
        self.instruction_label = tk.Label(self.root, text="Type the following:")
        self.instruction_label.pack(pady=10)

        self.text_widget = tk.Text(self.root, height=3, width=50, wrap=tk.WORD)
        self.text_widget.insert(tk.END, self.text_to_type)
        self.text_widget.config(state=tk.DISABLED)
        self.text_widget.pack(pady=10)

        self.entry = tk.Entry(self.root, textvariable=self.user_input)
        self.entry.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start Typing Test", command=self.start_typing_test)
        self.start_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)

    def start_typing_test(self):
        self.mistakes = 0
        self.start_time = time.time()
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(0, tk.END)
        self.entry.focus()
        self.start_button.config(state=tk.DISABLED)
        self.root.bind('<Key>', self.check_typing)

    def check_typing(self, event):
        user_text = self.user_input.get()
        if user_text == self.text_to_type:
            self.end_typing_test()
        else:
            self.highlight_mistakes(user_text)

    def highlight_mistakes(self, user_text):
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.tag_configure("mistake", background="pink")
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert(tk.END, self.text_to_type)

        for i, char in enumerate(user_text):
            if i >= len(self.text_to_type) or char != self.text_to_type[i]:
                start_pos = f"1.{i}"
                end_pos = f"1.{i+1}"
                self.text_widget.tag_add("mistake", start_pos, end_pos)

        self.text_widget.tag_raise("mistake")
        self.text_widget.config(state=tk.DISABLED)

        self.mistakes += len(user_text) - len(self.text_to_type)

    def end_typing_test(self):
        elapsed_time = time.time() - self.start_time
        typing_speed = len(self.text_to_type) / (elapsed_time / 60)  # Words per minute
        accuracy = min(((len(self.text_to_type) - self.mistakes) / len(self.text_to_type)) * 100, 100)

        result_text = f"Typing Speed: {typing_speed:.2f} WPM\nAccuracy: {accuracy:.2f}%"
        self.result_label.config(text=result_text)

        self.entry.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.root.unbind('<Key>')

if __name__ == "__main__":
    root = tk.Tk()
    typing_speed_test = TypingSpeedTest(root)
    root.mainloop()
