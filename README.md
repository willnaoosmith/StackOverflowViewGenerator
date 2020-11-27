A script to generate views on questions on StackOverflow so you can get the "Notable question" and "Famous question" badge

how to use:
> install selenium and geckodriver (I used geckodriver version 26 and it goes well)
 
> To execute it (On linux) run passing the arguments using this manner:

`python StackOverflowAutomaticViews.py  '{"User": "User0Here", "Password": "Password0Here"}|{"User": "User1Here", "Password": "Password1Here"}' UserIdHere`

> Create a crontab job to run this script every 15 minutes at least (For the view to be accounted) if you want to run it on a server (That's the purpose)

The crontab job to run it every 16 minutes is the following:

```
*/16 * * * * YourCommandHere >/dev/null 2>&1
```

In case of:
- Incorrect user
- Incorrect password
- captcha
- fire

nothing is going to work, bye.
