# merl
An open-source useless python library. Developed using the code.org IDE, because why not.
Use the following line on Windows to import merl:
```
pip install merl
```
If that doesn't work, then gimmie some time I gotta figure it out.

## Functions I want you to use
### send(pr) -- USE THIS
Sends 'pr' to Merl where 'pr' is a string. The response automatically prints out in the terminal/IDE, so don't resize the window to less than the width of 40 characters wide. Otherwise the unprinting function breaks.

---

## Functions that are supposed to be hidden
### printanim(msg)
Prints 'msg' where 'msg' is a string. If 'msg' does not have spaces, then it all prints at once. Else, it prints word-by-word.
If 'msg' spans longer than the terminal's horizontal size, then it will start duplicating the messages with each line.
Keep each 'msg' short, like Merl!

### replyPrint(prompt)
Where 'prompt' is a string. This makes Merl reply whatever, based on what you put in.
The reason why there are 2 "send" functions is because it has Merl check a thing or two before actually doing the reply checks, too.
Expect "I don't know." to show up more than once. With the exception of your system's time being between 9 AM and 4 PM, of course, because then you get a high traffic message more than half the time!
