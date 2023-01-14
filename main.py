import tkinter
import customtkinter
from pytube import YouTube


# Download video function
def download_video():
    try:
        link = entry.get()
        yt = type(YouTube(link))
        video = yt.streams.get_highest_resolution()
        video.download()
        print("Download completed")
    except:
        print('Download failed')


# Setting appearance mode
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# Setting app window
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Font settings
normalSettings = customtkinter.CTkFont(
    family="Montserrat", size=15, weight='normal')
boldSettings = customtkinter.CTkFont(
    family="Montserrat", size=12, weight='bold')

# Setting label
label = customtkinter.CTkLabel(
    master=app, text="Enter a valid YouTube link", font=normalSettings)
# label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
label.pack()

# Setting Input
url = tkinter.StringVar()
entry = customtkinter.CTkEntry(
    master=app, placeholder_text="Paste your link here", font=('Montserrat', 12), width=350, height=30, textvariable=url)
entry.pack()

# Setting button
button = customtkinter.CTkButton(
    master=app, text="Download", command=download_video, font=boldSettings)
button.pack(padx=20, pady=10)

# Looping the app
app.mainloop()
