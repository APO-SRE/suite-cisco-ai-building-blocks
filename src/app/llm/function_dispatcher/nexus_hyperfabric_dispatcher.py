# app/llm/function_dispatcher/nexus_hyperfabric_dispatcher.py
from typing import Any
from app.llm.function_dispatcher import register
from app.llm.platform_clients.nexus_hyperfabric_client import Nexus_hyperfabricClient

@register('authGetBearerTokens')
def authGetBearerTokens(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().authGetBearerTokens(body=body, **kwargs)

@register('authCreateBearerTokens')
def authCreateBearerTokens(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().authCreateBearerTokens(body=body, **kwargs)

@register('authDeleteBearerToken')
def authDeleteBearerToken(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().authDeleteBearerToken(body=body, **kwargs)

@register('authGetBearerToken')
def authGetBearerToken(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().authGetBearerToken(body=body, **kwargs)

@register('devicesGetDevices')
def devicesGetDevices(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().devicesGetDevices(body=body, **kwargs)

@register('fabricsGetAllFabrics')
def fabricsGetAllFabrics(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().fabricsGetAllFabrics(body=body, **kwargs)

@register('fabricsAddFabrics')
def fabricsAddFabrics(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().fabricsAddFabrics(body=body, **kwargs)

@register('fabricsDeleteFabric')
def fabricsDeleteFabric(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().fabricsDeleteFabric(body=body, **kwargs)

@register('fabricsGetFabric')
def fabricsGetFabric(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().fabricsGetFabric(body=body, **kwargs)

@register('fabricsUpdateFabric')
def fabricsUpdateFabric(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().fabricsUpdateFabric(body=body, **kwargs)

@register('fabricsGetFabricCandidates')
def fabricsGetFabricCandidates(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().fabricsGetFabricCandidates(body=body, **kwargs)

@register('fabricsRevertFabricCandidate')
def fabricsRevertFabricCandidate(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().fabricsRevertFabricCandidate(body=body, **kwargs)

@register('fabricsGetFabricCandidate')
def fabricsGetFabricCandidate(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().fabricsGetFabricCandidate(body=body, **kwargs)

@register('fabricsCommitFabricCandidate')
def fabricsCommitFabricCandidate(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().fabricsCommitFabricCandidate(body=body, **kwargs)

@register('fabricsReviewFabricCandidate')
def fabricsReviewFabricCandidate(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().fabricsReviewFabricCandidate(body=body, **kwargs)

@register('fabricsDeleteFabricConnections')
def fabricsDeleteFabricConnections(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().fabricsDeleteFabricConnections(body=body, **kwargs)

@register('fabricsGetFabricConnections')
def fabricsGetFabricConnections(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().fabricsGetFabricConnections(body=body, **kwargs)

@register('fabricsAddFabricConnections')
def fabricsAddFabricConnections(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().fabricsAddFabricConnections(body=body, **kwargs)

@register('fabricsSetFabricConnections')
def fabricsSetFabricConnections(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().fabricsSetFabricConnections(body=body, **kwargs)

@register('fabricsDeleteFabricConnection')
def fabricsDeleteFabricConnection(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().fabricsDeleteFabricConnection(body=body, **kwargs)

@register('fabricsGetFabricConnection')
def fabricsGetFabricConnection(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().fabricsGetFabricConnection(body=body, **kwargs)

@register('nodesGetFabricNodes')
def nodesGetFabricNodes(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().nodesGetFabricNodes(body=body, **kwargs)

@register('nodesAddFabricNodes')
def nodesAddFabricNodes(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().nodesAddFabricNodes(body=body, **kwargs)

@register('nodesDeleteFabricNode')
def nodesDeleteFabricNode(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().nodesDeleteFabricNode(body=body, **kwargs)

@register('nodesGetNamedFabricNode')
def nodesGetNamedFabricNode(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().nodesGetNamedFabricNode(body=body, **kwargs)

@register('nodesUpdateFabricNode')
def nodesUpdateFabricNode(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().nodesUpdateFabricNode(body=body, **kwargs)

@register('devicesUnbindDevice')
def devicesUnbindDevice(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().devicesUnbindDevice(body=body, **kwargs)

@register('devicesBindDevice')
def devicesBindDevice(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().devicesBindDevice(body=body, **kwargs)

@register('nodesGetManagementPorts')
def nodesGetManagementPorts(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().nodesGetManagementPorts(body=body, **kwargs)

@register('nodesAddManagementPorts')
def nodesAddManagementPorts(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().nodesAddManagementPorts(body=body, **kwargs)

@register('nodesGetManagementPort')
def nodesGetManagementPort(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().nodesGetManagementPort(body=body, **kwargs)

@register('nodesUpdateManagementPort')
def nodesUpdateManagementPort(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().nodesUpdateManagementPort(body=body, **kwargs)

@register('nodesGetPorts')
def nodesGetPorts(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().nodesGetPorts(body=body, **kwargs)

@register('nodesSetPorts')
def nodesSetPorts(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().nodesSetPorts(body=body, **kwargs)

@register('nodesResetPort')
def nodesResetPort(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().nodesResetPort(body=body, **kwargs)

@register('nodesGetPort')
def nodesGetPort(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().nodesGetPort(body=body, **kwargs)

@register('nodesUpdatePort')
def nodesUpdatePort(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().nodesUpdatePort(body=body, **kwargs)

@register('vnisGetFabricVnis')
def vnisGetFabricVnis(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().vnisGetFabricVnis(body=body, **kwargs)

@register('vnisAddFabricVnis')
def vnisAddFabricVnis(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().vnisAddFabricVnis(body=body, **kwargs)

@register('vnisDeleteFabricVni')
def vnisDeleteFabricVni(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().vnisDeleteFabricVni(body=body, **kwargs)

@register('vnisGetFabricVni')
def vnisGetFabricVni(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().vnisGetFabricVni(body=body, **kwargs)

@register('vnisUpdateFabricVni')
def vnisUpdateFabricVni(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().vnisUpdateFabricVni(body=body, **kwargs)

@register('vnisGetFabricVniMembers')
def vnisGetFabricVniMembers(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().vnisGetFabricVniMembers(body=body, **kwargs)

@register('vnisAddFabricVniMembers')
def vnisAddFabricVniMembers(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().vnisAddFabricVniMembers(body=body, **kwargs)

@register('vnisDeleteFabricVniMember')
def vnisDeleteFabricVniMember(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().vnisDeleteFabricVniMember(body=body, **kwargs)

@register('vnisGetFabricVniMember')
def vnisGetFabricVniMember(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().vnisGetFabricVniMember(body=body, **kwargs)

@register('vrfsGetFabricVrfs')
def vrfsGetFabricVrfs(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().vrfsGetFabricVrfs(body=body, **kwargs)

@register('vrfsAddFabricVrfs')
def vrfsAddFabricVrfs(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().vrfsAddFabricVrfs(body=body, **kwargs)

@register('vrfsDeleteFabricVrf')
def vrfsDeleteFabricVrf(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().vrfsDeleteFabricVrf(body=body, **kwargs)

@register('vrfsGetFabricVrf')
def vrfsGetFabricVrf(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().vrfsGetFabricVrf(body=body, **kwargs)

@register('vrfsUpdateFabricVrf')
def vrfsUpdateFabricVrf(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().vrfsUpdateFabricVrf(body=body, **kwargs)

@register('vrfsGetFabricStaticRoutes')
def vrfsGetFabricStaticRoutes(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().vrfsGetFabricStaticRoutes(body=body, **kwargs)

@register('vrfsAddFabricStaticRoutes')
def vrfsAddFabricStaticRoutes(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().vrfsAddFabricStaticRoutes(body=body, **kwargs)

@register('vrfsDeleteFabricStaticRoute')
def vrfsDeleteFabricStaticRoute(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().vrfsDeleteFabricStaticRoute(body=body, **kwargs)

@register('vrfsGetFabricStaticRoute')
def vrfsGetFabricStaticRoute(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().vrfsGetFabricStaticRoute(body=body, **kwargs)

@register('vrfsUpdateFabricStaticRoute')
def vrfsUpdateFabricStaticRoute(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().vrfsUpdateFabricStaticRoute(body=body, **kwargs)

@register('authGetUsers')
def authGetUsers(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().authGetUsers(body=body, **kwargs)

@register('authSetUsers')
def authSetUsers(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().authSetUsers(body=body, **kwargs)

@register('authDeleteUser')
def authDeleteUser(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().authDeleteUser(body=body, **kwargs)

@register('authGetUser')
def authGetUser(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().authGetUser(body=body, **kwargs)

@register('authUpdateUser')
def authUpdateUser(body: dict | None = None, **kwargs):
    """Auto‑generated wrapper.

    If `body` is omitted we wrap all remaining keyword arguments
    into it so the underlying SDK still receives the required
    payload.
    """
    if body is None:
        body = kwargs
        kwargs = {}
    return Nexus_hyperfabricClient().authUpdateUser(body=body, **kwargs)
