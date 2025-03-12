import smtplib

my_email = "maheshneyveli22@gmail.com"
password = "wxfn aepv bpwj vsfu"
proxies = {
   'http': 'devproxy01.chq.ei:8080',
   'https': 'devproxy01.chq.ei:8080',
}

connection = smtplib.SMTP("smtp.gmail.com",465,proxies)

connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs= "maheswaran.elumalai@expeditors.com", msg = "Hello")
