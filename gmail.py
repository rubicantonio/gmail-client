import smtplib, ssl


print("make sure your gmail doesnt have 2 factor authentication")

message = input("enter message here: ")
sender = input("Your mail: ")
password = input("Your password: ")

print(message)
reciver = input("reciver: ")
print("sending mail")
port = 465
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:

	server.login(sender, password)
	server.sendmail(sender, reciver, message)
	print("Email sent")
