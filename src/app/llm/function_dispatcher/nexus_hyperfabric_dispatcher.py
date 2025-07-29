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
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.authGetBearerTokens

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('authCreateBearerTokens')
def authCreateBearerTokens():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.authCreateBearerTokens

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('authDeleteBearerToken')
def authDeleteBearerToken(tokenId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if tokenId is not None:
        final_kwargs['tokenId'] = tokenId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.authDeleteBearerToken

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
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.authGetBearerToken

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
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.devicesGetDevices

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
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.fabricsGetAllFabrics

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('fabricsAddFabrics')
def fabricsAddFabrics():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.fabricsAddFabrics

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('fabricsDeleteFabric')
def fabricsDeleteFabric(fabricId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.fabricsDeleteFabric

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
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.fabricsGetFabric

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('fabricsUpdateFabric')
def fabricsUpdateFabric(fabricId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.fabricsUpdateFabric

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
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.fabricsGetFabricCandidates

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('fabricsRevertFabricCandidate')
def fabricsRevertFabricCandidate(fabricId: str, name: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.fabricsRevertFabricCandidate

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
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.fabricsGetFabricCandidate

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('fabricsCommitFabricCandidate')
def fabricsCommitFabricCandidate(fabricId: str, name: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.fabricsCommitFabricCandidate

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('fabricsReviewFabricCandidate')
def fabricsReviewFabricCandidate(fabricId: str, name: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if name is not None:
        final_kwargs['name'] = name

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.fabricsReviewFabricCandidate

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('fabricsDeleteFabricConnections')
def fabricsDeleteFabricConnections(fabricId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.fabricsDeleteFabricConnections

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
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.fabricsGetFabricConnections

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('fabricsAddFabricConnections')
def fabricsAddFabricConnections(fabricId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.fabricsAddFabricConnections

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('fabricsSetFabricConnections')
def fabricsSetFabricConnections(fabricId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.fabricsSetFabricConnections

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('fabricsDeleteFabricConnection')
def fabricsDeleteFabricConnection(fabricId: str, connectionId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if connectionId is not None:
        final_kwargs['connectionId'] = connectionId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.fabricsDeleteFabricConnection

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
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.fabricsGetFabricConnection

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
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nodesGetFabricNodes

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('nodesAddFabricNodes')
def nodesAddFabricNodes(fabricId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nodesAddFabricNodes

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('nodesDeleteFabricNode')
def nodesDeleteFabricNode(fabricId: str, nodeId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if nodeId is not None:
        final_kwargs['nodeId'] = nodeId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nodesDeleteFabricNode

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
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nodesGetNamedFabricNode

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('nodesUpdateFabricNode')
def nodesUpdateFabricNode(fabricId: str, nodeId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if nodeId is not None:
        final_kwargs['nodeId'] = nodeId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nodesUpdateFabricNode

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('devicesUnbindDevice')
def devicesUnbindDevice(fabricId: str, nodeId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if nodeId is not None:
        final_kwargs['nodeId'] = nodeId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.devicesUnbindDevice

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('devicesBindDevice')
def devicesBindDevice(fabricId: str, nodeId: str, deviceId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if nodeId is not None:
        final_kwargs['nodeId'] = nodeId
    if deviceId is not None:
        final_kwargs['deviceId'] = deviceId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.devicesBindDevice

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
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nodesGetManagementPorts

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('nodesAddManagementPorts')
def nodesAddManagementPorts(fabricId: str, nodeId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if nodeId is not None:
        final_kwargs['nodeId'] = nodeId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nodesAddManagementPorts

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
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nodesGetManagementPort

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('nodesUpdateManagementPort')
def nodesUpdateManagementPort(fabricId: str, nodeId: str, id: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if nodeId is not None:
        final_kwargs['nodeId'] = nodeId
    if id is not None:
        final_kwargs['id'] = id

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nodesUpdateManagementPort

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
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nodesGetPorts

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('nodesSetPorts')
def nodesSetPorts(fabricId: str, nodeId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if nodeId is not None:
        final_kwargs['nodeId'] = nodeId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nodesSetPorts

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('nodesResetPort')
def nodesResetPort(fabricId: str, nodeId: str, portId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if nodeId is not None:
        final_kwargs['nodeId'] = nodeId
    if portId is not None:
        final_kwargs['portId'] = portId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nodesResetPort

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
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nodesGetPort

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('nodesUpdatePort')
def nodesUpdatePort(fabricId: str, nodeId: str, portId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if nodeId is not None:
        final_kwargs['nodeId'] = nodeId
    if portId is not None:
        final_kwargs['portId'] = portId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.nodesUpdatePort

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
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.vnisGetFabricVnis

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vnisAddFabricVnis')
def vnisAddFabricVnis(fabricId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.vnisAddFabricVnis

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vnisDeleteFabricVni')
def vnisDeleteFabricVni(fabricId: str, vniId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if vniId is not None:
        final_kwargs['vniId'] = vniId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.vnisDeleteFabricVni

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
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.vnisGetFabricVni

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vnisUpdateFabricVni')
def vnisUpdateFabricVni(fabricId: str, vniId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if vniId is not None:
        final_kwargs['vniId'] = vniId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.vnisUpdateFabricVni

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
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.vnisGetFabricVniMembers

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vnisAddFabricVniMembers')
def vnisAddFabricVniMembers(fabricId: str, vniId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if vniId is not None:
        final_kwargs['vniId'] = vniId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.vnisAddFabricVniMembers

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vnisDeleteFabricVniMember')
def vnisDeleteFabricVniMember(fabricId: str, vniId: str, memberId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if vniId is not None:
        final_kwargs['vniId'] = vniId
    if memberId is not None:
        final_kwargs['memberId'] = memberId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.vnisDeleteFabricVniMember

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
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.vnisGetFabricVniMember

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
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.vrfsGetFabricVrfs

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vrfsAddFabricVrfs')
def vrfsAddFabricVrfs(fabricId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.vrfsAddFabricVrfs

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vrfsDeleteFabricVrf')
def vrfsDeleteFabricVrf(fabricId: str, vrfId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if vrfId is not None:
        final_kwargs['vrfId'] = vrfId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.vrfsDeleteFabricVrf

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
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.vrfsGetFabricVrf

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vrfsUpdateFabricVrf')
def vrfsUpdateFabricVrf(fabricId: str, vrfId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if vrfId is not None:
        final_kwargs['vrfId'] = vrfId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.vrfsUpdateFabricVrf

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
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.vrfsGetFabricStaticRoutes

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vrfsAddFabricStaticRoutes')
def vrfsAddFabricStaticRoutes(fabricId: str, vrfId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if vrfId is not None:
        final_kwargs['vrfId'] = vrfId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.vrfsAddFabricStaticRoutes

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vrfsDeleteFabricStaticRoute')
def vrfsDeleteFabricStaticRoute(fabricId: str, vrfId: str, routeId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if vrfId is not None:
        final_kwargs['vrfId'] = vrfId
    if routeId is not None:
        final_kwargs['routeId'] = routeId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.vrfsDeleteFabricStaticRoute

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
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.vrfsGetFabricStaticRoute

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vrfsUpdateFabricStaticRoute')
def vrfsUpdateFabricStaticRoute(fabricId: str, vrfId: str, routeId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if fabricId is not None:
        final_kwargs['fabricId'] = fabricId
    if vrfId is not None:
        final_kwargs['vrfId'] = vrfId
    if routeId is not None:
        final_kwargs['routeId'] = routeId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.vrfsUpdateFabricStaticRoute

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
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.authGetUsers

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('authSetUsers')
def authSetUsers():
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.authSetUsers

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('authDeleteUser')
def authDeleteUser(userId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if userId is not None:
        final_kwargs['userId'] = userId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.authDeleteUser

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
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.authGetUser

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('authUpdateUser')
def authUpdateUser(userId: str):
    """Auto-generated wrapper for clarity and maintainability."""
    # Explicitly build keyword arguments, excluding None values.
    final_kwargs = {}
    if userId is not None:
        final_kwargs['userId'] = userId

    # No body parameter for this function.
    body_payload = None

    client = Nexus_hyperfabricClient()
    # Use attribute access to trigger __getattr__ for dynamic resolution
    target = client.authUpdateUser

    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)
