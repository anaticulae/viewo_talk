#! /usr/bin/bash

export FLASK_APP=viewo_talk.app:create_app
# export FLASK_ENV=development

python -m flask run &
