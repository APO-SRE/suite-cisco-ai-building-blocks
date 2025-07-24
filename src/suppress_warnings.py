"""Suppress urllib3 SSL warnings for SD-WAN sandbox"""
import urllib3
import warnings

# Disable SSL warnings for sandbox environment
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Alternative: suppress all warnings from urllib3
warnings.filterwarnings('ignore', message='Unverified HTTPS request')