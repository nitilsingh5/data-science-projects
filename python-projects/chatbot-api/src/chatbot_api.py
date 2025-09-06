from tkinter import *
from openai import OpenAI
import time
from ttkbootstrap import Style
import threading
import requests
from PIL import Image,ImageTk
from io import BytesIO
from dotenv import load_dotenv
import os

load_dotenv()

client=OpenAI(
  api_key=os.getenv("OPENAI_API_KEY"),
  base_url='https://openrouter.ai/api/v1'
)


chat_history=[]
img_ref=[]
def chat():
  response=client.chat.completions.create(
    model='deepseek/deepseek-chat-v3.1:free',
    messages=chat_history
  )
  return response.choices[0].message.content.strip()

def effect(query,text):
  text.insert(END,'Assistant: ')
  for char in query:
    text_area.insert(END,char)
    time.sleep(0.02)
  text_area.insert(END,'\n\n')

def ask_query():
  text=text_query.get('1.0',END)
  
  chat_history.append({'role':'user','content':text})
  text_area.insert(END,f'You: {text}\n')
  def run():
    query=chat()
    chat_history.append({'role':'assistant','content':query})
    effect(query,text_area)
    text_query.delete('1.0',END)

  threading.Thread(target=run).start()

def img():
  prompt=text_query.get('1.0',END)
  text_area.insert(END,f"\n🖼 Generating Image for: {prompt}\n")

  def run():
    imge=client.images.generate(
      model='provider-3/FLUX.1-dev',
      prompt=prompt,
      size='512x512'
    )
    image_url=imge.data[0].url
    img_data=requests.get(image_url).content
    img=Image.open(BytesIO(img_data))
    img=img.resize((256,256))

    photo = ImageTk.PhotoImage(img)
    text_area.image_create(END,image=photo)
    text_area.insert(END,'\n\n')
    img_ref.append(photo)

    # img_window=Toplevel(root)
    # img_window.title('Generated Image')
    # lbl=Label(img_window,image=photo)
    # lbl.image=photo
    # lbl.pack()


    text_query.delete('1.0',END)
  
  threading.Thread(target=run).start()









root=Tk()
root.geometry('600x500')
root.title('Nitil AI')
style=Style('solar')
print(style.theme_names())

text_area=Text(root,font=1)
text_area.place(relx=0.01,rely=0.02,relwidth=0.98,relheight=0.6)

lbl=Label(root,text='Enter Your Query: ',font=1)
lbl.place(relx=0.07,rely=0.65)

text_query=Text(root,font=1)
text_query.place(relx=0.4,rely=0.65,relwidth=0.5,relheight=0.2)

ask=Button(root,text='ASK',width=7,font=1,command=ask_query)
ask.place(relx=0.4,rely=0.89,relwidth=0.2,relheight=0.08)
img_ask=Button(root,text='IMAGE',width=7,font=1,command=img)
img_ask.place(relx=0.7,rely=0.89,relwidth=0.2,relheight=0.08)

root.mainloop()

