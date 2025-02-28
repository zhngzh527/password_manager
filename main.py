from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)


  password_letter = [random.choice(letters) for _ in range(nr_letters)]
  password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
  password_number = [random.choice(numbers) for _ in range(nr_numbers)]

  password_list = password_symbols + password_letter + password_number
  random.shuffle(password_list)

  password_entry.delete(0,END)
  password = "".join(password_list)
  password_entry.insert(0,f'{password}')
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    new_data = {
        website_data:{
            "email":email_data,
            "password":password_data,
        }
    }

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Error",message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json","r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

# ----------------------------FIND PASSWORD-----------------------------#
def find_password():
    website_data = website_entry.get()
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website_data in data:
            messagebox.showinfo(title=f'{website_data}', message=f'Email: {data[website_data]['email']}\n'
                                                             f'Password: {data[website_data]['password']}')
        else:
            messagebox.showinfo(title="Error",message=f'No details about {website_data} exists')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200)
lock_pic = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_pic)
canvas.grid(column=1,row=0)

#Labels
website = Label(text="Website:")
website.grid(column=0,row=1)
email = Label(text="Email/Username:")
email.grid(column=0,row=2)
password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

#Entries
website_entry = Entry(width=31)
website_entry.focus()
website_entry.grid(column=1,row=1)
email_entry = Entry(width=49)
email_entry.insert(0, "zzxyy@email.com")
email_entry.grid(column=1,row=2,columnspan=2)
password_entry = Entry(width=31)
password_entry.grid(column=1,row=3)

#Buttons
create = Button(text="Generate Password",command=generate_password)
create.grid(column=2,row=3)
add = Button(text="Add",width=33,command=save)
add.grid(column=1,row=4,columnspan=2)
search = Button(text="Search",width=12,command=find_password)
search.grid(column=2,row=1)


window.mainloop()
