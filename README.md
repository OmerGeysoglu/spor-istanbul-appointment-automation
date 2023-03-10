# spor-istanbul-appointment-automation

Sport Istanbul is a service organized by the municipality, which has training in many sports branches. To attend training sessions, you must find a suitable appointment time. With this application, we have automated the system for those who have difficulty finding an appointment.

It is necessary to have a **twilio account** to access whatsapp messages
https://www.twilio.com/docs/whatsapp/quickstart/python

If you only want to use the version that works continuously in local, it is enough to edit the main.ipynb inside of **spor-istanbul-local** folder and run it.

In case you need to schedule your task you will need to use a **cron job**. We will be using **Heroku**, which offers a free scheduler (limited to 100 executions, after that you should set your cron job again).

After you create an account and deploy your project to Heroku, you will be able to set your scheduler.

## References:

Deploy Python Selenium based project live to Heroku:
https://github.com/akjasim/cb_selenium-python-deployment-heroku

Advanced Scheduler in Heroku:
https://medium.com/analytics-vidhya/schedule-a-python-script-on-heroku-a978b2f91ca8
