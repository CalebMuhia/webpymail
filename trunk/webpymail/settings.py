# -*- coding: utf-8 -*-

# WebPyMail - IMAP python/django web mail client
# Copyright (C) 2008 Helder Guerreiro

## This file is part of WebPyMail.
##
## WebPyMail is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## WebPyMail is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with WebPyMail.  If not, see <http://www.gnu.org/licenses/>.

#
# Helder Guerreiro <helder@paxjulia.com>
#
# $LastChangedDate: 2008-04-23 19:09:14 +0100 (Wed, 23 Apr 2008) $
# $LastChangedRevision: 310M $
# $LastChangedBy: (local) $
# 

# Django settings for webpymail project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('SysAdn', 'sysadm@example.com'),
)
MANAGERS = ADMINS

# Local time zone for this installation. 
# Choices can be found here:
#  http://www.postgresql.org/docs/8.1/static/datetime-keywords.html
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as 
# your system time zone.
TIME_ZONE = 'WEST'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = './media/'

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '8v7=r99a*pjt(c@es=7wc1q2#d8ycj1!j6*zoy@pdg2y8@b*wt'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'webpymail.urls'

TEMPLATE_DIRS = ( 'templates' )

INSTALLED_APPS = (
    # Django apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    
    # WebPyMail apps
    'webpymail.wpmauth',
    'webpymail.mailapp',
    'webpymail.settingsapp',
)

######################
# WEBPYMAIL SETTINGS #
######################

DEFAULT_FOLDER = 'INBOX'

###################
# DJANGO SETTINGS #
###################

# Database Setup:

DATABASE_ENGINE = 'sqlite3'      # 'postgresql_psycopg2', 'postgresql', 
                                 # 'mysql',         'sqlite3' or 'ado_mssql'.
DATABASE_NAME = './webpymail.db' # Or path to database file if using sqlite3.
DATABASE_USER = ''               # Not used with sqlite3.
DATABASE_PASSWORD = ''           # Not used with sqlite3.
DATABASE_HOST = ''               # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''               # Set to empty string for default. Not used with sqlite3.

# User profiles:

AUTH_PROFILE_MODULE = 'mailapp.UserProfile'

# SESSIONS

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 28800       # 8 hours
SESSION_COOKIE_SECURE = False    # set to True if using https
SESSION_COOKIE_NAME = 'wpm_sessionid'

# AUTHENTICATION

AUTHENTICATION_BACKENDS = (
    'webpymail.wpmauth.backends.ImapBackend',
    'django.contrib.auth.backends.ModelBackend',
    )

LOGIN_URL  = '/auth/login/'
LOGOUT_URL = '/auth/logout/'

LOGOUT_SUCCESS = '/'
LOGIN_SUCCESS = '/mail/'

# DISPLAY SETTINGS

# TODO: this should be an user setting:
MESSAGES_PAGE = 50 # Number of messages per page to display

# Mail compose form
MAXADDRESSES = 50   # Maximum number of mails that can be used on a To, Cc or 
                    # Bcc field.
SINGLELINELEN = 60
TEXTAREAROWS = 15
TEXTAREACOLS = 60

# SMTP SETTINGS

SMTPHOST = 'example.com'
SMTPPORT = 25
SMTPUSER = None
SMTPPASS = None

# Attachments

# TODO: Check if the following dir exists, if not raise an exception
TEMPDIR = '/tmp/webpymail' # Temporary dir to store the attachements

###############################################
# Do not change anything beyond this point... #
###############################################

WEBPYMAIL_VERSION = 'SVN'