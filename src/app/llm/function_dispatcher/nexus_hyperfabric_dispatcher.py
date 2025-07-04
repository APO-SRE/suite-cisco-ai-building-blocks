# app/llm/function_dispatcher/nexus_hyperfabric_dispatcher.py
import os
from typing import Any
from app.llm.function_dispatcher import register
from app.llm.platform_clients.nexus_hyperfabric_client import Nexus_hyperfabricClient

@register('authGetBearerTokens')
def authGetBearerTokens(includeMetadata: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'includeMetadata': 'includeMetadata'}.items()
        if locals_[san] is not None
    }

    target = Nexus_hyperfabricClient().__getattr__('authGetBearerTokens')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('authGetBearerToken')
def authGetBearerToken(tokenId: str, includeMetadata: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'tokenId': 'tokenId', 'includeMetadata': 'includeMetadata'}.items()
        if locals_[san] is not None
    }

    target = Nexus_hyperfabricClient().__getattr__('authGetBearerToken')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('devicesGetDevices')
def devicesGetDevices():
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {}.items()
        if locals_[san] is not None
    }

    target = Nexus_hyperfabricClient().__getattr__('devicesGetDevices')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('fabricsGetAllFabrics')
def fabricsGetAllFabrics(fabricId: str = None, candidate: str = None, includeMetadata: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'candidate': 'candidate', 'includeMetadata': 'includeMetadata'}.items()
        if locals_[san] is not None
    }

    target = Nexus_hyperfabricClient().__getattr__('fabricsGetAllFabrics')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('fabricsGetFabric')
def fabricsGetFabric(fabricId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'candidate': 'candidate', 'includeMetadata': 'includeMetadata'}.items()
        if locals_[san] is not None
    }

    target = Nexus_hyperfabricClient().__getattr__('fabricsGetFabric')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('fabricsGetFabricCandidates')
def fabricsGetFabricCandidates(fabricId: str, name: str = None, txnId: int = None, needInactive: bool = None, needReviews: bool = None, needEvents: bool = None, startTime: str = None, endTime: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'name': 'name', 'txnId': 'txnId', 'needInactive': 'needInactive', 'needReviews': 'needReviews', 'needEvents': 'needEvents', 'startTime': 'startTime', 'endTime': 'endTime'}.items()
        if locals_[san] is not None
    }

    target = Nexus_hyperfabricClient().__getattr__('fabricsGetFabricCandidates')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('fabricsGetFabricCandidate')
def fabricsGetFabricCandidate(fabricId: str, name: str, needInactive: bool = None, needReviews: bool = None, needEvents: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'name': 'name', 'needInactive': 'needInactive', 'needReviews': 'needReviews', 'needEvents': 'needEvents'}.items()
        if locals_[san] is not None
    }

    target = Nexus_hyperfabricClient().__getattr__('fabricsGetFabricCandidate')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('fabricsGetFabricConnections')
def fabricsGetFabricConnections(fabricId: str, candidate: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'candidate': 'candidate'}.items()
        if locals_[san] is not None
    }

    target = Nexus_hyperfabricClient().__getattr__('fabricsGetFabricConnections')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('fabricsGetFabricConnection')
def fabricsGetFabricConnection(fabricId: str, connectionId: str, candidate: str = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'connectionId': 'connectionId', 'candidate': 'candidate'}.items()
        if locals_[san] is not None
    }

    target = Nexus_hyperfabricClient().__getattr__('fabricsGetFabricConnection')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('nodesGetFabricNodes')
def nodesGetFabricNodes(fabricId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'candidate': 'candidate', 'includeMetadata': 'includeMetadata'}.items()
        if locals_[san] is not None
    }

    target = Nexus_hyperfabricClient().__getattr__('nodesGetFabricNodes')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('nodesGetNamedFabricNode')
def nodesGetNamedFabricNode(fabricId: str, nodeId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'nodeId': 'nodeId', 'candidate': 'candidate', 'includeMetadata': 'includeMetadata'}.items()
        if locals_[san] is not None
    }

    target = Nexus_hyperfabricClient().__getattr__('nodesGetNamedFabricNode')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('nodesGetManagementPorts')
def nodesGetManagementPorts(fabricId: str, nodeId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'nodeId': 'nodeId', 'candidate': 'candidate', 'includeMetadata': 'includeMetadata'}.items()
        if locals_[san] is not None
    }

    target = Nexus_hyperfabricClient().__getattr__('nodesGetManagementPorts')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('nodesGetManagementPort')
def nodesGetManagementPort(fabricId: str, nodeId: str, id: str, candidate: str = None, includeMetadata: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'nodeId': 'nodeId', 'id': 'id', 'candidate': 'candidate', 'includeMetadata': 'includeMetadata'}.items()
        if locals_[san] is not None
    }

    target = Nexus_hyperfabricClient().__getattr__('nodesGetManagementPort')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('nodesGetPorts')
