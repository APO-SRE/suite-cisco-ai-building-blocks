#!/usr/bin/env python3
"""
SD-WAN Alarm Wrapper

This module provides a wrapper for the getActiveAlarms function that automatically
adds default date parameters when none are provided.
"""
from datetime import datetime, timedelta
from app.llm.function_dispatcher.sdwan_mngr_dispatcher import getActiveAlarms as _original_getActiveAlarms


def getActiveAlarms(scrollId: str = None, startDate: str = None, endDate: str = None, 
                    count: int = None, timeZone: str = None):
    """
    Get active alarms with automatic date defaults.
    
    If no dates are provided, defaults to the last 24 hours.
    Date format: YYYY-MM-DDTHH:MM:SS (e.g., 2023-10-31T14:30:00)
    """
    # If no dates provided, default to last 24 hours
    if startDate is None and endDate is None:
        endDate = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        startDate = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%S')
    
    # Call the original function with the dates
    return _original_getActiveAlarms(
        scrollId=scrollId,
        startDate=startDate,
        endDate=endDate,
        count=count,
        timeZone=timeZone
    )


# Alternative: Register this wrapper to replace the original
def register_wrapper():
    """
    Register this wrapper to replace the original getActiveAlarms in the dispatcher.
    Call this after importing the dispatcher.
    """
    from app.llm.function_dispatcher import _registry
    from app.llm.function_dispatcher.sdwan_mngr_dispatcher import active_alarms, alarms_active, get_active_alarms, list_active_alarms, show_active_alarms
    
    # Replace all aliases with our wrapper
    _registry['getActiveAlarms'] = getActiveAlarms
    _registry['active_alarms'] = getActiveAlarms
    _registry['alarms_active'] = getActiveAlarms  
    _registry['get_active_alarms'] = getActiveAlarms
    _registry['list_active_alarms'] = getActiveAlarms
    _registry['show_active_alarms'] = getActiveAlarms