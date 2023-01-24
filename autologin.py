from webbot import Browser 
web = Browser()
web.go_to('https://lms.cuchd.in') 
web.type('20BCSCXXXX' , into='username')
web.click('NEXT' , tag='span')
web.type('pass@123' , into='password' , id='password') # specific selection
web.click('submit' , tag='span') # you are logged in ^_^
