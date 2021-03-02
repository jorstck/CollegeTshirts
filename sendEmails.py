from smtplib import *
import config

#edit config.py to change these fields
me = config.EMAIL_ADDRESS  # user email
password = config.EMAIL_PASSWORD # user password


ats = ["admissions@", "admission@", "admiss@"] 
# these are all the possible usernames for any given domain name
# you can add more if you want, or take some away
# for each domain name in emailList.txt, an email will be sent to admissions@{domain}.edu, admission@{domain}.edu, and admiss@{domain}.edu
# its easier to just try all of these than spend the time to figure out which one is correct
# the email simply will not send to any incorrect email addresses, so there's no harm in trying all 3 for each domain name


template = open("text_files/emailTemplate.txt").read() # reads in the template email to be sent

start = False
start_at = "northwestern" #used because the smtp will error after some time.. use this variable to choose which college to start at when sending emails
#if the smpt failed after sending emails to "admissions@vt.edu" you would make 'start_at' = vt (just the domain name)
#when the code errors again, update the 'start_at' variable, and give it some time before running again (theres no harm in trying immediately, it just wont work)
#if you have not begun sending emails, set 'start_at' to "adelphi" (this is the first college on the list)

with open("text_files/emailList.txt") as file1, open("text_files/fullCollegeList.txt") as file2:
    try:
        server = SMTP("smtp.gmail.com:587")
        #server.set_debuglevel(1) # useful for printing out more information about the server requests made by SMTP
        server.connect("smtp.gmail.com", "587")
        server.ehlo()
        server.starttls()
        server.login(me, password)
    except SMTPResponseException as e:
        print(e.smtp_code)

    for line1, line2 in zip(file1, file2):
        if(line1.strip()==start_at):
            start = True
        if(start):
            for a in ats:
                collegeEmail = a + line1.strip() + ".edu"
                college = line2.strip()
                msg = "Dear " + college + ",\n\n" + template

                msg = "From: " +me+"\nTo: "+collegeEmail+"\nSubject: Interest in your college\n"+msg
                

                try:
                    server.sendmail(me, collegeEmail, msg)
                    print("successfully sent email to " + collegeEmail)
                except SMTPResponseException as e:
                    print(e.smtp_code)
    
    server.quit()