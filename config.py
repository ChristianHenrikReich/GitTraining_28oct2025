# Application Configuration
# This file contains application-wide settings

# Database Configuration
DATABASE_URL = "sqlite:///course_app.db"
DATABASE_TIMEOUT = 30

# Application Settings
DEBUG_MODE = False
APP_NAME = "Git Course Application"
VERSION = "1.0.0"

# Feature Flags
ENABLE_LOGGING = True
ENABLE_EMAIL_NOTIFICATIONS = False
ENABLE_USER_REGISTRATION = True

# Limits
MAX_USERS = 1000
MAX_TASKS_PER_USER = 100
SESSION_TIMEOUT_MINUTES = 30