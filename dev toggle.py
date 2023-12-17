from os.path import exists


import tkinter as tk
from ttkbootstrap import PhotoImage
import ttkbootstrap as ttk
from json import loads as json_loads
from webbrowser import open as open_browser
import requests





end_directory = ":\Program Files\Epic Games\Fortnite\FortniteGame\Content\Paks\pakchunk20-WindowsClient.ucas" 




directory_found = False

for i in range (99, 123):
    path = chr(i) + end_directory
    if exists(path):
        directory_found = True
        directory = path
        break

if not directory_found:
    for i in range (96, 98):
        path = chr(i) + end_directory

        if exists(path):
            directory_found = True
            directory = path
            break


if not directory_found:
    error_window = tk.Tk()
    error_window.geometry("350x100")
    error_window.resizable(False, False)
    error_window.title("Error")

    error_label = tk.Label(error_window, text="unable to find directory\nvist discord for help", font="arial 20", fg="red")
    error_label.pack()
    error_window.mainloop()

hex_to_change = "504257415f57315f446f6f72435f43"
hex_to_change_to = "5042574d5f57315f446f6f72435f43"
program_version = "1.9.0"



icon_data = """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"""
image_data ="""
iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAxnpUWHRSYXcgcHJvZmlsZSB0eXBlIGV4aWYAAHjabVDbDcMgDPz3FB0BPyBmHNIQqRt0/BrsREnUkzhsHxzG0L+fHV4DhAKSFy21lGSQKpWaBZocbTImmTxBIVl+q8MpkJXYdvZUS5w/6nga+NYsyhcjfYew3oUq4a8Po3iZR0cj3sKohhGTCxgGzb+VStXl+oW1pzvUFwxad+tnzCguP3NZbHpbtneYqDNyMmYWb4DHYuBmAjrbQeRscWaZlaMTG8i/OR2AH5hUWo1unRCXAAABhWlDQ1BJQ0MgcHJvZmlsZQAAeJx9kT1Iw0AYht+miqKVDnYQcchQnexSRQSXUsUiWChthVYdTC79gyYNSYqLo+BacPBnserg4qyrg6sgCP6AuLo4KbpIid8lhRYx3nHcw3vf+3L3HSA0q0w1e2KAqllGOhEXc/lVse8VgzSDiGJOYqaezCxm4Tm+7uHj+12EZ3nX/TmGlILJAJ9IHGO6YRFvEM9sWjrnfeIQK0sK8TnxpEEXJH7kuuzyG+eSwwLPDBnZ9DxxiFgsdbHcxaxsqMTTxGFF1ShfyLmscN7irFbrrH1P/sJAQVvJcJ3WGBJYQhIpiJBRRwVVWIjQrpFiIk3ncQ//qONPkUsmVwWMHAuoQYXk+MH/4HdvzeJU1E0KxIHeF9v+GAf6doFWw7a/j227dQL4n4ErreOvNYHZT9IbHS18BAS3gYvrjibvAZc7wMiTLhmSI/lpCcUi8H5G35QHhm+BgTW3b+1znD4AWerV8g1wcAhMlCh73ePd/d19+7em3b8fJ8hy74TOohgAAA12aVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/Pgo8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJYTVAgQ29yZSA0LjQuMC1FeGl2MiI+CiA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIKICAgIHhtbG5zOnN0RXZ0PSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VFdmVudCMiCiAgICB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iCiAgICB4bWxuczpHSU1QPSJodHRwOi8vd3d3LmdpbXAub3JnL3htcC8iCiAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyIKICAgIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIKICAgeG1wTU06RG9jdW1lbnRJRD0iZ2ltcDpkb2NpZDpnaW1wOjkyNWQ4OGY3LTMwZWItNDU1MS05NGJjLThhOGJlM2Y2Mzg1NSIKICAgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDowN2MyZjM1OC1lNzc0LTQzZTQtOTFjMS0wMGJhODEzZGU5MmQiCiAgIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDo2ZDcxZWU1Zi1mYmY2LTRmMmItOGVmMS0xNTAxZTJhYzc1MDgiCiAgIGRjOkZvcm1hdD0iaW1hZ2UvcG5nIgogICBHSU1QOkFQST0iMi4wIgogICBHSU1QOlBsYXRmb3JtPSJXaW5kb3dzIgogICBHSU1QOlRpbWVTdGFtcD0iMTY5OTcxODA1NjkxMzk0MiIKICAgR0lNUDpWZXJzaW9uPSIyLjEwLjM0IgogICB0aWZmOk9yaWVudGF0aW9uPSIxIgogICB4bXA6Q3JlYXRvclRvb2w9IkdJTVAgMi4xMCIKICAgeG1wOk1ldGFkYXRhRGF0ZT0iMjAyMzoxMToxMVQxNTo1NDoxNCswMDowMCIKICAgeG1wOk1vZGlmeURhdGU9IjIwMjM6MTE6MTFUMTU6NTQ6MTQrMDA6MDAiPgogICA8eG1wTU06SGlzdG9yeT4KICAgIDxyZGY6U2VxPgogICAgIDxyZGY6bGkKICAgICAgc3RFdnQ6YWN0aW9uPSJzYXZlZCIKICAgICAgc3RFdnQ6Y2hhbmdlZD0iLyIKICAgICAgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDphOWQ3NDkxMy1iOTVmLTRhODQtYjgwNS1mMzBjZWMxYTk4YWQiCiAgICAgIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkdpbXAgMi4xMCAoV2luZG93cykiCiAgICAgIHN0RXZ0OndoZW49IjIwMjMtMTEtMTFUMTU6NTQ6MTYiLz4KICAgIDwvcmRmOlNlcT4KICAgPC94bXBNTTpIaXN0b3J5PgogIDwvcmRmOkRlc2NyaXB0aW9uPgogPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgIAo8P3hwYWNrZXQgZW5kPSJ3Ij8+rr6bogAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAAOwwAADsMBx2+oZAAAAAd0SU1FB+cLCw82EPiz8aYAAAPCSURBVFjD7ZddiJRlFMd//+d913V3ZnJWV8zCiLRuhIjsizSokJASunCnHSuUyN0w24JK6ONqCa9EhAIvdt3A8GNSu4gKFvqQSIpQEKOoLioSzUJKc2Z2dn3f9zldTFmzszO7VitBPpfPc97n/M/5n/N/zwOX1v99aTKD/IbyFUS6G0tuB1UKg+lnmtr3lDdhfg7SJ4Hp/V3bU8cvGMDapyw7VinmMa0BuxVwvx95R8ty4Usx1imnFIDzVjannzEF3kcHJVXtzcykQ4GC184lbXv2D7lfJgXQ/VjlTiXRW4j0v5lqQ2VJXYWB9HBDAF1dx9rCjuxR4NppIdw4lszILN63TaU/ttxfz1uynU9Om/NquFcFY6XnJ8zAg+vPdPjYfQtkp7XsjZHWGW7hjm3pH2syYLHrm3bn1ZDbK5E9XZOBFX2+NVspfYeYf5G6/3R4WWrBzi2u7ACy5yr3XjznANYRnx3tOk+BvOUvvgYmqwG0os+3ZkdLp4BMA7QG7qCkYW92NdAlrKPBrUXQG1Lwtfl4ucFdUm2n/VmLjPqWytxw1ujoksbOAXj1zMyTG4ZfuW4MTPmekSEs+QDRXgvTIplbVRhKvwey3l7bctZKm8A2NpDgmcFYaplD0dImXMV492LVOYCsMJj61FCh/kb3dmEo8y7IAAYGFIWVVD+o2LAUnb/FgRY3BuBOFIYyP9V9KD6vs0RHxu/t3OnKhn3TMDzT9c6ZrmmSgTkr+nxrPS7mjd/y+Lq9XG5vIGNuk/sXOaNp+6WzlZE1NX/KtZa1ibrG1J1/tFgDwnXcdz/iyoYUiMvVve7XU5I6m4AoiuA5hdFwHLfMEX6rsKUTF5aO+DB4Iol00pHc4eS3ArObyPKY8j3F02DZKWh4CWwmUjiJYQJuBCw9lYEnxLDJzaA6H0zJMADLTEkPzbwzbLR5NJb8A8lNgLhxDajsJPdVVe0m5HSv0bIG9BFQNDM/eVR4jBJyHxvBI6DdTaakL0MXplYlcfklmV+HaB0nlw+IZHagsF8h3ydRfBNomWE3gC1AajPvJVQx6bhDRz12MAxbDhPZ/MTFGzG7p545OyeFO0Tywvmj1b0jy8z8ZkhurvJYk4l39gxmVo7vu1xunwPYtzfnkWqymO8t7cf8qjpKzB114tndg5kDdTNhLmeBmzWyUrKNkNwGCjDGQEsK2zNfXAj7Dz9eWRRH0WdAG1hiuMMucJt/mNf+5of9iid9FzzUU7rRS90yTuweTL38d0qwu6e8HmxhiF7fNZg6dOkZ9p9cvwF36oBukQl/lAAAAABJRU5ErkJggg==
"""



