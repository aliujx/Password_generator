from tkinter import *
from  tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	nr_letters = random.randint(8, 10)
	nr_symbols = random.randint(2, 4)
	nr_numbers = random.randint(2, 4)

	password_letters = [random.choice(letters) for letter in range(nr_letters)]
	password_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]
	password_numbers = [random.choice(numbers) for number in range(nr_numbers)]
	password_list = password_letters + password_symbols + password_numbers
	random.shuffle(password_list)

	password = "".join(password_list)

	password_entry.insert(0, password)
	pyperclip.copy(password)

	
def search():
	message = messagebox.showinfo(title="Your password", message=f"{website_text}: \nemail: {

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
	website = website_entry.get()
	email = email_entry.get()
	password = password_entry.get()
	new_data_password = {
		website: {
			"email": email, 
			"password": password,
		}
	}

	if len(website) == 0 or len(password) == 0:
		messagebox.showinfo(title='Oops!', message="Please don't leave any field empty!")

	else:
		try:
			with open("my_passwords.json", mode="r") as file:
				#Reading old data
				data = json.load(file)
		except FileNotFoundError:
			with open("my_password.json", "w) as file:
				json.dump(new_data_password, file, indent=4)  
		else:
			#Updating old data with new data
			data.update(new_data_password)
			with open("my_password.json", "w") as data:
				#Saving the updated data
				json.dump(data, file, indent=4)
		finally:	
			website_entry.delete(0, END)
			password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_text = Label(text="Website:")
website_text.grid(column=0, row=1)

email_text = Label(text="Email/Username:")
email_text.grid(column=0, row=2)

password_text = Label(text="Password: ")
password_text.grid(column=0, row=3)

website_entry = Entry(width=22)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=40)
email_entry.insert(END, "aliujx@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)
					  
search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1)

password_button = Button(text="Generate Password",command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)





window.mainloop()
