import tkinter as tk
from tkinter import messagebox


class MyForm:
    def __init__(self, root):
        self.root = root
        self.root.title("MyForm")
        
        self.contacts = []

        self.setup_ui()

    def setup_ui(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        tk.Label(frame, text="Name:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.name_entry = tk.Entry(frame)
        self.name_entry.grid(row=0, column=1, pady=5)

        tk.Label(frame, text="Email:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.email_entry = tk.Entry(frame)
        self.email_entry.grid(row=1, column=1, pady=5)

        tk.Label(frame, text="Phone:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.phone_entry = tk.Entry(frame)
        self.phone_entry.grid(row=2, column=1, pady=5)

        self.add_button = tk.Button(frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=5)

        self.contact_listbox = tk.Listbox(frame)
        self.contact_listbox.grid(row=4, column=0, columnspan=2, pady=5)
        self.contact_listbox.bind('<<ListboxSelect>>', self.load_contact)

        self.edit_button = tk.Button(frame, text="Edit Contact", command=self.edit_contact)
        self.edit_button.grid(row=5, column=0, pady=5)
        
        self.delete_button = tk.Button(frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=5, column=1, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        if name and email and phone:
            self.contacts.append({"name": name, "email": email, "phone": phone})
            self.update_contact_listbox()
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "All fields must be filled.")

    def edit_contact(self):
        selected = self.contact_listbox.curselection()
        if selected:
            index = selected[0]
            name = self.name_entry.get()
            email = self.email_entry.get()
            phone = self.phone_entry.get()

            if name and email and phone:
                self.contacts[index] = {"name": name, "email": email, "phone": phone}
                self.update_contact_listbox()
                self.clear_entries()
            else:
                messagebox.showwarning("Input Error", "All fields must be filled.")
        else:
            messagebox.showwarning("Selection Error", "No contact selected for editing.")

    def delete_contact(self):
        selected = self.contact_listbox.curselection()
        if selected:
            index = selected[0]
            del self.contacts[index]
            self.update_contact_listbox()
            self.clear_entries()
        else:
            messagebox.showwarning("Selection Error", "No contact selected for deletion.")

    def load_contact(self, event):
        selected = self.contact_listbox.curselection()
        if selected:
            index = selected[0]
            contact = self.contacts[index]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, contact["name"])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, contact["email"])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, contact["phone"])

    def update_contact_listbox(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact['name']} | {contact['email']} | {contact['phone']}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = MyForm(root)
    root.mainloop()