config = json_loads(requests.get("https://drive.google.com/uc?export=download&id=1Z1gj3b46F3FGVhy_jNg-ciXrEKdXk9M6").text)



#----------------------------------------------------------------config texts
latest_version = config["dev_toggle"]["latest_version"]

update_available_text = config["update_available_text"]
url = config["discord_button_link"]
message_text= config["dev_toggle"]["message_text"]



def discord_pressed():
    open_browser(url)



def check_status_func():
    check_status_button.config(state="disabled")
    with open(directory, "rb") as f:
        file = f.read().hex()
    if file.find(hex_to_change) == -1:
        check_status_button.configure(text="enabled", font="Arial 10 bold", bg="green")
    else: 
        check_status_button.configure(text="disabled", font="Arial 10 bold", bg="red")
    check_status_button.config(state="normal")

def toggle_func():

    toggle_button.config(state="disabled")


    with open(directory, "rb") as f:

        file = f.read()

    file = file.hex()


    location = file.find(hex_to_change) 


    if location != -1:

        file = file.replace(hex_to_change, hex_to_change_to)


        file = bytes.fromhex(file)

        with open(directory, "wb") as f:
            f.write(file)

    else:
        file = file.replace(hex_to_change_to, hex_to_change)


        file = bytes.fromhex(file)

        with open(directory, "wb") as f:
            f.write(file)

    
    toggle_button.config(state="normal")
    check_status_func()
    return True







