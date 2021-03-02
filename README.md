# college-tshirts
Send colleges emails to ask for free tshirts

----------------------------------------------------------------------------------------------------------------------------------------------

THINGS TO DO BEFORE RUNNING:

edit config.py and add your gmail credentials (username and password)

edit /text_files/emailTemplate.txt and make sure this is what you want to send to colleges
(make sure to put Sincerely, {your name} at the bottom. and write anything about yourself that you want the colleges to see)
(make sure to put your home address (or wherever you want to receive tshirts at))

run sendEmails.py to start the code (it will fail after some amount of emails are sent)
follow instructions regarding the variable 'start_at' in sendEmails.py to see how to handle when the code fails

after running sendEmails.py enough times, the program will exit without error. This means all emails have been sent

----------------------------------------------------------------------------------------------------------------------------------------------

IF YOU WANT TO ADD MORE COLLEGES TO THE LIST:

its easy!

add more lines in the files /text_files/emailList.txt and /text_files/fullCollegeList.txt
for example:
if you want to add Virginia Tech

you would add "vt" on a new line in emailList.txt and you would add "Virginia Tech" to the SAME LINE NUMBER in fullCollegeList.txt
it is important that the two new entries are on the same line number
the emailList.txt entry is important that you write the domain name (write vt if you plan on sending to ...@vt.edu). This must be the exact domain name you want to send to)
the fullCollegeList.txt entry is less important - this is how you will address the college in the email
    (ex: "Dear Virginia Tech" or "Dear Virginia Polytechnical State and University") both are fine. it doesn't really matter what you call them

A list of colleges that I have not implemented can be found in /text_files/moreColleges.txt
You can add these if you want, but need to find the correct domain name and append the correct files to add these colleges ^^^ see previous instructions