def nodesGetPorts(fabricId: str, nodeId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'nodeId': 'nodeId', 'candidate': 'candidate', 'includeMetadata': 'includeMetadata'}.items()
        if locals_[san] is not None
    }

    target = Nexus_hyperfabricClient().__getattr__('nodesGetPorts')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('nodesGetPort')
def nodesGetPort(fabricId: str, nodeId: str, portId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'nodeId': 'nodeId', 'portId': 'portId', 'candidate': 'candidate', 'includeMetadata': 'includeMetadata'}.items()
        if locals_[san] is not None
    }

    target = Nexus_hyperfabricClient().__getattr__('nodesGetPort')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vnisGetFabricVnis')
def vnisGetFabricVnis(fabricId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'candidate': 'candidate', 'includeMetadata': 'includeMetadata'}.items()
        if locals_[san] is not None
    }

    target = Nexus_hyperfabricClient().__getattr__('vnisGetFabricVnis')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vnisGetFabricVni')
def vnisGetFabricVni(fabricId: str, vniId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'vniId': 'vniId', 'candidate': 'candidate', 'includeMetadata': 'includeMetadata'}.items()
        if locals_[san] is not None
    }

    target = Nexus_hyperfabricClient().__getattr__('vnisGetFabricVni')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vnisGetFabricVniMembers')
def vnisGetFabricVniMembers(fabricId: str, vniId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'vniId': 'vniId', 'candidate': 'candidate', 'includeMetadata': 'includeMetadata'}.items()
        if locals_[san] is not None
    }

    target = Nexus_hyperfabricClient().__getattr__('vnisGetFabricVniMembers')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vnisGetFabricVniMember')
def vnisGetFabricVniMember(fabricId: str, vniId: str, memberId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'vniId': 'vniId', 'memberId': 'memberId', 'candidate': 'candidate', 'includeMetadata': 'includeMetadata'}.items()
        if locals_[san] is not None
    }

    target = Nexus_hyperfabricClient().__getattr__('vnisGetFabricVniMember')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vrfsGetFabricVrfs')
def vrfsGetFabricVrfs(fabricId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'candidate': 'candidate', 'includeMetadata': 'includeMetadata'}.items()
        if locals_[san] is not None
    }

    target = Nexus_hyperfabricClient().__getattr__('vrfsGetFabricVrfs')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vrfsGetFabricVrf')
def vrfsGetFabricVrf(fabricId: str, vrfId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'vrfId': 'vrfId', 'candidate': 'candidate', 'includeMetadata': 'includeMetadata'}.items()
        if locals_[san] is not None
    }

    target = Nexus_hyperfabricClient().__getattr__('vrfsGetFabricVrf')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vrfsGetFabricStaticRoutes')
def vrfsGetFabricStaticRoutes(fabricId: str, vrfId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'vrfId': 'vrfId', 'candidate': 'candidate', 'includeMetadata': 'includeMetadata'}.items()
        if locals_[san] is not None
    }

    target = Nexus_hyperfabricClient().__getattr__('vrfsGetFabricStaticRoutes')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('vrfsGetFabricStaticRoute')
def vrfsGetFabricStaticRoute(fabricId: str, vrfId: str, routeId: str, candidate: str = None, includeMetadata: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'fabricId': 'fabricId', 'vrfId': 'vrfId', 'routeId': 'routeId', 'candidate': 'candidate', 'includeMetadata': 'includeMetadata'}.items()
        if locals_[san] is not None
    }

    target = Nexus_hyperfabricClient().__getattr__('vrfsGetFabricStaticRoute')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('authGetUsers')
def authGetUsers(emails: str = None, enabled: bool = None, roles: str = None, includeMetadata: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'emails': 'emails', 'enabled': 'enabled', 'roles': 'roles', 'includeMetadata': 'includeMetadata'}.items()
        if locals_[san] is not None
    }

    target = Nexus_hyperfabricClient().__getattr__('authGetUsers')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)

@register('authGetUser')
def authGetUser(userId: str, includeMetadata: bool = None):
    """Auto‑generated wrapper (org‑ID injection included)."""
    locals_ = locals()
    body_payload = locals_.pop('body', None) if 'body' in locals_ else None
    final_kwargs = {
        orig: locals_[san]
        for orig, san in {'userId': 'userId', 'includeMetadata': 'includeMetadata'}.items()
        if locals_[san] is not None
    }

    target = Nexus_hyperfabricClient().__getattr__('authGetUser')
    if body_payload is not None:
        return target(body=body_payload, **final_kwargs)
    return target(**final_kwargs)
