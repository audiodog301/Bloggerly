
print('Welcome to Blogger!\nSimply enter your information, and copy it into your html document. Please remember to put backslashes before quote marks and do not put in carriage returns. I\'m just too lazy to sanitize my inputs.')
title = input("What do you want your blog post to be called? ")
date = input("When are you writing this? ")
name = input("What is your name? ")
body = input("What do you want the body of your blog to say? ")

html = "<h1>" + title + "</h1>" + " Written <i>" + date + "</i>" + ", " + "By " + name + "<br><p>" + body
print(html)
