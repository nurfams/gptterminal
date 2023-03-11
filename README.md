aplikasi ini modifikasi dari program https://github.com/acheong08/ChatGPT

# gptterminal
implementasi openai chat gpt ke windows terminal, linux, termux

# Untuk Instalasi Awal download python terlebih dahulu 
https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe

# Installasi
pip3 install --upgrade revChatGPT

# lalu clone repo ini terlebih dahulu
git clone https://github.com/nurfams/gptterminal.git

# Ubah Username dan Password atau menggunakan token
{ <br>
  "email": "email", <br>
  "password": "your password" <br>
} <br>
<br>
Kalau mau menggunakan token klik link ini : <br>
https://chat.openai.com/api/auth/session <br>
<br>
Ubah yang email dan password diatas Menjadi :
<br>
{ <br>
 "access_token": "<access_token>" <br>
} <br>

# jalankan di dalam folder atau  
di termux : python gpt.py <br>
di cmd    : gpt.py
