#!/bin/bash

# Set heroku configuration variables and push to heroku
heroku config:set APP_ENVIRONMENT="PRODUCTION"
heroku config:set DB_USERNAME=""
heroku config:set DB_PASSWORD=""
heroku config:set DJANGO_KEY="#bs+nv%s7mefcx5*xk8r*6r3qxqya7bkbm*966yb8d(ki*tgvm"

# Push to heroku
git push heroku master

# Unset heroku configurations so that local env variables take effect
heroku config:unset APP_ENVIRONMENT
heroku config:unset DB_USERNAME
heroku config:unset DB_PASSWORD
heroku config:unset DJANGO_KEY
