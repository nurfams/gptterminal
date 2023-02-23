#!/usr/bin/env python
from revChatGPT.V1 import Chatbot

chatbot = Chatbot(config={
    "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJudXJmYW1zNDZAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImdlb2lwX2NvdW50cnkiOiJJRCJ9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItWVFIZ3JuYllFQ2R4VHZnYzFLV3lZZldsIn0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJhdXRoMHw2M2Y1NjBkZGY4M2JkODE2ZTg4NzU0YTYiLCJhdWQiOlsiaHR0cHM6Ly9hcGkub3BlbmFpLmNvbS92MSIsImh0dHBzOi8vb3BlbmFpLm9wZW5haS5hdXRoMGFwcC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjc3MDI1OTQwLCJleHAiOjE2NzgyMzU1NDAsImF6cCI6IlRkSkljYmUxNldvVEh0Tjk1bnl5d2g1RTR5T282SXRHIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCBtb2RlbC5yZWFkIG1vZGVsLnJlcXVlc3Qgb3JnYW5pemF0aW9uLnJlYWQgb2ZmbGluZV9hY2Nlc3MifQ.zRee0eL7klwjz8UL9b2X70Rs2rX9zQQXupnOQhfYyIbLCAhBAgLdXatMbgqSoG-ELjvVDWtm1OavE_zA2ntLM6EPW2xrxKaeFR4uqXSgY9C4tfvv__3G9_Go8pYnlPrawDXIPQS90wUwQF-2t2qTdRaX7PrOTNs2SvWn8_RnZtv6-zHfJ9bN2jFwRXa9jKT84EkjtSPwSkFqByh6O4nkGF51OagayEHViT7vn8ozqdZS8dQhLSv8eS3GnFXrjjjPb4Qvn-bH7O6rDCP0IU6FpIPoROHzq_6jyDL7HcQMEwhPgxwm_s9e6Ok8uIt7591__uOV-ak8PUJ9iGBhADAFbw"
})

while True:

    print("")
    print("##########################################################################")
    print("")
    print("Jika mau keluar ketikkan exit")
    prev_text = ""
    text = (input("Masukkan pertanyaan : "))
    print("")
    print("############################# Jawaban ####################################")
    print("")
    for data in chatbot.ask(
        text,
    ):
        message = data["message"][len(prev_text) :]
        print(message, end="", flush=True)
        prev_text = data["message"]
    print()

    if text == "exit":
        print("pertanyaan dihentikan")
        break