window = ttk.Window(themename="purpledark")
icon = PhotoImage(master=window, data=icon_data)
window.title("R0's dev toggle (beta)")
window.geometry("400x300+100+100")
window.resizable(False, False)
window.iconphoto(True, icon)


window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=3)
window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=2)
window.grid_rowconfigure(2, weight=2)



bottom_label = ttk.Label(window, text= "thanks to spifili", font="Arial 9")


update_available_label = ttk.Label(window, text=update_available_text, font="Arial 10")




title_label = ttk.Label(window, text= "R0's dev toggle", font="Arial 40 bold" )
title_label.grid(row=0, column=1, sticky="n")



version_label = ttk.Label(window, text=f"v{program_version}", font ="Arial 9")
version_label.grid(row=2, column=1, sticky="sw")


discord_image = PhotoImage(data=image_data)

discord_button_style = ttk.Style()
discord_button_style.configure("discord.Outline.TButton", font=("Helvetica", 1))
discord_button_style.configure("discord.Outline.TButton", padding=(3, 3, 3, 3))


discord_button = ttk.Button(window,  command=discord_pressed, style="discord.Outline.TButton", )
discord_button.configure(image=discord_image)


discord_button.place(x=355, y=255)

check_status_button = tk.Button(window, text="check status", font="Arial 10", command=check_status_func, height=1, width=9)

message_button = ttk.Label(window, text=message_text)
message_button.grid(row=2, column=1, sticky="n")




s = ttk.Style()
s.configure('custom.Outline.TButton', font=('Arial', 20, "bold"))
toggle_button = ttk.Button(window, text="TOGGLE", command=toggle_func, style="custom.Outline.TButton")

toggle_button.grid(row=1, column=1, ipadx=5, ipady=8)

check_status_button.place(x=315, y=85)





for i in range(3):

    if latest_version.split(".")[i] > program_version.split(".")[i]:
        
        
        bottom_label.config(text=update_available_text, font="Arial, 10")
        break
        
bottom_label.grid(column=1, row=2, sticky="s")












check_status_func()

window.mainloop()

