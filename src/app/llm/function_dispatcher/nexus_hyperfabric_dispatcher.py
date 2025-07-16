# app/llm/function_dispatcher/nexus_hyperfabric_dispatcher.py
import os
from typing import Any
from app.llm.function_dispatcher import register
from app.llm.platform_clients.nexus_hyperfabric_client import Nexus_hyperfabricClient

@register('authGetBearerTokens')
def authGetBearerTokens(includeMetadata: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if includeMetadata is not None:
        final_kwargs['includeMetadata'] = includeMetadata

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    target = getattr(client, 'authGetBearerTokens')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('authGetBearerToken')
def authGetBearerToken(tokenId: str, includeMetadata: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if tokenId is not None:
        final_kwargs['tokenId'] = tokenId
    if includeMetadata is not None:
        final_kwargs['includeMetadata'] = includeMetadata

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    target = getattr(client, 'authGetBearerToken')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('devicesGetDevices')
def devicesGetDevices():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    target = getattr(client, 'devicesGetDevices')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('fabricsGetAllFabrics')
def fabricsGetAllFabrics(fabricId: str = None, candidate: str = None, includeMetadata: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if candidate is not None:
        final_kwargs['candidate'] = candidate
    if includeMetadata is not None:
        final_kwargs['includeMetadata'] = includeMetadata

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    target = getattr(client, 'fabricsGetAllFabrics')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('fabricsGetFabric')
def fabricsGetFabric(fabricId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if candidate is not None:
        final_kwargs['candidate'] = candidate
    if includeMetadata is not None:
        final_kwargs['includeMetadata'] = includeMetadata

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    target = getattr(client, 'fabricsGetFabric')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('fabricsGetFabricCandidates')
def fabricsGetFabricCandidates(fabricId: str, name: str = None, txnId: int = None, needInactive: bool = None, needReviews: bool = None, needEvents: bool = None, startTime: str = None, endTime: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if name is not None:
        final_kwargs['name'] = name
    if txnId is not None:
        final_kwargs['txnId'] = txnId
    if needInactive is not None:
        final_kwargs['needInactive'] = needInactive
    if needReviews is not None:
        final_kwargs['needReviews'] = needReviews
    if needEvents is not None:
        final_kwargs['needEvents'] = needEvents
    if startTime is not None:
        final_kwargs['startTime'] = startTime
    if endTime is not None:
        final_kwargs['endTime'] = endTime

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    target = getattr(client, 'fabricsGetFabricCandidates')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('fabricsGetFabricCandidate')
def fabricsGetFabricCandidate(fabricId: str, name: str, needInactive: bool = None, needReviews: bool = None, needEvents: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if name is not None:
        final_kwargs['name'] = name
    if needInactive is not None:
        final_kwargs['needInactive'] = needInactive
    if needReviews is not None:
        final_kwargs['needReviews'] = needReviews
    if needEvents is not None:
        final_kwargs['needEvents'] = needEvents

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    target = getattr(client, 'fabricsGetFabricCandidate')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('fabricsGetFabricConnections')
def fabricsGetFabricConnections(fabricId: str, candidate: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if candidate is not None:
        final_kwargs['candidate'] = candidate

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    target = getattr(client, 'fabricsGetFabricConnections')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('fabricsGetFabricConnection')
def fabricsGetFabricConnection(fabricId: str, connectionId: str, candidate: str = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if connectionId is not None:
        final_kwargs['connectionId'] = connectionId
    if candidate is not None:
        final_kwargs['candidate'] = candidate

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    target = getattr(client, 'fabricsGetFabricConnection')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('nodesGetFabricNodes')
def nodesGetFabricNodes(fabricId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if candidate is not None:
        final_kwargs['candidate'] = candidate
    if includeMetadata is not None:
        final_kwargs['includeMetadata'] = includeMetadata

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    target = getattr(client, 'nodesGetFabricNodes')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('nodesGetNamedFabricNode')
def nodesGetNamedFabricNode(fabricId: str, nodeId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if nodeId is not None:
        final_kwargs['nodeId'] = nodeId
    if candidate is not None:
        final_kwargs['candidate'] = candidate
    if includeMetadata is not None:
        final_kwargs['includeMetadata'] = includeMetadata

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    target = getattr(client, 'nodesGetNamedFabricNode')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('nodesGetManagementPorts')
def nodesGetManagementPorts(fabricId: str, nodeId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if nodeId is not None:
        final_kwargs['nodeId'] = nodeId
    if candidate is not None:
        final_kwargs['candidate'] = candidate
    if includeMetadata is not None:
        final_kwargs['includeMetadata'] = includeMetadata

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    target = getattr(client, 'nodesGetManagementPorts')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('nodesGetManagementPort')
def nodesGetManagementPort(fabricId: str, nodeId: str, id: str, candidate: str = None, includeMetadata: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if nodeId is not None:
        final_kwargs['nodeId'] = nodeId
    if id is not None:
        final_kwargs['id'] = id
    if candidate is not None:
        final_kwargs['candidate'] = candidate
    if includeMetadata is not None:
        final_kwargs['includeMetadata'] = includeMetadata

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    target = getattr(client, 'nodesGetManagementPort')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('nodesGetPorts')
def nodesGetPorts(fabricId: str, nodeId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if nodeId is not None:
        final_kwargs['nodeId'] = nodeId
    if candidate is not None:
        final_kwargs['candidate'] = candidate
    if includeMetadata is not None:
        final_kwargs['includeMetadata'] = includeMetadata

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    target = getattr(client, 'nodesGetPorts')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('nodesGetPort')
def nodesGetPort(fabricId: str, nodeId: str, portId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if nodeId is not None:
        final_kwargs['nodeId'] = nodeId
    if portId is not None:
        final_kwargs['portId'] = portId
    if candidate is not None:
        final_kwargs['candidate'] = candidate
    if includeMetadata is not None:
        final_kwargs['includeMetadata'] = includeMetadata

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    target = getattr(client, 'nodesGetPort')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vnisGetFabricVnis')
def vnisGetFabricVnis(fabricId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if candidate is not None:
        final_kwargs['candidate'] = candidate
    if includeMetadata is not None:
        final_kwargs['includeMetadata'] = includeMetadata

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    target = getattr(client, 'vnisGetFabricVnis')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vnisGetFabricVni')
def vnisGetFabricVni(fabricId: str, vniId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if vniId is not None:
        final_kwargs['vniId'] = vniId
    if candidate is not None:
        final_kwargs['candidate'] = candidate
    if includeMetadata is not None:
        final_kwargs['includeMetadata'] = includeMetadata

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    target = getattr(client, 'vnisGetFabricVni')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vnisGetFabricVniMembers')
def vnisGetFabricVniMembers(fabricId: str, vniId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if vniId is not None:
        final_kwargs['vniId'] = vniId
    if candidate is not None:
        final_kwargs['candidate'] = candidate
    if includeMetadata is not None:
        final_kwargs['includeMetadata'] = includeMetadata

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    target = getattr(client, 'vnisGetFabricVniMembers')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vnisGetFabricVniMember')
def vnisGetFabricVniMember(fabricId: str, vniId: str, memberId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if vniId is not None:
        final_kwargs['vniId'] = vniId
    if memberId is not None:
        final_kwargs['memberId'] = memberId
    if candidate is not None:
        final_kwargs['candidate'] = candidate
    if includeMetadata is not None:
        final_kwargs['includeMetadata'] = includeMetadata

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    target = getattr(client, 'vnisGetFabricVniMember')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vrfsGetFabricVrfs')
def vrfsGetFabricVrfs(fabricId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if candidate is not None:
        final_kwargs['candidate'] = candidate
    if includeMetadata is not None:
        final_kwargs['includeMetadata'] = includeMetadata

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    target = getattr(client, 'vrfsGetFabricVrfs')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vrfsGetFabricVrf')
def vrfsGetFabricVrf(fabricId: str, vrfId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if vrfId is not None:
        final_kwargs['vrfId'] = vrfId
    if candidate is not None:
        final_kwargs['candidate'] = candidate
    if includeMetadata is not None:
        final_kwargs['includeMetadata'] = includeMetadata

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    target = getattr(client, 'vrfsGetFabricVrf')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vrfsGetFabricStaticRoutes')
def vrfsGetFabricStaticRoutes(fabricId: str, vrfId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if vrfId is not None:
        final_kwargs['vrfId'] = vrfId
    if candidate is not None:
        final_kwargs['candidate'] = candidate
    if includeMetadata is not None:
        final_kwargs['includeMetadata'] = includeMetadata

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    target = getattr(client, 'vrfsGetFabricStaticRoutes')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vrfsGetFabricStaticRoute')
def vrfsGetFabricStaticRoute(fabricId: str, vrfId: str, routeId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if vrfId is not None:
        final_kwargs['vrfId'] = vrfId
    if routeId is not None:
        final_kwargs['routeId'] = routeId
    if candidate is not None:
        final_kwargs['candidate'] = candidate
    if includeMetadata is not None:
        final_kwargs['includeMetadata'] = includeMetadata

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    target = getattr(client, 'vrfsGetFabricStaticRoute')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('authGetUsers')
def authGetUsers(emails: str = None, enabled: bool = None, roles: str = None, includeMetadata: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if emails is not None:
        final_kwargs['emails'] = emails
    if enabled is not None:
        final_kwargs['enabled'] = enabled
    if roles is not None:
        final_kwargs['roles'] = roles
    if includeMetadata is not None:
        final_kwargs['includeMetadata'] = includeMetadata

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    target = getattr(client, 'authGetUsers')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('authGetUser')
def authGetUser(userId: str, includeMetadata: bool = None):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if userId is not None:
        final_kwargs['userId'] = userId
    if includeMetadata is not None:
        final_kwargs['includeMetadata'] = includeMetadata

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    target = getattr(client, 'authGetUser')

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)
