# app/llm/function_dispatcher/cloudlock_dispatcher.py
import os
from typing import Any
from app.llm.function_dispatcher import register
from app.llm.platform_clients.cloudlock_client import CloudlockClient

@register('listActivities')
def listActivities(ids: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if ids is not None:
        final_kwargs['ids'] = ids

    # No body parameter for this function.
    body_payload = None

    client = CloudlockClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.listActivities

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('listApplications')
def listApplications(classification: str = None, vendor: str = None, app_category: str = None, detected_at_after: str = None, detected_at_before: str = None, app_ids: str = None, scope_categories: str = None, install_state: str = None, count_total: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if classification is not None:
        final_kwargs['classification'] = classification
    if vendor is not None:
        final_kwargs['vendor'] = vendor
    if app_category is not None:
        final_kwargs['app_category'] = app_category
    if detected_at_after is not None:
        final_kwargs['detected_at_after'] = detected_at_after
    if detected_at_before is not None:
        final_kwargs['detected_at_before'] = detected_at_before
    if app_ids is not None:
        final_kwargs['app_ids'] = app_ids
    if scope_categories is not None:
        final_kwargs['scope_categories'] = scope_categories
    if install_state is not None:
        final_kwargs['install_state'] = install_state
    if count_total is not None:
        final_kwargs['count_total'] = count_total

    # No body parameter for this function.
    body_payload = None

    client = CloudlockClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.listApplications

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('listApplicationAccessScopes')
def listApplicationAccessScopes(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CloudlockClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.listApplicationAccessScopes

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('updateAppsClassification')
def updateAppsClassification(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CloudlockClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.updateAppsClassification

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('listApplicationInstallations')
def listApplicationInstallations(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CloudlockClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.listApplicationInstallations

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('listEntities')
def listEntities(platform: str = None, owners: str = None, exposure: str = None, asset_type: str = None, mime_type: str = None, updated_before: str = None, updated_after: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if platform is not None:
        final_kwargs['platform'] = platform
    if owners is not None:
        final_kwargs['owners'] = owners
    if exposure is not None:
        final_kwargs['exposure'] = exposure
    if asset_type is not None:
        final_kwargs['asset_type'] = asset_type
    if mime_type is not None:
        final_kwargs['mime_type'] = mime_type
    if updated_before is not None:
        final_kwargs['updated_before'] = updated_before
    if updated_after is not None:
        final_kwargs['updated_after'] = updated_after

    # No body parameter for this function.
    body_payload = None

    client = CloudlockClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.listEntities

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('listIncidentEntities')
def listIncidentEntities(id: int):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CloudlockClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.listIncidentEntities

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('listIncidents')
def listIncidents(incident_type: str = None, severity: str = None, policy_id: str = None, updated_before: str = None, updated_after: str = None, incident_status: str = None, vendor: str = None, customer_key: str = None, fields: str = None, order: str = None, flat: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if incident_type is not None:
        final_kwargs['incident_type'] = incident_type
    if severity is not None:
        final_kwargs['severity'] = severity
    if policy_id is not None:
        final_kwargs['policy_id'] = policy_id
    if updated_before is not None:
        final_kwargs['updated_before'] = updated_before
    if updated_after is not None:
        final_kwargs['updated_after'] = updated_after
    if incident_status is not None:
        final_kwargs['incident_status'] = incident_status
    if vendor is not None:
        final_kwargs['vendor'] = vendor
    if customer_key is not None:
        final_kwargs['customer_key'] = customer_key
    if fields is not None:
        final_kwargs['fields'] = fields
    if order is not None:
        final_kwargs['order'] = order
    if flat is not None:
        final_kwargs['flat'] = flat

    # No body parameter for this function.
    body_payload = None

    client = CloudlockClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.listIncidents

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('listIncidentAggregatesPolicies')
def listIncidentAggregatesPolicies(vendor: str = None, order: str = None, policies: str = None, users: str = None, status: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if vendor is not None:
        final_kwargs['vendor'] = vendor
    if order is not None:
        final_kwargs['order'] = order
    if policies is not None:
        final_kwargs['policies'] = policies
    if users is not None:
        final_kwargs['users'] = users
    if status is not None:
        final_kwargs['status'] = status

    # No body parameter for this function.
    body_payload = None

    client = CloudlockClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.listIncidentAggregatesPolicies

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('listIncidentAggregatesStatus')
def listIncidentAggregatesStatus():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CloudlockClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.listIncidentAggregatesStatus

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('listIncidentAggregatesUsers')
def listIncidentAggregatesUsers():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = CloudlockClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.listIncidentAggregatesUsers

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('getIncident')
def getIncident(id: int):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CloudlockClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.getIncident

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('updateIncident')
def updateIncident(id: int):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CloudlockClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.updateIncident

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('deleteEntriesIpSuspicious')
def deleteEntriesIpSuspicious(ids: str, Location: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if ids is not None:
        final_kwargs['ids'] = ids
    if Location is not None:
        final_kwargs['Location'] = Location

    # No body parameter for this function.
    body_payload = None

    client = CloudlockClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.deleteEntriesIpSuspicious

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('listEntriesIpSuspicious')
def listEntriesIpSuspicious(q: str = None, name: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if q is not None:
        final_kwargs['q'] = q
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = CloudlockClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.listEntriesIpSuspicious

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('importCsvEntriesIpSuspicious')
def importCsvEntriesIpSuspicious(file: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if file is not None:
        final_kwargs['file'] = file

    # No body parameter for this function.
    body_payload = None

    client = CloudlockClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.importCsvEntriesIpSuspicious

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('updateEntryIpSuspicious')
def updateEntryIpSuspicious(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CloudlockClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.updateEntryIpSuspicious

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('deleteEntriesIpTrusted')
def deleteEntriesIpTrusted(ids: str, Location: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if ids is not None:
        final_kwargs['ids'] = ids
    if Location is not None:
        final_kwargs['Location'] = Location

    # No body parameter for this function.
    body_payload = None

    client = CloudlockClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.deleteEntriesIpTrusted

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('listEntriesTrustedIp')
def listEntriesTrustedIp(q: str = None, name: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if q is not None:
        final_kwargs['q'] = q
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = CloudlockClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.listEntriesTrustedIp

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('importCsvEntriesIpTrusted')
def importCsvEntriesIpTrusted(file: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if file is not None:
        final_kwargs['file'] = file

    # No body parameter for this function.
    body_payload = None

    client = CloudlockClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.importCsvEntriesIpTrusted

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('updateEntryIpTrusted')
def updateEntryIpTrusted(id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = CloudlockClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.updateEntryIpTrusted

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('listPolicies')
def listPolicies(state: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if state is not None:
        final_kwargs['state'] = state

    # No body parameter for this function.
    body_payload = None

    client = CloudlockClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.listPolicies

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)
