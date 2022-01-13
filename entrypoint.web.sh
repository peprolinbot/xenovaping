#!/bin/sh
gunicorn web:app -b 0.0.0.0:8000
