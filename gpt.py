#!/usr/bin/env python
from revChatGPT.V1 import Chatbot

chatbot = Chatbot(config={
  "email": "email",
  "password": "your password"
})

while True:
    print("")
    print("############################ Pertanyaan ###################################")
    print("")
    print("Jika mau keluar ketikkan exit / stop / berhenti")
    prev_text = ""
    text = (input("Masukkan pertanyaan : "))
    print("")
    print("############################# Jawaban ####################################")
    print("")

    if text in ["exit", "stop", "berhenti", ""]:
        print("pertanyaan dihentikan")
        break

    for data in chatbot.ask(
        text,
    ):
        message = data["message"][len(prev_text) :]
        print(message, end="", flush=True)
        prev_text = data["message"]
    print()
