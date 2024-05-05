import tkinter as tk
import re

def check_password_strength(password):
  """
  This function checks password strength based on length, character types, and returns feedback.
  """
  score = 0
  suggestions = []

  # Check length
  if len(password) >= 12:
    score += 1
  else:
    suggestions.append("Password should be at least 12 characters long")

  # Check character types
  if re.search(r"[A-Z]", password):
    score += 1
  else:
    suggestions.append("Password should contain at least one uppercase letter")
  if re.search(r"[a-z]", password):
    score += 1
  else:
    suggestions.append("Password should contain at least one lowercase letter")
  if re.search(r"\d", password):
    score += 1
  else:
    suggestions.append("Password should contain at least one digit")
  if re.search(r"[!@#$%^&*(),.?\n\":{}|<>]", password):
    score += 1
  else:
    suggestions.append("Password should contain at least one special character")

  # Strength feedback based on score
  if score == 5:
    feedback = "Strong password!"
  elif score == 4:
    feedback = "Good password, consider adding another character type."
  elif score == 3:
    feedback = "Moderate password, add more character types and increase length."
  else:
    feedback = "Weak password, needs improvement with length and character diversity."

  return feedback, suggestions

def evaluate_password():
  password = password_entry.get()
  feedback, suggestions = check_password_strength(password)
  feedback_label.config(text=feedback)
  suggestions_text.delete("1.0", tk.END)
  if suggestions:
    for suggestion in suggestions:
      suggestions_text.insert(tk.END, "- " + suggestion + "\n")

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create labels and entry field
password_label = tk.Label(root, text="Enter your password:")
password_label.pack()

password_entry = tk.Entry(root)
password_entry.pack()

# Create button to trigger evaluation
evaluate_button = tk.Button(root, text="Evaluate", command=evaluate_password)
evaluate_button.pack()

# Create label for feedback
feedback_label = tk.Label(root, text="")
feedback_label.pack()

# Create text box for suggestions
suggestions_text = tk.Text(root, height=5)
suggestions_text.pack()

# Run the main loop
root.mainloop()
