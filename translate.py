from googletrans import Translator
translator = Translator()
from tkinter import *
from tkinter import ttk
root=Tk()

root.config(bg="#F2CCC3")
root.geometry("800x500")
label=Label(root,text="LANGUAGE TRANSLATOR",font=("Calibre",18,"italic"),bg="#F2CCC3")
label_enter=Label(root,text="Enter Text",bg="#F2CCC3",font=("Calibre",15,"italic"))
label_ou=Label(root,text="Output",bg="#F2CCC3",font=("Calibre",15,"italic"))
label_ou.place(relx=0.63,rely=0.1,anchor=CENTER)
label_enter.place(relx=0.12,rely=0.1,anchor=CENTER)
label.place(relx=0.5,rely=0.03,anchor=CENTER)
txt=Text(root,width=40,height=20,relief="flat")
txt.place(relx=0.23,rely=0.5,anchor=CENTER)
txt1=Text(root,width=40,height=20,relief="flat")
txt1.place(relx=0.73,rely=0.5,anchor=CENTER)
LANGUAGES = {
    'af': 'afrikaans','sq': 'albanian','am': 'amharic','ar': 'arabic','hy': 'armenian','az': 'azerbaijani','eu': 'basque','be': 'belarusian','bn': 'bengali','bs': 'bosnian','bg': 'bulgarian','ca': 'catalan','ceb': 'cebuano','ny': 'chichewa','zh-cn': 'chinese (simplified)','zh-tw': 'chinese (traditional)','co': 'corsican','hr': 'croatian','cs': 'czech','da': 'danish','nl': 'dutch','en': 'english','eo': 'esperanto','et': 'estonian','tl': 'filipino','fi': 'finnish','fr': 'french','fy': 'frisian','gl': 'galician','ka': 'georgian','de': 'german','el': 'greek','gu': 'gujarati','ht': 'haitian creole','ha': 'hausa','haw': 'hawaiian','iw': 'hebrew','he': 'hebrew','hi': 'hindi','hmn': 'hmong','hu': 'hungarian','is': 'icelandic','ig': 'igbo','id': 'indonesian','ga': 'irish','it': 'italian','ja': 'japanese','jw': 'javanese','kn': 'kannada','kk': 'kazakh','km': 'khmer','ko': 'korean','ku': 'kurdish (kurmanji)','ky': 'kyrgyz','lo': 'lao','la': 'latin','lv': 'latvian','lt': 'lithuanian','lb': 'luxembourgish','mk': 'macedonian','mg': 'malagasy','ms': 'malay','ml': 'malayalam','mt': 'maltese','mi': 'maori','mr': 'marathi','mn': 'mongolian','my': 'myanmar (burmese)','ne': 'nepali','no': 'norwegian','or': 'odia','ps': 'pashto','fa': 'persian','pl': 'polish','pt': 'portuguese','pa': 'punjabi','ro': 'romanian','ru': 'russian','sm': 'samoan','gd': 'scots gaelic','sr': 'serbian','st': 'sesotho','sn': 'shona','sd': 'sindhi','si': 'sinhala','sk': 'slovak','sl': 'slovenian','so': 'somali','es': 'spanish','su': 'sundanese','sw': 'swahili','sv': 'swedish','tg': 'tajik','ta': 'tamil','te': 'telugu','th': 'thai','tr': 'turkish','uk': 'ukrainian','ur': 'urdu','ug': 'uyghur','uz': 'uzbek','vi': 'vietnamese','cy': 'welsh','xh': 'xhosa','yi': 'yiddish','yo': 'yoruba','zu': 'zulu',
}
key,values=zip(*LANGUAGES.items())
from_in=ttk.Combobox(root, width = 15,values=values) 
from_in.current(21)
from_in.place(relx=0.3,rely=0.1,anchor=CENTER)
from_out=ttk.Combobox(root, width = 15,values=values) 
from_out.current(21)
from_out.place(relx=0.8,rely=0.1,anchor=CENTER)
def do():
    result = translator.translate(txt.get("1.0",END),dest=key[values.index(from_out.get())])
    txt1.delete(1.0,END)
    txt1.insert(END,result.text)
btn=Button(root,text="Translate",bg="gold",relief="flat",font=("Calibre",15,"bold"),command=do)
btn.place(relx=0.48,rely=0.9,anchor=CENTER)
root.mainloop()

#,src=from_in.get(),dest=
