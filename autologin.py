from webbot import Browser 
web = Browser()
web.go_to('https://lms.cuchd.in') 
web.type('20BCS1509' , into='username')
web.click('NEXT' , tag='span')
web.type('@52535455Pp' , into='password' , id='password') # specific selection
web.click('submit' , tag='span') # you are logged in ^_^
