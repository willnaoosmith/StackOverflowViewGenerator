A script to generate views on questions on StackOverflow so you can get the "Notable question" and "Famous question" badge

how to use:
> install selenium and geckodriver (I used geckodriver version 26 and it goes well)

> put your user, password and user ID on the "user", "password" and "UserID" variables respectively.

> Create a crontab job to run this script every 15 minutes at least (For the view to be accounted) if you want to run it on a server (That's the purpose)

The crontab job to run it every 15 minutes is the following:

```
*/15 * * * * YourCommandHere >/dev/null 2>&1
```

In case of:
- Incorrect user
- Incorrect password
- captcha
- fire

nothing is going to work, bye.