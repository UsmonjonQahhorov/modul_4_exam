import smtplib

password_email = 'yeqzgnpuggwrpthv'
sender = "qohhorovusmonjon@gmail.com"
server = "smtp.gmail.com"
port = 465
reciever ="absaitovdev@gmail.com"

message = f"""
Sender : {sender}
Reciever : {reciever} 
Github_link : https://github.com/UsmonjonQahhorov/modul_4_exam
Dockerhub_link: qohhoroff/exam_bot:latest"""
with smtplib.SMTP_SSL(server, port) as server:
    server.login(sender, password_email)
    server.sendmail(sender, reciever, message)