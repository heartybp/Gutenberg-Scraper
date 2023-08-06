import tkinter as tk
from tkinter import messagebox
from bs4 import BeautifulSoup
import requests

class BookSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Project Gutenberg Book Search")
        
        self.label = tk.Label(root, text="Enter book title:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.search_button = tk.Button(root, text="Search", command=self.search_books)
        self.search_button.pack()

    def search_books(self):
        search_term = self.entry.get()
        if search_term:
            self.display_results(search_term)
        else:
            messagebox.showinfo("Error", "Please enter a search term.")

    def display_results(self, search_term):
        base_url = "https://www.gutenberg.org/ebooks/search/?query="

        # construct the search URL
        search_url = base_url + search_term

        # send GET request to search URL
        response = requests.get(search_url)
        soup = BeautifulSoup(response.content, "html.parser")

        # find book titles and display them
        book_titles = soup.select(".booklink .title")
        if book_titles:
            results = [title.get_text().strip() for title in book_titles if title.get_text().strip()]
            if results:
                messagebox.showinfo("Search Results", "\n".join(results))
            else:
                messagebox.showinfo("No Results", "No books found for the search term.")
        else:
            messagebox.showinfo("No Results", "No books found for the search term.")
    
def main():
    root = tk.Tk()
    root.geometry("400x300")
    app = BookSearchApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()