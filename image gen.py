import replicate
import tkinter as tk
from PIL import ImageTk, Image
import requests
import io
from bs4 import BeautifulSoup

def sel():
    promp=entry.get()
    input = {
        "width": 856,
        "height": 1156,
        "prompt": promp+", illustration in the style of WHMSCPE001",
        "output_format": "png",
        "output_quality": 100,
        "num_inference_steps": 25
    }

    output = replicate.run(
        "bingbangboom-lab/flux-new-whimscape:2e8de10f217bc56da163a0204cf09f89995eaf643459014803fae79753183682",
        input=input
    )
    response1 = requests.get(output)
    soup = BeautifulSoup(response1.text, 'html.parser')
    text = soup.get_text()
    try:
        response = requests.get(text, verify=False)
        response.raise_for_status()  
        img_data = response.content

        image = Image.open(io.BytesIO(img_data))
    except Exception:
        image = Image.open("default_image.jpg")  

    image = image.resize((250, 250))
    photo = ImageTk.PhotoImage(image)

    label.config(image=photo)
    label.image = photo  
    label.update()


root = tk.Tk()

msg = tk.Message(root, text="Enter the image prompt:")
msg.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Submit", command=sel)
button.pack()

label = tk.Label(root)
label.pack()

root.mainloop()