import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import argparse

from dataConstructor import DataConstructor
from pdfWriter import pdfWriter


class MatchSheetApp:
    def __init__(self, root, original_FDM_path):
        self.root = root
        self.root.title("Match Sheet")

        self.filename = original_FDM_path
        self.data = DataConstructor(self.filename)
        self.team, self.players, self.license_numbers, self.is_present = self.data.show_player()

        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root, columns=('Name', 'License Number', 'Present'), show='headings')
        self.tree.heading('Name', text='Name')
        self.tree.heading('License Number', text='License Number')
        self.tree.heading('Present', text='Present')
        
        for player, license_number, presence in zip(self.players, self.license_numbers, self.is_present):
            self.tree.insert('', 'end', values=(player, license_number, presence))

        self.tree.pack(pady=10)

        self.change_presence_button = tk.Button(self.root, text="Change Presence", command=self.change_presence)
        self.change_presence_button.pack(pady=5)

        self.preview_button = tk.Button(self.root, text="Preview PDF", command=self.preview_pdf)
        self.preview_button.pack(pady=5)

        self.download_button = tk.Button(self.root, text="Download PDF", command=lambda: self.download_pdf('FDM.pdf'))
        self.download_button.pack(pady=5)

    def change_presence(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Alert", "Please select a player.")
            return
        
        player_name = self.tree.item(selected_item)['values'][0]
        self.data.change_presence(player_name)
        self.refresh_tree()
        messagebox.showinfo("Information", f"The presence of {player_name} has been changed.")

    def preview_pdf(self):
        preview_info = f"Team: {self.data.team}\n\nPlayers:\n"
        for player, license_number, presence in zip(self.players, self.license_numbers, self.is_present):
            preview_info += f"{player} - License: {license_number} - Present: {'Yes' if presence else 'No'}\n"
        
        messagebox.showinfo("Preview", preview_info)

    def refresh_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.team, self.players, self.license_numbers, self.is_present = self.data.show_player()
        for player, license_number, presence in zip(self.players, self.license_numbers, self.is_present):
            self.tree.insert('', 'end', values=(player, license_number, presence))
    
    def download_pdf(self, initial_pdf_path):
        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

        if not save_path:
            return

        try:
            pdf = pdfWriter(initial_pdf_path)
            pdf.write(self.data.team, self.players, self.license_numbers, self.is_present)
            pdf.doc.save(save_path)

            messagebox.showinfo("Information", f"The PDF has been successfully updated: {save_path}")
        except FileNotFoundError:
            messagebox.showerror("Error", "The specified initial PDF file was not found. Please check the file path.")
        except PermissionError:
            messagebox.showerror("Error", "Permission denied. Please close the PDF if it is open in another application.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while updating the PDF: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Match Sheet Generator for FSGT")
    parser.add_argument("--original_FDM_path",type=str, required=True, help='Path of the original Match Sheet you have to complete')
    args = parser.parse_args()

    root = tk.Tk()
    app = MatchSheetApp(root, args.original_FDM_path)
    root.mainloop()
