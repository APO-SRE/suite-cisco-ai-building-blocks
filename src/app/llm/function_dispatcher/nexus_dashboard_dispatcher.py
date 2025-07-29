# app/llm/function_dispatcher/nexus_dashboard_dispatcher.py
import os
from typing import Any
from app.llm.function_dispatcher import register
from app.llm.platform_clients.nexus_dashboard_client import Nexus_dashboardClient

@register('post_login')
def post_login():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.post_login

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('login')(globals()['post_login'])

@register('login')
def login():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.login

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('get_nexus_api_federation_v4_federations')
def get_nexus_api_federation_v4_federations(AuthCookie: str = None, Cookie: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_api_federation_v4_federations

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_api_federation_v4_federation')(globals()['get_nexus_api_federation_v4_federations'])

# alias → easier for LLM
register('nexus_api_federation_v4_federations')(globals()['get_nexus_api_federation_v4_federations'])

@register('nexus_api_federation_v4_federation')
def nexus_api_federation_v4_federation(AuthCookie: str = None, Cookie: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_api_federation_v4_federation

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_federation_v4_federation')(globals()['nexus_api_federation_v4_federation'])

@register('nexus_api_federation_v4_federations')
def nexus_api_federation_v4_federations(AuthCookie: str = None, Cookie: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_api_federation_v4_federations

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_federation_v4_federation')(globals()['nexus_api_federation_v4_federations'])

# alias → easier for LLM
register('api_federation_v4_federations')(globals()['nexus_api_federation_v4_federations'])

@register('post_nexus_api_federation_v4_federations')
def post_nexus_api_federation_v4_federations(forceAdd: str = None, AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if forceAdd is not None:
        final_kwargs['forceAdd'] = forceAdd
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.post_nexus_api_federation_v4_federations

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_api_federation_v4_federation')(globals()['post_nexus_api_federation_v4_federations'])

# alias → easier for LLM
register('nexus_api_federation_v4_federations')(globals()['post_nexus_api_federation_v4_federations'])

@register('delete_nexus_api_federation_v4_federations_statusFederationID_')
def delete_nexus_api_federation_v4_federations_statusFederationID_(statusFederationID: str, forceAdd: str = None, AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if statusFederationID is not None:
        final_kwargs['statusFederationID'] = statusFederationID
    if forceAdd is not None:
        final_kwargs['forceAdd'] = forceAdd
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.delete_nexus_api_federation_v4_federations_statusFederationID_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_api_federation_v4_federations_statusFederationID_')(globals()['delete_nexus_api_federation_v4_federations_statusFederationID_'])

@register('nexus_api_federation_v4_federations_statusFederationID_')
def nexus_api_federation_v4_federations_statusFederationID_(statusFederationID: str, forceAdd: str = None, AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if statusFederationID is not None:
        final_kwargs['statusFederationID'] = statusFederationID
    if forceAdd is not None:
        final_kwargs['forceAdd'] = forceAdd
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_api_federation_v4_federations_statusFederationID_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_federation_v4_federations_statusFederationID_')(globals()['nexus_api_federation_v4_federations_statusFederationID_'])

@register('get_nexus_api_federation_v4_federations_statusFederationID_')
def get_nexus_api_federation_v4_federations_statusFederationID_(statusFederationID: str, AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if statusFederationID is not None:
        final_kwargs['statusFederationID'] = statusFederationID
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_api_federation_v4_federations_statusFederationID_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_api_federation_v4_federations_statusFederationID_')(globals()['get_nexus_api_federation_v4_federations_statusFederationID_'])

@register('get_nexus_api_federation_v4_members')
def get_nexus_api_federation_v4_members(AuthCookie: str = None, Cookie: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_api_federation_v4_members

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_api_federation_v4_member')(globals()['get_nexus_api_federation_v4_members'])

# alias → easier for LLM
register('nexus_api_federation_v4_members')(globals()['get_nexus_api_federation_v4_members'])

@register('nexus_api_federation_v4_member')
def nexus_api_federation_v4_member(AuthCookie: str = None, Cookie: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_api_federation_v4_member

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_federation_v4_member')(globals()['nexus_api_federation_v4_member'])

@register('nexus_api_federation_v4_members')
def nexus_api_federation_v4_members(AuthCookie: str = None, Cookie: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_api_federation_v4_members

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_federation_v4_member')(globals()['nexus_api_federation_v4_members'])

# alias → easier for LLM
register('api_federation_v4_members')(globals()['nexus_api_federation_v4_members'])

@register('post_nexus_api_federation_v4_members')
def post_nexus_api_federation_v4_members(forceAdd: str = None, AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if forceAdd is not None:
        final_kwargs['forceAdd'] = forceAdd
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.post_nexus_api_federation_v4_members

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_api_federation_v4_member')(globals()['post_nexus_api_federation_v4_members'])

# alias → easier for LLM
register('nexus_api_federation_v4_members')(globals()['post_nexus_api_federation_v4_members'])

@register('delete_nexus_api_federation_v4_members_statusMemberID_')
def delete_nexus_api_federation_v4_members_statusMemberID_(statusMemberID: str, forceDelete: str = None, AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if statusMemberID is not None:
        final_kwargs['statusMemberID'] = statusMemberID
    if forceDelete is not None:
        final_kwargs['forceDelete'] = forceDelete
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.delete_nexus_api_federation_v4_members_statusMemberID_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_api_federation_v4_members_statusMemberID_')(globals()['delete_nexus_api_federation_v4_members_statusMemberID_'])

@register('nexus_api_federation_v4_members_statusMemberID_')
def nexus_api_federation_v4_members_statusMemberID_(statusMemberID: str, forceDelete: str = None, AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if statusMemberID is not None:
        final_kwargs['statusMemberID'] = statusMemberID
    if forceDelete is not None:
        final_kwargs['forceDelete'] = forceDelete
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_api_federation_v4_members_statusMemberID_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_federation_v4_members_statusMemberID_')(globals()['nexus_api_federation_v4_members_statusMemberID_'])

@register('get_nexus_api_federation_v4_members_statusMemberID_')
def get_nexus_api_federation_v4_members_statusMemberID_(statusMemberID: str, AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if statusMemberID is not None:
        final_kwargs['statusMemberID'] = statusMemberID
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_api_federation_v4_members_statusMemberID_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_api_federation_v4_members_statusMemberID_')(globals()['get_nexus_api_federation_v4_members_statusMemberID_'])

@register('post_nexus_api_sitemanagement_v4_fabrics')
def post_nexus_api_sitemanagement_v4_fabrics(AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.post_nexus_api_sitemanagement_v4_fabrics

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_api_sitemanagement_v4_fabrics')(globals()['post_nexus_api_sitemanagement_v4_fabrics'])

# alias → easier for LLM
register('nexus_api_sitemanagement_v4_fabric')(globals()['post_nexus_api_sitemanagement_v4_fabrics'])

@register('nexus_api_sitemanagement_v4_fabrics')
def nexus_api_sitemanagement_v4_fabrics(AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_api_sitemanagement_v4_fabrics

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_sitemanagement_v4_fabrics')(globals()['nexus_api_sitemanagement_v4_fabrics'])

# alias → easier for LLM
register('api_sitemanagement_v4_fabric')(globals()['nexus_api_sitemanagement_v4_fabrics'])

@register('nexus_api_sitemanagement_v4_fabric')
def nexus_api_sitemanagement_v4_fabric(AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_api_sitemanagement_v4_fabric

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_sitemanagement_v4_fabric')(globals()['nexus_api_sitemanagement_v4_fabric'])

@register('get_nexus_api_sitemanagement_v4_sitegroups')
def get_nexus_api_sitemanagement_v4_sitegroups(AuthCookie: str = None, Cookie: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_api_sitemanagement_v4_sitegroups

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_api_sitemanagement_v4_sitegroups')(globals()['get_nexus_api_sitemanagement_v4_sitegroups'])

# alias → easier for LLM
register('nexus_api_sitemanagement_v4_sitegroup')(globals()['get_nexus_api_sitemanagement_v4_sitegroups'])

@register('nexus_api_sitemanagement_v4_sitegroups')
def nexus_api_sitemanagement_v4_sitegroups(AuthCookie: str = None, Cookie: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_api_sitemanagement_v4_sitegroups

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_sitemanagement_v4_sitegroup')(globals()['nexus_api_sitemanagement_v4_sitegroups'])

# alias → easier for LLM
register('api_sitemanagement_v4_sitegroups')(globals()['nexus_api_sitemanagement_v4_sitegroups'])

@register('nexus_api_sitemanagement_v4_sitegroup')
def nexus_api_sitemanagement_v4_sitegroup(AuthCookie: str = None, Cookie: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_api_sitemanagement_v4_sitegroup

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_sitemanagement_v4_sitegroup')(globals()['nexus_api_sitemanagement_v4_sitegroup'])

@register('post_nexus_api_sitemanagement_v4_sitegroups')
def post_nexus_api_sitemanagement_v4_sitegroups(AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.post_nexus_api_sitemanagement_v4_sitegroups

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_api_sitemanagement_v4_sitegroups')(globals()['post_nexus_api_sitemanagement_v4_sitegroups'])

# alias → easier for LLM
register('nexus_api_sitemanagement_v4_sitegroup')(globals()['post_nexus_api_sitemanagement_v4_sitegroups'])

@register('delete_nexus_api_sitemanagement_v4_sitegroups_specName_')
def delete_nexus_api_sitemanagement_v4_sitegroups_specName_(specName: str, forceDelete: str = None, AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if forceDelete is not None:
        final_kwargs['forceDelete'] = forceDelete
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.delete_nexus_api_sitemanagement_v4_sitegroups_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_api_sitemanagement_v4_sitegroups_specName_')(globals()['delete_nexus_api_sitemanagement_v4_sitegroups_specName_'])

@register('nexus_api_sitemanagement_v4_sitegroups_specName_')
def nexus_api_sitemanagement_v4_sitegroups_specName_(specName: str, forceDelete: str = None, AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if forceDelete is not None:
        final_kwargs['forceDelete'] = forceDelete
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_api_sitemanagement_v4_sitegroups_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_sitemanagement_v4_sitegroups_specName_')(globals()['nexus_api_sitemanagement_v4_sitegroups_specName_'])

@register('get_nexus_api_sitemanagement_v4_sitegroups_specName_')
def get_nexus_api_sitemanagement_v4_sitegroups_specName_(specName: str, AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_api_sitemanagement_v4_sitegroups_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_api_sitemanagement_v4_sitegroups_specName_')(globals()['get_nexus_api_sitemanagement_v4_sitegroups_specName_'])

@register('patch_nexus_api_sitemanagement_v4_sitegroups_specName_')
def patch_nexus_api_sitemanagement_v4_sitegroups_specName_(specName: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.patch_nexus_api_sitemanagement_v4_sitegroups_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_api_sitemanagement_v4_sitegroups_specName_')(globals()['patch_nexus_api_sitemanagement_v4_sitegroups_specName_'])

@register('put_nexus_api_sitemanagement_v4_sitegroups_specName_')
def put_nexus_api_sitemanagement_v4_sitegroups_specName_(specName: str, AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.put_nexus_api_sitemanagement_v4_sitegroups_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_api_sitemanagement_v4_sitegroups_specName_')(globals()['put_nexus_api_sitemanagement_v4_sitegroups_specName_'])

@register('get_nexus_api_sitemanagement_v4_sites')
def get_nexus_api_sitemanagement_v4_sites(AuthCookie: str = None, Cookie: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_api_sitemanagement_v4_sites

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_api_sitemanagement_v4_sites')(globals()['get_nexus_api_sitemanagement_v4_sites'])

# alias → easier for LLM
register('nexus_api_sitemanagement_v4_site')(globals()['get_nexus_api_sitemanagement_v4_sites'])

@register('nexus_api_sitemanagement_v4_sites')
def nexus_api_sitemanagement_v4_sites(AuthCookie: str = None, Cookie: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_api_sitemanagement_v4_sites

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_sitemanagement_v4_sites')(globals()['nexus_api_sitemanagement_v4_sites'])

# alias → easier for LLM
register('api_sitemanagement_v4_site')(globals()['nexus_api_sitemanagement_v4_sites'])

@register('nexus_api_sitemanagement_v4_site')
def nexus_api_sitemanagement_v4_site(AuthCookie: str = None, Cookie: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_api_sitemanagement_v4_site

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_sitemanagement_v4_site')(globals()['nexus_api_sitemanagement_v4_site'])

@register('post_nexus_api_sitemanagement_v4_sites')
def post_nexus_api_sitemanagement_v4_sites(forceAdd: str = None, AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if forceAdd is not None:
        final_kwargs['forceAdd'] = forceAdd
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.post_nexus_api_sitemanagement_v4_sites

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_api_sitemanagement_v4_sites')(globals()['post_nexus_api_sitemanagement_v4_sites'])

# alias → easier for LLM
register('nexus_api_sitemanagement_v4_site')(globals()['post_nexus_api_sitemanagement_v4_sites'])

@register('delete_nexus_api_sitemanagement_v4_sites_specName_')
def delete_nexus_api_sitemanagement_v4_sites_specName_(specName: str, forceDelete: str = None, AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if forceDelete is not None:
        final_kwargs['forceDelete'] = forceDelete
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.delete_nexus_api_sitemanagement_v4_sites_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_api_sitemanagement_v4_sites_specName_')(globals()['delete_nexus_api_sitemanagement_v4_sites_specName_'])

@register('nexus_api_sitemanagement_v4_sites_specName_')
def nexus_api_sitemanagement_v4_sites_specName_(specName: str, forceDelete: str = None, AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if forceDelete is not None:
        final_kwargs['forceDelete'] = forceDelete
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_api_sitemanagement_v4_sites_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_sitemanagement_v4_sites_specName_')(globals()['nexus_api_sitemanagement_v4_sites_specName_'])

@register('get_nexus_api_sitemanagement_v4_sites_specName_')
def get_nexus_api_sitemanagement_v4_sites_specName_(specName: str, AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_api_sitemanagement_v4_sites_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_api_sitemanagement_v4_sites_specName_')(globals()['get_nexus_api_sitemanagement_v4_sites_specName_'])

@register('put_nexus_api_sitemanagement_v4_sites_specName_')
def put_nexus_api_sitemanagement_v4_sites_specName_(specName: str, AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.put_nexus_api_sitemanagement_v4_sites_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_api_sitemanagement_v4_sites_specName_')(globals()['put_nexus_api_sitemanagement_v4_sites_specName_'])

@register('get_nexus_infra_api_aaa_v4_defaultauth')
def get_nexus_infra_api_aaa_v4_defaultauth(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_aaa_v4_defaultauth

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_defaultauth')(globals()['get_nexus_infra_api_aaa_v4_defaultauth'])

@register('nexus_infra_api_aaa_v4_defaultauth')
def nexus_infra_api_aaa_v4_defaultauth(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_aaa_v4_defaultauth

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_aaa_v4_defaultauth')(globals()['nexus_infra_api_aaa_v4_defaultauth'])

@register('get_nexus_infra_api_aaa_v4_defaultauth_specDefaultDomain_')
def get_nexus_infra_api_aaa_v4_defaultauth_specDefaultDomain_(specDefaultDomain: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specDefaultDomain is not None:
        final_kwargs['specDefaultDomain'] = specDefaultDomain
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_aaa_v4_defaultauth_specDefaultDomain_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_defaultauth_specDefaultDomain_')(globals()['get_nexus_infra_api_aaa_v4_defaultauth_specDefaultDomain_'])

@register('nexus_infra_api_aaa_v4_defaultauth_specDefaultDomain_')
def nexus_infra_api_aaa_v4_defaultauth_specDefaultDomain_(specDefaultDomain: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specDefaultDomain is not None:
        final_kwargs['specDefaultDomain'] = specDefaultDomain
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_aaa_v4_defaultauth_specDefaultDomain_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_aaa_v4_defaultauth_specDefaultDomain_')(globals()['nexus_infra_api_aaa_v4_defaultauth_specDefaultDomain_'])

@register('put_nexus_infra_api_aaa_v4_defaultauth_specDefaultDomain_')
def put_nexus_infra_api_aaa_v4_defaultauth_specDefaultDomain_(specDefaultDomain: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specDefaultDomain is not None:
        final_kwargs['specDefaultDomain'] = specDefaultDomain
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.put_nexus_infra_api_aaa_v4_defaultauth_specDefaultDomain_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_defaultauth_specDefaultDomain_')(globals()['put_nexus_infra_api_aaa_v4_defaultauth_specDefaultDomain_'])

@register('get_nexus_infra_api_aaa_v4_gatewayconfiguration')
def get_nexus_infra_api_aaa_v4_gatewayconfiguration(showSecret: str = None, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if showSecret is not None:
        final_kwargs['showSecret'] = showSecret
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_aaa_v4_gatewayconfiguration

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_gatewayconfiguration')(globals()['get_nexus_infra_api_aaa_v4_gatewayconfiguration'])

@register('nexus_infra_api_aaa_v4_gatewayconfiguration')
def nexus_infra_api_aaa_v4_gatewayconfiguration(showSecret: str = None, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if showSecret is not None:
        final_kwargs['showSecret'] = showSecret
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_aaa_v4_gatewayconfiguration

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_aaa_v4_gatewayconfiguration')(globals()['nexus_infra_api_aaa_v4_gatewayconfiguration'])

@register('get_nexus_infra_api_aaa_v4_gatewayconfiguration_specName_')
def get_nexus_infra_api_aaa_v4_gatewayconfiguration_specName_(specName: str, showSecret: str = None, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if showSecret is not None:
        final_kwargs['showSecret'] = showSecret
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_aaa_v4_gatewayconfiguration_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_gatewayconfiguration_specName_')(globals()['get_nexus_infra_api_aaa_v4_gatewayconfiguration_specName_'])

@register('nexus_infra_api_aaa_v4_gatewayconfiguration_specName_')
def nexus_infra_api_aaa_v4_gatewayconfiguration_specName_(specName: str, showSecret: str = None, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if showSecret is not None:
        final_kwargs['showSecret'] = showSecret
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_aaa_v4_gatewayconfiguration_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_aaa_v4_gatewayconfiguration_specName_')(globals()['nexus_infra_api_aaa_v4_gatewayconfiguration_specName_'])

@register('put_nexus_infra_api_aaa_v4_gatewayconfiguration_specName_')
def put_nexus_infra_api_aaa_v4_gatewayconfiguration_specName_(specName: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.put_nexus_infra_api_aaa_v4_gatewayconfiguration_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_gatewayconfiguration_specName_')(globals()['put_nexus_infra_api_aaa_v4_gatewayconfiguration_specName_'])

@register('get_nexus_infra_api_aaa_v4_localusers')
def get_nexus_infra_api_aaa_v4_localusers(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_aaa_v4_localusers

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_localusers')(globals()['get_nexus_infra_api_aaa_v4_localusers'])

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_localuser')(globals()['get_nexus_infra_api_aaa_v4_localusers'])

@register('nexus_infra_api_aaa_v4_localusers')
def nexus_infra_api_aaa_v4_localusers(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_aaa_v4_localusers

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_aaa_v4_localuser')(globals()['nexus_infra_api_aaa_v4_localusers'])

# alias → easier for LLM
register('infra_api_aaa_v4_localusers')(globals()['nexus_infra_api_aaa_v4_localusers'])

@register('nexus_infra_api_aaa_v4_localuser')
def nexus_infra_api_aaa_v4_localuser(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_aaa_v4_localuser

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_aaa_v4_localuser')(globals()['nexus_infra_api_aaa_v4_localuser'])

@register('post_nexus_infra_api_aaa_v4_localusers')
def post_nexus_infra_api_aaa_v4_localusers(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.post_nexus_infra_api_aaa_v4_localusers

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_localusers')(globals()['post_nexus_infra_api_aaa_v4_localusers'])

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_localuser')(globals()['post_nexus_infra_api_aaa_v4_localusers'])

@register('delete_nexus_infra_api_aaa_v4_localusers_specLoginID_')
def delete_nexus_infra_api_aaa_v4_localusers_specLoginID_(specLoginID: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specLoginID is not None:
        final_kwargs['specLoginID'] = specLoginID
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.delete_nexus_infra_api_aaa_v4_localusers_specLoginID_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_localusers_specLoginID_')(globals()['delete_nexus_infra_api_aaa_v4_localusers_specLoginID_'])

@register('nexus_infra_api_aaa_v4_localusers_specLoginID_')
def nexus_infra_api_aaa_v4_localusers_specLoginID_(specLoginID: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specLoginID is not None:
        final_kwargs['specLoginID'] = specLoginID
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_aaa_v4_localusers_specLoginID_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_aaa_v4_localusers_specLoginID_')(globals()['nexus_infra_api_aaa_v4_localusers_specLoginID_'])

@register('get_nexus_infra_api_aaa_v4_localusers_specLoginID_')
def get_nexus_infra_api_aaa_v4_localusers_specLoginID_(specLoginID: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specLoginID is not None:
        final_kwargs['specLoginID'] = specLoginID
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_aaa_v4_localusers_specLoginID_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_localusers_specLoginID_')(globals()['get_nexus_infra_api_aaa_v4_localusers_specLoginID_'])

@register('put_nexus_infra_api_aaa_v4_localusers_specLoginID_')
def put_nexus_infra_api_aaa_v4_localusers_specLoginID_(specLoginID: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specLoginID is not None:
        final_kwargs['specLoginID'] = specLoginID
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.put_nexus_infra_api_aaa_v4_localusers_specLoginID_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_localusers_specLoginID_')(globals()['put_nexus_infra_api_aaa_v4_localusers_specLoginID_'])

@register('get_nexus_infra_api_aaa_v4_logindomains')
def get_nexus_infra_api_aaa_v4_logindomains(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_aaa_v4_logindomains

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_logindomains')(globals()['get_nexus_infra_api_aaa_v4_logindomains'])

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_logindomain')(globals()['get_nexus_infra_api_aaa_v4_logindomains'])

@register('nexus_infra_api_aaa_v4_logindomains')
def nexus_infra_api_aaa_v4_logindomains(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_aaa_v4_logindomains

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_aaa_v4_logindomain')(globals()['nexus_infra_api_aaa_v4_logindomains'])

# alias → easier for LLM
register('infra_api_aaa_v4_logindomains')(globals()['nexus_infra_api_aaa_v4_logindomains'])

@register('nexus_infra_api_aaa_v4_logindomain')
def nexus_infra_api_aaa_v4_logindomain(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_aaa_v4_logindomain

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_aaa_v4_logindomain')(globals()['nexus_infra_api_aaa_v4_logindomain'])

@register('post_nexus_infra_api_aaa_v4_logindomains')
def post_nexus_infra_api_aaa_v4_logindomains(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.post_nexus_infra_api_aaa_v4_logindomains

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_logindomains')(globals()['post_nexus_infra_api_aaa_v4_logindomains'])

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_logindomain')(globals()['post_nexus_infra_api_aaa_v4_logindomains'])

@register('delete_nexus_infra_api_aaa_v4_logindomains_specDomain_')
def delete_nexus_infra_api_aaa_v4_logindomains_specDomain_(specDomain: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specDomain is not None:
        final_kwargs['specDomain'] = specDomain
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.delete_nexus_infra_api_aaa_v4_logindomains_specDomain_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_logindomains_specDomain_')(globals()['delete_nexus_infra_api_aaa_v4_logindomains_specDomain_'])

@register('nexus_infra_api_aaa_v4_logindomains_specDomain_')
def nexus_infra_api_aaa_v4_logindomains_specDomain_(specDomain: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specDomain is not None:
        final_kwargs['specDomain'] = specDomain
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_aaa_v4_logindomains_specDomain_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_aaa_v4_logindomains_specDomain_')(globals()['nexus_infra_api_aaa_v4_logindomains_specDomain_'])

@register('get_nexus_infra_api_aaa_v4_logindomains_specDomain_')
def get_nexus_infra_api_aaa_v4_logindomains_specDomain_(specDomain: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specDomain is not None:
        final_kwargs['specDomain'] = specDomain
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_aaa_v4_logindomains_specDomain_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_logindomains_specDomain_')(globals()['get_nexus_infra_api_aaa_v4_logindomains_specDomain_'])

@register('put_nexus_infra_api_aaa_v4_logindomains_specDomain_')
def put_nexus_infra_api_aaa_v4_logindomains_specDomain_(specDomain: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specDomain is not None:
        final_kwargs['specDomain'] = specDomain
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.put_nexus_infra_api_aaa_v4_logindomains_specDomain_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_logindomains_specDomain_')(globals()['put_nexus_infra_api_aaa_v4_logindomains_specDomain_'])

@register('get_nexus_infra_api_aaa_v4_remoteusers')
def get_nexus_infra_api_aaa_v4_remoteusers(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_aaa_v4_remoteusers

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_remoteusers')(globals()['get_nexus_infra_api_aaa_v4_remoteusers'])

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_remoteuser')(globals()['get_nexus_infra_api_aaa_v4_remoteusers'])

@register('nexus_infra_api_aaa_v4_remoteusers')
def nexus_infra_api_aaa_v4_remoteusers(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_aaa_v4_remoteusers

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_aaa_v4_remoteusers')(globals()['nexus_infra_api_aaa_v4_remoteusers'])

# alias → easier for LLM
register('infra_api_aaa_v4_remoteuser')(globals()['nexus_infra_api_aaa_v4_remoteusers'])

@register('nexus_infra_api_aaa_v4_remoteuser')
def nexus_infra_api_aaa_v4_remoteuser(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_aaa_v4_remoteuser

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_aaa_v4_remoteuser')(globals()['nexus_infra_api_aaa_v4_remoteuser'])

@register('get_nexus_infra_api_aaa_v4_remoteusers_specLoginID_')
def get_nexus_infra_api_aaa_v4_remoteusers_specLoginID_(specLoginID: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specLoginID is not None:
        final_kwargs['specLoginID'] = specLoginID
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_aaa_v4_remoteusers_specLoginID_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_remoteusers_specLoginID_')(globals()['get_nexus_infra_api_aaa_v4_remoteusers_specLoginID_'])

@register('nexus_infra_api_aaa_v4_remoteusers_specLoginID_')
def nexus_infra_api_aaa_v4_remoteusers_specLoginID_(specLoginID: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specLoginID is not None:
        final_kwargs['specLoginID'] = specLoginID
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_aaa_v4_remoteusers_specLoginID_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_aaa_v4_remoteusers_specLoginID_')(globals()['nexus_infra_api_aaa_v4_remoteusers_specLoginID_'])

@register('get_nexus_infra_api_aaa_v4_securitydomains')
def get_nexus_infra_api_aaa_v4_securitydomains(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_aaa_v4_securitydomains

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_securitydomain')(globals()['get_nexus_infra_api_aaa_v4_securitydomains'])

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_securitydomains')(globals()['get_nexus_infra_api_aaa_v4_securitydomains'])

@register('nexus_infra_api_aaa_v4_securitydomain')
def nexus_infra_api_aaa_v4_securitydomain(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_aaa_v4_securitydomain

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_aaa_v4_securitydomain')(globals()['nexus_infra_api_aaa_v4_securitydomain'])

@register('nexus_infra_api_aaa_v4_securitydomains')
def nexus_infra_api_aaa_v4_securitydomains(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_aaa_v4_securitydomains

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_aaa_v4_securitydomain')(globals()['nexus_infra_api_aaa_v4_securitydomains'])

# alias → easier for LLM
register('infra_api_aaa_v4_securitydomains')(globals()['nexus_infra_api_aaa_v4_securitydomains'])

@register('post_nexus_infra_api_aaa_v4_securitydomains')
def post_nexus_infra_api_aaa_v4_securitydomains(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.post_nexus_infra_api_aaa_v4_securitydomains

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_securitydomain')(globals()['post_nexus_infra_api_aaa_v4_securitydomains'])

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_securitydomains')(globals()['post_nexus_infra_api_aaa_v4_securitydomains'])

@register('delete_nexus_infra_api_aaa_v4_securitydomains_specName_')
def delete_nexus_infra_api_aaa_v4_securitydomains_specName_(specName: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.delete_nexus_infra_api_aaa_v4_securitydomains_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_securitydomains_specName_')(globals()['delete_nexus_infra_api_aaa_v4_securitydomains_specName_'])

@register('nexus_infra_api_aaa_v4_securitydomains_specName_')
def nexus_infra_api_aaa_v4_securitydomains_specName_(specName: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_aaa_v4_securitydomains_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_aaa_v4_securitydomains_specName_')(globals()['nexus_infra_api_aaa_v4_securitydomains_specName_'])

@register('get_nexus_infra_api_aaa_v4_securitydomains_specName_')
def get_nexus_infra_api_aaa_v4_securitydomains_specName_(specName: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_aaa_v4_securitydomains_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_securitydomains_specName_')(globals()['get_nexus_infra_api_aaa_v4_securitydomains_specName_'])

@register('put_nexus_infra_api_aaa_v4_securitydomains_specName_')
def put_nexus_infra_api_aaa_v4_securitydomains_specName_(specName: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.put_nexus_infra_api_aaa_v4_securitydomains_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_securitydomains_specName_')(globals()['put_nexus_infra_api_aaa_v4_securitydomains_specName_'])

@register('get_nexus_infra_api_aaa_v4_trustedjwtkeys')
def get_nexus_infra_api_aaa_v4_trustedjwtkeys(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_aaa_v4_trustedjwtkeys

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_trustedjwtkey')(globals()['get_nexus_infra_api_aaa_v4_trustedjwtkeys'])

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_trustedjwtkeys')(globals()['get_nexus_infra_api_aaa_v4_trustedjwtkeys'])

@register('nexus_infra_api_aaa_v4_trustedjwtkey')
def nexus_infra_api_aaa_v4_trustedjwtkey(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_aaa_v4_trustedjwtkey

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_aaa_v4_trustedjwtkey')(globals()['nexus_infra_api_aaa_v4_trustedjwtkey'])

@register('nexus_infra_api_aaa_v4_trustedjwtkeys')
def nexus_infra_api_aaa_v4_trustedjwtkeys(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_aaa_v4_trustedjwtkeys

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_aaa_v4_trustedjwtkey')(globals()['nexus_infra_api_aaa_v4_trustedjwtkeys'])

# alias → easier for LLM
register('infra_api_aaa_v4_trustedjwtkeys')(globals()['nexus_infra_api_aaa_v4_trustedjwtkeys'])

@register('post_nexus_infra_api_aaa_v4_trustedjwtkeys')
def post_nexus_infra_api_aaa_v4_trustedjwtkeys(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.post_nexus_infra_api_aaa_v4_trustedjwtkeys

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_trustedjwtkey')(globals()['post_nexus_infra_api_aaa_v4_trustedjwtkeys'])

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_trustedjwtkeys')(globals()['post_nexus_infra_api_aaa_v4_trustedjwtkeys'])

@register('delete_nexus_infra_api_aaa_v4_trustedjwtkeys_specKeyID_')
def delete_nexus_infra_api_aaa_v4_trustedjwtkeys_specKeyID_(specKeyID: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specKeyID is not None:
        final_kwargs['specKeyID'] = specKeyID
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.delete_nexus_infra_api_aaa_v4_trustedjwtkeys_specKeyID_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_trustedjwtkeys_specKeyID_')(globals()['delete_nexus_infra_api_aaa_v4_trustedjwtkeys_specKeyID_'])

@register('nexus_infra_api_aaa_v4_trustedjwtkeys_specKeyID_')
def nexus_infra_api_aaa_v4_trustedjwtkeys_specKeyID_(specKeyID: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specKeyID is not None:
        final_kwargs['specKeyID'] = specKeyID
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_aaa_v4_trustedjwtkeys_specKeyID_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_aaa_v4_trustedjwtkeys_specKeyID_')(globals()['nexus_infra_api_aaa_v4_trustedjwtkeys_specKeyID_'])

@register('get_nexus_infra_api_aaa_v4_trustedjwtkeys_specKeyID_')
def get_nexus_infra_api_aaa_v4_trustedjwtkeys_specKeyID_(specKeyID: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specKeyID is not None:
        final_kwargs['specKeyID'] = specKeyID
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_aaa_v4_trustedjwtkeys_specKeyID_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_trustedjwtkeys_specKeyID_')(globals()['get_nexus_infra_api_aaa_v4_trustedjwtkeys_specKeyID_'])

@register('put_nexus_infra_api_aaa_v4_trustedjwtkeys_specKeyID_')
def put_nexus_infra_api_aaa_v4_trustedjwtkeys_specKeyID_(specKeyID: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specKeyID is not None:
        final_kwargs['specKeyID'] = specKeyID
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.put_nexus_infra_api_aaa_v4_trustedjwtkeys_specKeyID_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_trustedjwtkeys_specKeyID_')(globals()['put_nexus_infra_api_aaa_v4_trustedjwtkeys_specKeyID_'])

@register('get_nexus_infra_api_aaa_v4_userapikeys')
def get_nexus_infra_api_aaa_v4_userapikeys(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_aaa_v4_userapikeys

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_userapikeys')(globals()['get_nexus_infra_api_aaa_v4_userapikeys'])

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_userapikey')(globals()['get_nexus_infra_api_aaa_v4_userapikeys'])

@register('nexus_infra_api_aaa_v4_userapikeys')
def nexus_infra_api_aaa_v4_userapikeys(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_aaa_v4_userapikeys

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_aaa_v4_userapikeys')(globals()['nexus_infra_api_aaa_v4_userapikeys'])

# alias → easier for LLM
register('infra_api_aaa_v4_userapikey')(globals()['nexus_infra_api_aaa_v4_userapikeys'])

@register('nexus_infra_api_aaa_v4_userapikey')
def nexus_infra_api_aaa_v4_userapikey(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_aaa_v4_userapikey

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_aaa_v4_userapikey')(globals()['nexus_infra_api_aaa_v4_userapikey'])

@register('post_nexus_infra_api_aaa_v4_userapikeys')
def post_nexus_infra_api_aaa_v4_userapikeys(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.post_nexus_infra_api_aaa_v4_userapikeys

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_userapikeys')(globals()['post_nexus_infra_api_aaa_v4_userapikeys'])

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_userapikey')(globals()['post_nexus_infra_api_aaa_v4_userapikeys'])

@register('delete_nexus_infra_api_aaa_v4_userapikeys_specUuid_')
def delete_nexus_infra_api_aaa_v4_userapikeys_specUuid_(specUuid: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specUuid is not None:
        final_kwargs['specUuid'] = specUuid
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.delete_nexus_infra_api_aaa_v4_userapikeys_specUuid_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_userapikeys_specUuid_')(globals()['delete_nexus_infra_api_aaa_v4_userapikeys_specUuid_'])

@register('nexus_infra_api_aaa_v4_userapikeys_specUuid_')
def nexus_infra_api_aaa_v4_userapikeys_specUuid_(specUuid: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specUuid is not None:
        final_kwargs['specUuid'] = specUuid
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_aaa_v4_userapikeys_specUuid_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_aaa_v4_userapikeys_specUuid_')(globals()['nexus_infra_api_aaa_v4_userapikeys_specUuid_'])

@register('get_nexus_infra_api_aaa_v4_userapikeys_specUuid_')
def get_nexus_infra_api_aaa_v4_userapikeys_specUuid_(specUuid: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specUuid is not None:
        final_kwargs['specUuid'] = specUuid
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_aaa_v4_userapikeys_specUuid_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_userapikeys_specUuid_')(globals()['get_nexus_infra_api_aaa_v4_userapikeys_specUuid_'])

@register('put_nexus_infra_api_aaa_v4_userapikeys_specUuid_')
def put_nexus_infra_api_aaa_v4_userapikeys_specUuid_(specUuid: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specUuid is not None:
        final_kwargs['specUuid'] = specUuid
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.put_nexus_infra_api_aaa_v4_userapikeys_specUuid_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_userapikeys_specUuid_')(globals()['put_nexus_infra_api_aaa_v4_userapikeys_specUuid_'])

@register('get_nexus_infra_api_aaa_v4_userpreferences')
def get_nexus_infra_api_aaa_v4_userpreferences(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_aaa_v4_userpreferences

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_userpreferences')(globals()['get_nexus_infra_api_aaa_v4_userpreferences'])

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_userpreference')(globals()['get_nexus_infra_api_aaa_v4_userpreferences'])

@register('nexus_infra_api_aaa_v4_userpreferences')
def nexus_infra_api_aaa_v4_userpreferences(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_aaa_v4_userpreferences

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_aaa_v4_userpreferences')(globals()['nexus_infra_api_aaa_v4_userpreferences'])

# alias → easier for LLM
register('infra_api_aaa_v4_userpreference')(globals()['nexus_infra_api_aaa_v4_userpreferences'])

@register('nexus_infra_api_aaa_v4_userpreference')
def nexus_infra_api_aaa_v4_userpreference(AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_aaa_v4_userpreference

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_aaa_v4_userpreference')(globals()['nexus_infra_api_aaa_v4_userpreference'])

@register('get_nexus_infra_api_aaa_v4_userpreferences_specLoginID_')
def get_nexus_infra_api_aaa_v4_userpreferences_specLoginID_(specLoginID: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specLoginID is not None:
        final_kwargs['specLoginID'] = specLoginID
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_aaa_v4_userpreferences_specLoginID_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_userpreferences_specLoginID_')(globals()['get_nexus_infra_api_aaa_v4_userpreferences_specLoginID_'])

@register('nexus_infra_api_aaa_v4_userpreferences_specLoginID_')
def nexus_infra_api_aaa_v4_userpreferences_specLoginID_(specLoginID: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specLoginID is not None:
        final_kwargs['specLoginID'] = specLoginID
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_aaa_v4_userpreferences_specLoginID_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_aaa_v4_userpreferences_specLoginID_')(globals()['nexus_infra_api_aaa_v4_userpreferences_specLoginID_'])

@register('put_nexus_infra_api_aaa_v4_userpreferences_specLoginID_')
def put_nexus_infra_api_aaa_v4_userpreferences_specLoginID_(specLoginID: str, AuthCookie: str = None, Cookie: str = None, X_Csrf_Token: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specLoginID is not None:
        final_kwargs['specLoginID'] = specLoginID
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if X_Csrf_Token is not None:
        final_kwargs['X-Csrf-Token'] = X_Csrf_Token

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.put_nexus_infra_api_aaa_v4_userpreferences_specLoginID_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_aaa_v4_userpreferences_specLoginID_')(globals()['put_nexus_infra_api_aaa_v4_userpreferences_specLoginID_'])

@register('get_nexus_infra_api_certmanagement_v4_trustedcas')
def get_nexus_infra_api_certmanagement_v4_trustedcas(AuthCookie: str = None, Cookie: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_certmanagement_v4_trustedcas

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_certmanagement_v4_trustedca')(globals()['get_nexus_infra_api_certmanagement_v4_trustedcas'])

# alias → easier for LLM
register('nexus_infra_api_certmanagement_v4_trustedcas')(globals()['get_nexus_infra_api_certmanagement_v4_trustedcas'])

@register('nexus_infra_api_certmanagement_v4_trustedca')
def nexus_infra_api_certmanagement_v4_trustedca(AuthCookie: str = None, Cookie: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_certmanagement_v4_trustedca

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_certmanagement_v4_trustedca')(globals()['nexus_infra_api_certmanagement_v4_trustedca'])

@register('nexus_infra_api_certmanagement_v4_trustedcas')
def nexus_infra_api_certmanagement_v4_trustedcas(AuthCookie: str = None, Cookie: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_certmanagement_v4_trustedcas

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_certmanagement_v4_trustedcas')(globals()['nexus_infra_api_certmanagement_v4_trustedcas'])

# alias → easier for LLM
register('infra_api_certmanagement_v4_trustedca')(globals()['nexus_infra_api_certmanagement_v4_trustedcas'])

@register('post_nexus_infra_api_certmanagement_v4_trustedcas')
def post_nexus_infra_api_certmanagement_v4_trustedcas(AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.post_nexus_infra_api_certmanagement_v4_trustedcas

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_certmanagement_v4_trustedca')(globals()['post_nexus_infra_api_certmanagement_v4_trustedcas'])

# alias → easier for LLM
register('nexus_infra_api_certmanagement_v4_trustedcas')(globals()['post_nexus_infra_api_certmanagement_v4_trustedcas'])

@register('delete_nexus_infra_api_certmanagement_v4_trustedcas_specName_')
def delete_nexus_infra_api_certmanagement_v4_trustedcas_specName_(specName: str, AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.delete_nexus_infra_api_certmanagement_v4_trustedcas_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_certmanagement_v4_trustedcas_specName_')(globals()['delete_nexus_infra_api_certmanagement_v4_trustedcas_specName_'])

@register('nexus_infra_api_certmanagement_v4_trustedcas_specName_')
def nexus_infra_api_certmanagement_v4_trustedcas_specName_(specName: str, AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_certmanagement_v4_trustedcas_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_certmanagement_v4_trustedcas_specName_')(globals()['nexus_infra_api_certmanagement_v4_trustedcas_specName_'])

@register('get_nexus_infra_api_certmanagement_v4_trustedcas_specName_')
def get_nexus_infra_api_certmanagement_v4_trustedcas_specName_(specName: str, AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_certmanagement_v4_trustedcas_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_certmanagement_v4_trustedcas_specName_')(globals()['get_nexus_infra_api_certmanagement_v4_trustedcas_specName_'])

@register('put_nexus_infra_api_certmanagement_v4_trustedcas_specName_')
def put_nexus_infra_api_certmanagement_v4_trustedcas_specName_(specName: str, AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.put_nexus_infra_api_certmanagement_v4_trustedcas_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_certmanagement_v4_trustedcas_specName_')(globals()['put_nexus_infra_api_certmanagement_v4_trustedcas_specName_'])

@register('get_nexus_infra_api_credmgr_v4_credentials')
def get_nexus_infra_api_credmgr_v4_credentials(AuthCookie: str = None, Cookie: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_credmgr_v4_credentials

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_credmgr_v4_credential')(globals()['get_nexus_infra_api_credmgr_v4_credentials'])

# alias → easier for LLM
register('nexus_infra_api_credmgr_v4_credentials')(globals()['get_nexus_infra_api_credmgr_v4_credentials'])

@register('nexus_infra_api_credmgr_v4_credential')
def nexus_infra_api_credmgr_v4_credential(AuthCookie: str = None, Cookie: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_credmgr_v4_credential

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_credmgr_v4_credential')(globals()['nexus_infra_api_credmgr_v4_credential'])

@register('nexus_infra_api_credmgr_v4_credentials')
def nexus_infra_api_credmgr_v4_credentials(AuthCookie: str = None, Cookie: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_credmgr_v4_credentials

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_credmgr_v4_credentials')(globals()['nexus_infra_api_credmgr_v4_credentials'])

# alias → easier for LLM
register('infra_api_credmgr_v4_credential')(globals()['nexus_infra_api_credmgr_v4_credentials'])

@register('post_nexus_infra_api_credmgr_v4_credentials')
def post_nexus_infra_api_credmgr_v4_credentials(AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.post_nexus_infra_api_credmgr_v4_credentials

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_credmgr_v4_credential')(globals()['post_nexus_infra_api_credmgr_v4_credentials'])

# alias → easier for LLM
register('nexus_infra_api_credmgr_v4_credentials')(globals()['post_nexus_infra_api_credmgr_v4_credentials'])

@register('delete_nexus_infra_api_credmgr_v4_credentials_specName_')
def delete_nexus_infra_api_credmgr_v4_credentials_specName_(specName: str, AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.delete_nexus_infra_api_credmgr_v4_credentials_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_credmgr_v4_credentials_specName_')(globals()['delete_nexus_infra_api_credmgr_v4_credentials_specName_'])

@register('nexus_infra_api_credmgr_v4_credentials_specName_')
def nexus_infra_api_credmgr_v4_credentials_specName_(specName: str, AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_credmgr_v4_credentials_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_credmgr_v4_credentials_specName_')(globals()['nexus_infra_api_credmgr_v4_credentials_specName_'])

@register('get_nexus_infra_api_credmgr_v4_credentials_specName_')
def get_nexus_infra_api_credmgr_v4_credentials_specName_(specName: str, showCredential: str = None, AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if showCredential is not None:
        final_kwargs['showCredential'] = showCredential
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_credmgr_v4_credentials_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_credmgr_v4_credentials_specName_')(globals()['get_nexus_infra_api_credmgr_v4_credentials_specName_'])

@register('patch_nexus_infra_api_credmgr_v4_credentials_specName_')
def patch_nexus_infra_api_credmgr_v4_credentials_specName_(specName: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.patch_nexus_infra_api_credmgr_v4_credentials_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_credmgr_v4_credentials_specName_')(globals()['patch_nexus_infra_api_credmgr_v4_credentials_specName_'])

@register('put_nexus_infra_api_credmgr_v4_credentials_specName_')
def put_nexus_infra_api_credmgr_v4_credentials_specName_(specName: str, AuthCookie: str = None, Cookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie
    if Cookie is not None:
        final_kwargs['Cookie'] = Cookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.put_nexus_infra_api_credmgr_v4_credentials_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_credmgr_v4_credentials_specName_')(globals()['put_nexus_infra_api_credmgr_v4_credentials_specName_'])

@register('get_nexus_infra_api_eventmonitoring_v1_eventconfigs')
def get_nexus_infra_api_eventmonitoring_v1_eventconfigs(X_Nd_Rbac: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_eventmonitoring_v1_eventconfigs

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_eventmonitoring_v1_eventconfig')(globals()['get_nexus_infra_api_eventmonitoring_v1_eventconfigs'])

# alias → easier for LLM
register('nexus_infra_api_eventmonitoring_v1_eventconfigs')(globals()['get_nexus_infra_api_eventmonitoring_v1_eventconfigs'])

@register('nexus_infra_api_eventmonitoring_v1_eventconfig')
def nexus_infra_api_eventmonitoring_v1_eventconfig(X_Nd_Rbac: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_eventmonitoring_v1_eventconfig

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_eventmonitoring_v1_eventconfig')(globals()['nexus_infra_api_eventmonitoring_v1_eventconfig'])

@register('nexus_infra_api_eventmonitoring_v1_eventconfigs')
def nexus_infra_api_eventmonitoring_v1_eventconfigs(X_Nd_Rbac: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_eventmonitoring_v1_eventconfigs

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_eventmonitoring_v1_eventconfigs')(globals()['nexus_infra_api_eventmonitoring_v1_eventconfigs'])

# alias → easier for LLM
register('infra_api_eventmonitoring_v1_eventconfig')(globals()['nexus_infra_api_eventmonitoring_v1_eventconfigs'])

@register('get_nexus_infra_api_eventmonitoring_v1_eventrecords')
def get_nexus_infra_api_eventmonitoring_v1_eventrecords(X_Nd_Rbac: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_eventmonitoring_v1_eventrecords

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_eventmonitoring_v1_eventrecord')(globals()['get_nexus_infra_api_eventmonitoring_v1_eventrecords'])

# alias → easier for LLM
register('nexus_infra_api_eventmonitoring_v1_eventrecords')(globals()['get_nexus_infra_api_eventmonitoring_v1_eventrecords'])

@register('nexus_infra_api_eventmonitoring_v1_eventrecord')
def nexus_infra_api_eventmonitoring_v1_eventrecord(X_Nd_Rbac: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_eventmonitoring_v1_eventrecord

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_eventmonitoring_v1_eventrecord')(globals()['nexus_infra_api_eventmonitoring_v1_eventrecord'])

@register('nexus_infra_api_eventmonitoring_v1_eventrecords')
def nexus_infra_api_eventmonitoring_v1_eventrecords(X_Nd_Rbac: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_eventmonitoring_v1_eventrecords

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_eventmonitoring_v1_eventrecord')(globals()['nexus_infra_api_eventmonitoring_v1_eventrecords'])

# alias → easier for LLM
register('infra_api_eventmonitoring_v1_eventrecords')(globals()['nexus_infra_api_eventmonitoring_v1_eventrecords'])

@register('get_nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even')
def get_nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even(namespace: str, X_Nd_Rbac: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if namespace is not None:
        final_kwargs['namespace'] = namespace
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even')(globals()['get_nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even'])

@register('nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even')
def nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even(namespace: str, X_Nd_Rbac: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if namespace is not None:
        final_kwargs['namespace'] = namespace
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_eventmonitoring_v1_namespaces_namespace_even')(globals()['nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even'])

@register('get_nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even')
def get_nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even_1(namespace: str, specId: str, X_Nd_Rbac: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if namespace is not None:
        final_kwargs['namespace'] = namespace
    if specId is not None:
        final_kwargs['specId'] = specId
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even_1

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even')(globals()['get_nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even_1'])

@register('get_nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even')
def get_nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even_2(namespace: str, X_Nd_Rbac: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if namespace is not None:
        final_kwargs['namespace'] = namespace
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even_2

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even')(globals()['get_nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even_2'])

@register('get_nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even')
def get_nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even_3(namespace: str, specMetaName: str, X_Nd_Rbac: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if namespace is not None:
        final_kwargs['namespace'] = namespace
    if specMetaName is not None:
        final_kwargs['specMetaName'] = specMetaName
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even_3

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even')(globals()['get_nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even_3'])

@register('put_nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even')
def put_nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even(namespace: str, specMetaName: str, X_Nd_Rbac: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if namespace is not None:
        final_kwargs['namespace'] = namespace
    if specMetaName is not None:
        final_kwargs['specMetaName'] = specMetaName
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.put_nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even')(globals()['put_nexus_infra_api_eventmonitoring_v1_namespaces_namespace_even'])

@register('get_nexus_infra_api_platform_v1_clusters')
def get_nexus_infra_api_platform_v1_clusters(X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_platform_v1_clusters

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_clusters')(globals()['get_nexus_infra_api_platform_v1_clusters'])

# alias → easier for LLM
register('nexus_infra_api_platform_v1_cluster')(globals()['get_nexus_infra_api_platform_v1_clusters'])

@register('nexus_infra_api_platform_v1_clusters')
def nexus_infra_api_platform_v1_clusters(X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_platform_v1_clusters

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_platform_v1_clusters')(globals()['nexus_infra_api_platform_v1_clusters'])

# alias → easier for LLM
register('infra_api_platform_v1_cluster')(globals()['nexus_infra_api_platform_v1_clusters'])

@register('nexus_infra_api_platform_v1_cluster')
def nexus_infra_api_platform_v1_cluster(X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_platform_v1_cluster

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_platform_v1_cluster')(globals()['nexus_infra_api_platform_v1_cluster'])

@register('get_nexus_infra_api_platform_v1_clusters_specName_')
def get_nexus_infra_api_platform_v1_clusters_specName_(specName: str, X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_platform_v1_clusters_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_clusters_specName_')(globals()['get_nexus_infra_api_platform_v1_clusters_specName_'])

@register('nexus_infra_api_platform_v1_clusters_specName_')
def nexus_infra_api_platform_v1_clusters_specName_(specName: str, X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_platform_v1_clusters_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_platform_v1_clusters_specName_')(globals()['nexus_infra_api_platform_v1_clusters_specName_'])

@register('put_nexus_infra_api_platform_v1_clusters_specName_')
def put_nexus_infra_api_platform_v1_clusters_specName_(specName: str, X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.put_nexus_infra_api_platform_v1_clusters_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_clusters_specName_')(globals()['put_nexus_infra_api_platform_v1_clusters_specName_'])

@register('get_nexus_infra_api_platform_v1_externalips')
def get_nexus_infra_api_platform_v1_externalips(X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_platform_v1_externalips

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_externalip')(globals()['get_nexus_infra_api_platform_v1_externalips'])

# alias → easier for LLM
register('nexus_infra_api_platform_v1_externalips')(globals()['get_nexus_infra_api_platform_v1_externalips'])

@register('nexus_infra_api_platform_v1_externalip')
def nexus_infra_api_platform_v1_externalip(X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_platform_v1_externalip

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_platform_v1_externalip')(globals()['nexus_infra_api_platform_v1_externalip'])

@register('nexus_infra_api_platform_v1_externalips')
def nexus_infra_api_platform_v1_externalips(X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_platform_v1_externalips

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_platform_v1_externalips')(globals()['nexus_infra_api_platform_v1_externalips'])

# alias → easier for LLM
register('infra_api_platform_v1_externalip')(globals()['nexus_infra_api_platform_v1_externalips'])

@register('post_nexus_infra_api_platform_v1_externalips')
def post_nexus_infra_api_platform_v1_externalips(X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.post_nexus_infra_api_platform_v1_externalips

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_externalip')(globals()['post_nexus_infra_api_platform_v1_externalips'])

# alias → easier for LLM
register('nexus_infra_api_platform_v1_externalips')(globals()['post_nexus_infra_api_platform_v1_externalips'])

@register('get_nexus_infra_api_platform_v1_externalips_specName_')
def get_nexus_infra_api_platform_v1_externalips_specName_(specName: str, X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_platform_v1_externalips_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_externalips_specName_')(globals()['get_nexus_infra_api_platform_v1_externalips_specName_'])

@register('nexus_infra_api_platform_v1_externalips_specName_')
def nexus_infra_api_platform_v1_externalips_specName_(specName: str, X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_platform_v1_externalips_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_platform_v1_externalips_specName_')(globals()['nexus_infra_api_platform_v1_externalips_specName_'])

@register('put_nexus_infra_api_platform_v1_externalips_specName_')
def put_nexus_infra_api_platform_v1_externalips_specName_(specName: str, X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.put_nexus_infra_api_platform_v1_externalips_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_externalips_specName_')(globals()['put_nexus_infra_api_platform_v1_externalips_specName_'])

@register('get_nexus_infra_api_platform_v1_networkstorages')
def get_nexus_infra_api_platform_v1_networkstorages(X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_platform_v1_networkstorages

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_networkstorages')(globals()['get_nexus_infra_api_platform_v1_networkstorages'])

# alias → easier for LLM
register('nexus_infra_api_platform_v1_networkstorage')(globals()['get_nexus_infra_api_platform_v1_networkstorages'])

@register('nexus_infra_api_platform_v1_networkstorages')
def nexus_infra_api_platform_v1_networkstorages(X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_platform_v1_networkstorages

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_platform_v1_networkstorages')(globals()['nexus_infra_api_platform_v1_networkstorages'])

# alias → easier for LLM
register('infra_api_platform_v1_networkstorage')(globals()['nexus_infra_api_platform_v1_networkstorages'])

@register('nexus_infra_api_platform_v1_networkstorage')
def nexus_infra_api_platform_v1_networkstorage(X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_platform_v1_networkstorage

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_platform_v1_networkstorage')(globals()['nexus_infra_api_platform_v1_networkstorage'])

@register('post_nexus_infra_api_platform_v1_networkstorages')
def post_nexus_infra_api_platform_v1_networkstorages(X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.post_nexus_infra_api_platform_v1_networkstorages

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_networkstorages')(globals()['post_nexus_infra_api_platform_v1_networkstorages'])

# alias → easier for LLM
register('nexus_infra_api_platform_v1_networkstorage')(globals()['post_nexus_infra_api_platform_v1_networkstorages'])

@register('delete_nexus_infra_api_platform_v1_networkstorages_specName_')
def delete_nexus_infra_api_platform_v1_networkstorages_specName_(specName: str, X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.delete_nexus_infra_api_platform_v1_networkstorages_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_networkstorages_specName_')(globals()['delete_nexus_infra_api_platform_v1_networkstorages_specName_'])

@register('nexus_infra_api_platform_v1_networkstorages_specName_')
def nexus_infra_api_platform_v1_networkstorages_specName_(specName: str, X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_platform_v1_networkstorages_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_platform_v1_networkstorages_specName_')(globals()['nexus_infra_api_platform_v1_networkstorages_specName_'])

@register('get_nexus_infra_api_platform_v1_networkstorages_specName_')
def get_nexus_infra_api_platform_v1_networkstorages_specName_(specName: str, X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_platform_v1_networkstorages_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_networkstorages_specName_')(globals()['get_nexus_infra_api_platform_v1_networkstorages_specName_'])

@register('put_nexus_infra_api_platform_v1_networkstorages_specName_')
def put_nexus_infra_api_platform_v1_networkstorages_specName_(specName: str, X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.put_nexus_infra_api_platform_v1_networkstorages_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_networkstorages_specName_')(globals()['put_nexus_infra_api_platform_v1_networkstorages_specName_'])

@register('get_nexus_infra_api_platform_v1_nodes')
def get_nexus_infra_api_platform_v1_nodes(X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_platform_v1_nodes

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_node')(globals()['get_nexus_infra_api_platform_v1_nodes'])

# alias → easier for LLM
register('nexus_infra_api_platform_v1_nodes')(globals()['get_nexus_infra_api_platform_v1_nodes'])

@register('nexus_infra_api_platform_v1_node')
def nexus_infra_api_platform_v1_node(X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_platform_v1_node

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_platform_v1_node')(globals()['nexus_infra_api_platform_v1_node'])

@register('nexus_infra_api_platform_v1_nodes')
def nexus_infra_api_platform_v1_nodes(X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_platform_v1_nodes

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_platform_v1_nodes')(globals()['nexus_infra_api_platform_v1_nodes'])

# alias → easier for LLM
register('infra_api_platform_v1_node')(globals()['nexus_infra_api_platform_v1_nodes'])

@register('delete_nexus_infra_api_platform_v1_nodes_specName_')
def delete_nexus_infra_api_platform_v1_nodes_specName_(specName: str, X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.delete_nexus_infra_api_platform_v1_nodes_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_nodes_specName_')(globals()['delete_nexus_infra_api_platform_v1_nodes_specName_'])

@register('nexus_infra_api_platform_v1_nodes_specName_')
def nexus_infra_api_platform_v1_nodes_specName_(specName: str, X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_platform_v1_nodes_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_platform_v1_nodes_specName_')(globals()['nexus_infra_api_platform_v1_nodes_specName_'])

@register('get_nexus_infra_api_platform_v1_nodes_specName_')
def get_nexus_infra_api_platform_v1_nodes_specName_(specName: str, X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_platform_v1_nodes_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_nodes_specName_')(globals()['get_nexus_infra_api_platform_v1_nodes_specName_'])

@register('put_nexus_infra_api_platform_v1_nodes_specName_')
def put_nexus_infra_api_platform_v1_nodes_specName_(specName: str, X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.put_nexus_infra_api_platform_v1_nodes_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_nodes_specName_')(globals()['put_nexus_infra_api_platform_v1_nodes_specName_'])

@register('get_nexus_infra_api_platform_v1_routes')
def get_nexus_infra_api_platform_v1_routes(X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_platform_v1_routes

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_route')(globals()['get_nexus_infra_api_platform_v1_routes'])

# alias → easier for LLM
register('nexus_infra_api_platform_v1_routes')(globals()['get_nexus_infra_api_platform_v1_routes'])

@register('nexus_infra_api_platform_v1_route')
def nexus_infra_api_platform_v1_route(X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_platform_v1_route

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_platform_v1_route')(globals()['nexus_infra_api_platform_v1_route'])

@register('nexus_infra_api_platform_v1_routes')
def nexus_infra_api_platform_v1_routes(X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_platform_v1_routes

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_platform_v1_routes')(globals()['nexus_infra_api_platform_v1_routes'])

# alias → easier for LLM
register('infra_api_platform_v1_route')(globals()['nexus_infra_api_platform_v1_routes'])

@register('post_nexus_infra_api_platform_v1_routes')
def post_nexus_infra_api_platform_v1_routes(X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.post_nexus_infra_api_platform_v1_routes

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_route')(globals()['post_nexus_infra_api_platform_v1_routes'])

# alias → easier for LLM
register('nexus_infra_api_platform_v1_routes')(globals()['post_nexus_infra_api_platform_v1_routes'])

@register('delete_nexus_infra_api_platform_v1_routes_specDestination_')
def delete_nexus_infra_api_platform_v1_routes_specDestination_(specDestination: str, X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specDestination is not None:
        final_kwargs['specDestination'] = specDestination
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.delete_nexus_infra_api_platform_v1_routes_specDestination_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_routes_specDestination_')(globals()['delete_nexus_infra_api_platform_v1_routes_specDestination_'])

@register('nexus_infra_api_platform_v1_routes_specDestination_')
def nexus_infra_api_platform_v1_routes_specDestination_(specDestination: str, X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specDestination is not None:
        final_kwargs['specDestination'] = specDestination
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_platform_v1_routes_specDestination_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_platform_v1_routes_specDestination_')(globals()['nexus_infra_api_platform_v1_routes_specDestination_'])

@register('get_nexus_infra_api_platform_v1_routes_specDestination_')
def get_nexus_infra_api_platform_v1_routes_specDestination_(specDestination: str, X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specDestination is not None:
        final_kwargs['specDestination'] = specDestination
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_platform_v1_routes_specDestination_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_routes_specDestination_')(globals()['get_nexus_infra_api_platform_v1_routes_specDestination_'])

@register('put_nexus_infra_api_platform_v1_routes_specDestination_')
def put_nexus_infra_api_platform_v1_routes_specDestination_(specDestination: str, X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specDestination is not None:
        final_kwargs['specDestination'] = specDestination
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.put_nexus_infra_api_platform_v1_routes_specDestination_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_routes_specDestination_')(globals()['put_nexus_infra_api_platform_v1_routes_specDestination_'])

@register('get_nexus_infra_api_platform_v1_syslogsyncs')
def get_nexus_infra_api_platform_v1_syslogsyncs(X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_platform_v1_syslogsyncs

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_syslogsync')(globals()['get_nexus_infra_api_platform_v1_syslogsyncs'])

# alias → easier for LLM
register('nexus_infra_api_platform_v1_syslogsyncs')(globals()['get_nexus_infra_api_platform_v1_syslogsyncs'])

@register('nexus_infra_api_platform_v1_syslogsync')
def nexus_infra_api_platform_v1_syslogsync(X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_platform_v1_syslogsync

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_platform_v1_syslogsync')(globals()['nexus_infra_api_platform_v1_syslogsync'])

@register('nexus_infra_api_platform_v1_syslogsyncs')
def nexus_infra_api_platform_v1_syslogsyncs(X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_platform_v1_syslogsyncs

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_platform_v1_syslogsync')(globals()['nexus_infra_api_platform_v1_syslogsyncs'])

# alias → easier for LLM
register('infra_api_platform_v1_syslogsyncs')(globals()['nexus_infra_api_platform_v1_syslogsyncs'])

@register('post_nexus_infra_api_platform_v1_syslogsyncs')
def post_nexus_infra_api_platform_v1_syslogsyncs(X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.post_nexus_infra_api_platform_v1_syslogsyncs

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_syslogsync')(globals()['post_nexus_infra_api_platform_v1_syslogsyncs'])

# alias → easier for LLM
register('nexus_infra_api_platform_v1_syslogsyncs')(globals()['post_nexus_infra_api_platform_v1_syslogsyncs'])

@register('delete_nexus_infra_api_platform_v1_syslogsyncs_specAddress_')
def delete_nexus_infra_api_platform_v1_syslogsyncs_specAddress_(specAddress: str, X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specAddress is not None:
        final_kwargs['specAddress'] = specAddress
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.delete_nexus_infra_api_platform_v1_syslogsyncs_specAddress_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_syslogsyncs_specAddress_')(globals()['delete_nexus_infra_api_platform_v1_syslogsyncs_specAddress_'])

@register('nexus_infra_api_platform_v1_syslogsyncs_specAddress_')
def nexus_infra_api_platform_v1_syslogsyncs_specAddress_(specAddress: str, X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specAddress is not None:
        final_kwargs['specAddress'] = specAddress
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_platform_v1_syslogsyncs_specAddress_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_platform_v1_syslogsyncs_specAddress_')(globals()['nexus_infra_api_platform_v1_syslogsyncs_specAddress_'])

@register('get_nexus_infra_api_platform_v1_syslogsyncs_specAddress_')
def get_nexus_infra_api_platform_v1_syslogsyncs_specAddress_(specAddress: str, X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specAddress is not None:
        final_kwargs['specAddress'] = specAddress
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_platform_v1_syslogsyncs_specAddress_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_syslogsyncs_specAddress_')(globals()['get_nexus_infra_api_platform_v1_syslogsyncs_specAddress_'])

@register('put_nexus_infra_api_platform_v1_syslogsyncs_specAddress_')
def put_nexus_infra_api_platform_v1_syslogsyncs_specAddress_(specAddress: str, X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specAddress is not None:
        final_kwargs['specAddress'] = specAddress
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.put_nexus_infra_api_platform_v1_syslogsyncs_specAddress_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v1_syslogsyncs_specAddress_')(globals()['put_nexus_infra_api_platform_v1_syslogsyncs_specAddress_'])

@register('get_nexus_infra_api_platform_v2_clusters')
def get_nexus_infra_api_platform_v2_clusters(X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_platform_v2_clusters

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v2_cluster')(globals()['get_nexus_infra_api_platform_v2_clusters'])

# alias → easier for LLM
register('nexus_infra_api_platform_v2_clusters')(globals()['get_nexus_infra_api_platform_v2_clusters'])

@register('nexus_infra_api_platform_v2_cluster')
def nexus_infra_api_platform_v2_cluster(X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_platform_v2_cluster

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_platform_v2_cluster')(globals()['nexus_infra_api_platform_v2_cluster'])

@register('nexus_infra_api_platform_v2_clusters')
def nexus_infra_api_platform_v2_clusters(X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None, filter: str = None, orderBy: str = None, inc: str = None, pageSize: str = None, previousPage: str = None, offset: str = None, lastReported: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair
    if filter is not None:
        final_kwargs['filter'] = filter
    if orderBy is not None:
        final_kwargs['orderBy'] = orderBy
    if inc is not None:
        final_kwargs['inc'] = inc
    if pageSize is not None:
        final_kwargs['pageSize'] = pageSize
    if previousPage is not None:
        final_kwargs['previousPage'] = previousPage
    if offset is not None:
        final_kwargs['offset'] = offset
    if lastReported is not None:
        final_kwargs['lastReported'] = lastReported

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_platform_v2_clusters

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_platform_v2_cluster')(globals()['nexus_infra_api_platform_v2_clusters'])

# alias → easier for LLM
register('infra_api_platform_v2_clusters')(globals()['nexus_infra_api_platform_v2_clusters'])

@register('get_nexus_infra_api_platform_v2_clusters_specName_')
def get_nexus_infra_api_platform_v2_clusters_specName_(specName: str, X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_nexus_infra_api_platform_v2_clusters_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v2_clusters_specName_')(globals()['get_nexus_infra_api_platform_v2_clusters_specName_'])

@register('nexus_infra_api_platform_v2_clusters_specName_')
def nexus_infra_api_platform_v2_clusters_specName_(specName: str, X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nexus_infra_api_platform_v2_clusters_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('infra_api_platform_v2_clusters_specName_')(globals()['nexus_infra_api_platform_v2_clusters_specName_'])

@register('put_nexus_infra_api_platform_v2_clusters_specName_')
def put_nexus_infra_api_platform_v2_clusters_specName_(specName: str, X_Nd_Rbac: str = None, X_Aci_Username: str = None, X_Aci_Sessionid: str = None, X_Aci_Usertype: str = None, X_Nd_UILogin: str = None, X_Aci_Avpair: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if specName is not None:
        final_kwargs['specName'] = specName
    if X_Nd_Rbac is not None:
        final_kwargs['X-Nd-Rbac'] = X_Nd_Rbac
    if X_Aci_Username is not None:
        final_kwargs['X-Aci-Username'] = X_Aci_Username
    if X_Aci_Sessionid is not None:
        final_kwargs['X-Aci-Sessionid'] = X_Aci_Sessionid
    if X_Aci_Usertype is not None:
        final_kwargs['X-Aci-Usertype'] = X_Aci_Usertype
    if X_Nd_UILogin is not None:
        final_kwargs['X-Nd-UILogin'] = X_Nd_UILogin
    if X_Aci_Avpair is not None:
        final_kwargs['X-Aci-Avpair'] = X_Aci_Avpair

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.put_nexus_infra_api_platform_v2_clusters_specName_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('nexus_infra_api_platform_v2_clusters_specName_')(globals()['put_nexus_infra_api_platform_v2_clusters_specName_'])

@register('post_refresh')
def post_refresh(AuthCookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.post_refresh

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('refresh')(globals()['post_refresh'])

@register('refresh')
def refresh(AuthCookie: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if AuthCookie is not None:
        final_kwargs['AuthCookie'] = AuthCookie

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.refresh

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('get_api_action_class_backuprestore_status')
def get_api_action_class_backuprestore_status():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_api_action_class_backuprestore_status

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_action_class_backuprestore_status')(globals()['get_api_action_class_backuprestore_status'])

# alias → easier for LLM
register('api_action_class_backuprestore_statu')(globals()['get_api_action_class_backuprestore_status'])

@register('api_action_class_backuprestore_status')
def api_action_class_backuprestore_status():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.api_action_class_backuprestore_status

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('action_class_backuprestore_status')(globals()['api_action_class_backuprestore_status'])

# alias → easier for LLM
register('action_class_backuprestore_statu')(globals()['api_action_class_backuprestore_status'])

@register('api_action_class_backuprestore_statu')
def api_action_class_backuprestore_statu():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.api_action_class_backuprestore_statu

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('action_class_backuprestore_statu')(globals()['api_action_class_backuprestore_statu'])

@register('get_api_action_class_backuprestore_backup_name_')
def get_api_action_class_backuprestore_backup_name_(name: str, action: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if name is not None:
        final_kwargs['name'] = name
    if action is not None:
        final_kwargs['action'] = action

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_api_action_class_backuprestore_backup_name_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_action_class_backuprestore_backup_name_')(globals()['get_api_action_class_backuprestore_backup_name_'])

@register('api_action_class_backuprestore_backup_name_')
def api_action_class_backuprestore_backup_name_(name: str, action: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if name is not None:
        final_kwargs['name'] = name
    if action is not None:
        final_kwargs['action'] = action

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.api_action_class_backuprestore_backup_name_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('action_class_backuprestore_backup_name_')(globals()['api_action_class_backuprestore_backup_name_'])

@register('delete_api_action_class_backuprestore_backup_name_')
def delete_api_action_class_backuprestore_backup_name_(name: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.delete_api_action_class_backuprestore_backup_name_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_action_class_backuprestore_backup_name_')(globals()['delete_api_action_class_backuprestore_backup_name_'])

@register('get_api_action_class_backuprestore_backup')
def get_api_action_class_backuprestore_backup():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_api_action_class_backuprestore_backup

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_action_class_backuprestore_backup')(globals()['get_api_action_class_backuprestore_backup'])

@register('api_action_class_backuprestore_backup')
def api_action_class_backuprestore_backup():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.api_action_class_backuprestore_backup

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('action_class_backuprestore_backup')(globals()['api_action_class_backuprestore_backup'])

@register('post_api_action_class_backuprestore_backup')
def post_api_action_class_backuprestore_backup():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.post_api_action_class_backuprestore_backup

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_action_class_backuprestore_backup')(globals()['post_api_action_class_backuprestore_backup'])

@register('get_api_config_class_backuprestore_backup_schedule_name_')
def get_api_config_class_backuprestore_backup_schedule_name_():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_api_config_class_backuprestore_backup_schedule_name_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_config_class_backuprestore_backup_schedule_name_')(globals()['get_api_config_class_backuprestore_backup_schedule_name_'])

@register('api_config_class_backuprestore_backup_schedule_name_')
def api_config_class_backuprestore_backup_schedule_name_():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.api_config_class_backuprestore_backup_schedule_name_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('config_class_backuprestore_backup_schedule_name_')(globals()['api_config_class_backuprestore_backup_schedule_name_'])

@register('put_api_config_class_backuprestore_backup_schedule_name_')
def put_api_config_class_backuprestore_backup_schedule_name_(name: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.put_api_config_class_backuprestore_backup_schedule_name_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_config_class_backuprestore_backup_schedule_name_')(globals()['put_api_config_class_backuprestore_backup_schedule_name_'])

@register('delete_api_config_class_backuprestore_backup_schedule_name_')
def delete_api_config_class_backuprestore_backup_schedule_name_(name: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.delete_api_config_class_backuprestore_backup_schedule_name_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_config_class_backuprestore_backup_schedule_name_')(globals()['delete_api_config_class_backuprestore_backup_schedule_name_'])

@register('get_api_config_class_backuprestore_backup_schedule')
def get_api_config_class_backuprestore_backup_schedule():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_api_config_class_backuprestore_backup_schedule

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_config_class_backuprestore_backup_schedule')(globals()['get_api_config_class_backuprestore_backup_schedule'])

@register('api_config_class_backuprestore_backup_schedule')
def api_config_class_backuprestore_backup_schedule():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.api_config_class_backuprestore_backup_schedule

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('config_class_backuprestore_backup_schedule')(globals()['api_config_class_backuprestore_backup_schedule'])

@register('post_api_config_class_backuprestore_backup_schedule')
def post_api_config_class_backuprestore_backup_schedule():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.post_api_config_class_backuprestore_backup_schedule

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_config_class_backuprestore_backup_schedule')(globals()['post_api_config_class_backuprestore_backup_schedule'])

@register('post_api_action_class_backuprestore_restore_file-import')
def post_api_action_class_backuprestore_restore_file_import():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.post_api_action_class_backuprestore_restore_file_import

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_action_class_backuprestore_restore_file-import')(globals()['post_api_action_class_backuprestore_restore_file_import'])

@register('api_action_class_backuprestore_restore_file-import')
def api_action_class_backuprestore_restore_file_import():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.api_action_class_backuprestore_restore_file_import

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('action_class_backuprestore_restore_file-import')(globals()['api_action_class_backuprestore_restore_file_import'])

@register('delete_api_action_class_backuprestore_restore_file-import')
def delete_api_action_class_backuprestore_restore_file_import():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.delete_api_action_class_backuprestore_restore_file_import

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_action_class_backuprestore_restore_file-import')(globals()['delete_api_action_class_backuprestore_restore_file_import'])

@register('post_api_action_class_backuprestore_restore')
def post_api_action_class_backuprestore_restore():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.post_api_action_class_backuprestore_restore

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_action_class_backuprestore_restore')(globals()['post_api_action_class_backuprestore_restore'])

@register('api_action_class_backuprestore_restore')
def api_action_class_backuprestore_restore():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.api_action_class_backuprestore_restore

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('action_class_backuprestore_restore')(globals()['api_action_class_backuprestore_restore'])

@register('get_api_config_class_securecopystorage')
def get_api_config_class_securecopystorage():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_api_config_class_securecopystorage

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_config_class_securecopystorage')(globals()['get_api_config_class_securecopystorage'])

@register('api_config_class_securecopystorage')
def api_config_class_securecopystorage():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.api_config_class_securecopystorage

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('config_class_securecopystorage')(globals()['api_config_class_securecopystorage'])

@register('post_api_config_class_securecopystorage')
def post_api_config_class_securecopystorage():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.post_api_config_class_securecopystorage

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_config_class_securecopystorage')(globals()['post_api_config_class_securecopystorage'])

@register('get_api_config_class_securecopystorage_name_')
def get_api_config_class_securecopystorage_name_(name: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.get_api_config_class_securecopystorage_name_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_config_class_securecopystorage_name_')(globals()['get_api_config_class_securecopystorage_name_'])

@register('api_config_class_securecopystorage_name_')
def api_config_class_securecopystorage_name_(name: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.api_config_class_securecopystorage_name_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('config_class_securecopystorage_name_')(globals()['api_config_class_securecopystorage_name_'])

@register('put_api_config_class_securecopystorage_name_')
def put_api_config_class_securecopystorage_name_(name: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.put_api_config_class_securecopystorage_name_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_config_class_securecopystorage_name_')(globals()['put_api_config_class_securecopystorage_name_'])

@register('delete_api_config_class_securecopystorage_name_')
def delete_api_config_class_securecopystorage_name_(name: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = Nexus_dashboardClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.delete_api_config_class_securecopystorage_name_

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

# alias → easier for LLM
register('api_config_class_securecopystorage_name_')(globals()['delete_api_config_class_securecopystorage_name_'])
