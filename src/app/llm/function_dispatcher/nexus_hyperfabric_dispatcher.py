# app/llm/function_dispatcher/nexus_hyperfabric_dispatcher.py
from typing import Any
from app.llm.function_dispatcher import register
from app.llm.platform_clients.nexus_hyperfabric_client import Nexus_hyperfabricClient

@register('authGetBearerTokens')
def authGetBearerTokens(**kwargs):
    return Nexus_hyperfabricClient().authGetBearerTokens(**{**kwargs})

@register('authCreateBearerTokens')
def authCreateBearerTokens():
    return Nexus_hyperfabricClient().authCreateBearerTokens(**{})

@register('authDeleteBearerToken')
def authDeleteBearerToken(tokenId: str):
    return Nexus_hyperfabricClient().authDeleteBearerToken(**{'tokenId': tokenId})

@register('authGetBearerToken')
def authGetBearerToken(tokenId: str, **kwargs):
    return Nexus_hyperfabricClient().authGetBearerToken(**{'tokenId': tokenId, **kwargs})

@register('devicesGetDevices')
def devicesGetDevices():
    return Nexus_hyperfabricClient().devicesGetDevices(**{})

@register('fabricsGetAllFabrics')
def fabricsGetAllFabrics(**kwargs):
    return Nexus_hyperfabricClient().fabricsGetAllFabrics(**{**kwargs})

@register('fabricsAddFabrics')
def fabricsAddFabrics():
    return Nexus_hyperfabricClient().fabricsAddFabrics(**{})

@register('fabricsDeleteFabric')
def fabricsDeleteFabric(fabricId: str):
    return Nexus_hyperfabricClient().fabricsDeleteFabric(**{'fabricId': fabricId})

@register('fabricsGetFabric')
def fabricsGetFabric(fabricId: str, **kwargs):
    return Nexus_hyperfabricClient().fabricsGetFabric(**{'fabricId': fabricId, **kwargs})

@register('fabricsUpdateFabric')
def fabricsUpdateFabric(fabricId: str):
    return Nexus_hyperfabricClient().fabricsUpdateFabric(**{'fabricId': fabricId})

@register('fabricsGetFabricCandidates')
def fabricsGetFabricCandidates(fabricId: str, **kwargs):
    return Nexus_hyperfabricClient().fabricsGetFabricCandidates(**{'fabricId': fabricId, **kwargs})

@register('fabricsRevertFabricCandidate')
def fabricsRevertFabricCandidate(fabricId: str, name: str):
    return Nexus_hyperfabricClient().fabricsRevertFabricCandidate(**{'fabricId': fabricId, 'name': name})

@register('fabricsGetFabricCandidate')
def fabricsGetFabricCandidate(fabricId: str, name: str, **kwargs):
    return Nexus_hyperfabricClient().fabricsGetFabricCandidate(**{'fabricId': fabricId, 'name': name, **kwargs})

@register('fabricsCommitFabricCandidate')
def fabricsCommitFabricCandidate(fabricId: str, name: str):
    return Nexus_hyperfabricClient().fabricsCommitFabricCandidate(**{'fabricId': fabricId, 'name': name})

@register('fabricsReviewFabricCandidate')
def fabricsReviewFabricCandidate(fabricId: str, name: str):
    return Nexus_hyperfabricClient().fabricsReviewFabricCandidate(**{'fabricId': fabricId, 'name': name})

@register('fabricsDeleteFabricConnections')
def fabricsDeleteFabricConnections(fabricId: str):
    return Nexus_hyperfabricClient().fabricsDeleteFabricConnections(**{'fabricId': fabricId})

@register('fabricsGetFabricConnections')
def fabricsGetFabricConnections(fabricId: str, **kwargs):
    return Nexus_hyperfabricClient().fabricsGetFabricConnections(**{'fabricId': fabricId, **kwargs})

@register('fabricsAddFabricConnections')
def fabricsAddFabricConnections(fabricId: str):
    return Nexus_hyperfabricClient().fabricsAddFabricConnections(**{'fabricId': fabricId})

@register('fabricsSetFabricConnections')
def fabricsSetFabricConnections(fabricId: str):
    return Nexus_hyperfabricClient().fabricsSetFabricConnections(**{'fabricId': fabricId})

@register('fabricsDeleteFabricConnection')
def fabricsDeleteFabricConnection(connectionId: str, fabricId: str):
    return Nexus_hyperfabricClient().fabricsDeleteFabricConnection(**{'connectionId': connectionId, 'fabricId': fabricId})

@register('fabricsGetFabricConnection')
def fabricsGetFabricConnection(connectionId: str, fabricId: str, **kwargs):
    return Nexus_hyperfabricClient().fabricsGetFabricConnection(**{'connectionId': connectionId, 'fabricId': fabricId, **kwargs})

@register('nodesGetFabricNodes')
def nodesGetFabricNodes(fabricId: str, **kwargs):
    return Nexus_hyperfabricClient().nodesGetFabricNodes(**{'fabricId': fabricId, **kwargs})

@register('nodesAddFabricNodes')
def nodesAddFabricNodes(fabricId: str):
    return Nexus_hyperfabricClient().nodesAddFabricNodes(**{'fabricId': fabricId})

@register('nodesDeleteFabricNode')
def nodesDeleteFabricNode(fabricId: str, nodeId: str):
    return Nexus_hyperfabricClient().nodesDeleteFabricNode(**{'fabricId': fabricId, 'nodeId': nodeId})

@register('nodesGetNamedFabricNode')
def nodesGetNamedFabricNode(fabricId: str, nodeId: str, **kwargs):
    return Nexus_hyperfabricClient().nodesGetNamedFabricNode(**{'fabricId': fabricId, 'nodeId': nodeId, **kwargs})

@register('nodesUpdateFabricNode')
def nodesUpdateFabricNode(fabricId: str, nodeId: str):
    return Nexus_hyperfabricClient().nodesUpdateFabricNode(**{'fabricId': fabricId, 'nodeId': nodeId})

@register('devicesUnbindDevice')
def devicesUnbindDevice(fabricId: str, nodeId: str):
    return Nexus_hyperfabricClient().devicesUnbindDevice(**{'fabricId': fabricId, 'nodeId': nodeId})

@register('devicesBindDevice')
def devicesBindDevice(deviceId: str, fabricId: str, nodeId: str):
    return Nexus_hyperfabricClient().devicesBindDevice(**{'deviceId': deviceId, 'fabricId': fabricId, 'nodeId': nodeId})

@register('nodesGetManagementPorts')
def nodesGetManagementPorts(fabricId: str, nodeId: str, **kwargs):
    return Nexus_hyperfabricClient().nodesGetManagementPorts(**{'fabricId': fabricId, 'nodeId': nodeId, **kwargs})

@register('nodesAddManagementPorts')
def nodesAddManagementPorts(fabricId: str, nodeId: str):
    return Nexus_hyperfabricClient().nodesAddManagementPorts(**{'fabricId': fabricId, 'nodeId': nodeId})

@register('nodesGetManagementPort')
def nodesGetManagementPort(fabricId: str, id: str, nodeId: str, **kwargs):
    return Nexus_hyperfabricClient().nodesGetManagementPort(**{'fabricId': fabricId, 'id': id, 'nodeId': nodeId, **kwargs})

@register('nodesUpdateManagementPort')
def nodesUpdateManagementPort(fabricId: str, id: str, nodeId: str):
    return Nexus_hyperfabricClient().nodesUpdateManagementPort(**{'fabricId': fabricId, 'id': id, 'nodeId': nodeId})

@register('nodesGetPorts')
def nodesGetPorts(fabricId: str, nodeId: str, **kwargs):
    return Nexus_hyperfabricClient().nodesGetPorts(**{'fabricId': fabricId, 'nodeId': nodeId, **kwargs})

@register('nodesSetPorts')
def nodesSetPorts(fabricId: str, nodeId: str):
    return Nexus_hyperfabricClient().nodesSetPorts(**{'fabricId': fabricId, 'nodeId': nodeId})

@register('nodesResetPort')
def nodesResetPort(fabricId: str, nodeId: str, portId: str):
    return Nexus_hyperfabricClient().nodesResetPort(**{'fabricId': fabricId, 'nodeId': nodeId, 'portId': portId})

@register('nodesGetPort')
def nodesGetPort(fabricId: str, nodeId: str, portId: str, **kwargs):
    return Nexus_hyperfabricClient().nodesGetPort(**{'fabricId': fabricId, 'nodeId': nodeId, 'portId': portId, **kwargs})

@register('nodesUpdatePort')
def nodesUpdatePort(fabricId: str, nodeId: str, portId: str):
    return Nexus_hyperfabricClient().nodesUpdatePort(**{'fabricId': fabricId, 'nodeId': nodeId, 'portId': portId})

@register('vnisGetFabricVnis')
def vnisGetFabricVnis(fabricId: str, **kwargs):
    return Nexus_hyperfabricClient().vnisGetFabricVnis(**{'fabricId': fabricId, **kwargs})

@register('vnisAddFabricVnis')
def vnisAddFabricVnis(fabricId: str):
    return Nexus_hyperfabricClient().vnisAddFabricVnis(**{'fabricId': fabricId})

@register('vnisDeleteFabricVni')
def vnisDeleteFabricVni(fabricId: str, vniId: str):
    return Nexus_hyperfabricClient().vnisDeleteFabricVni(**{'fabricId': fabricId, 'vniId': vniId})

@register('vnisGetFabricVni')
def vnisGetFabricVni(fabricId: str, vniId: str, **kwargs):
    return Nexus_hyperfabricClient().vnisGetFabricVni(**{'fabricId': fabricId, 'vniId': vniId, **kwargs})

@register('vnisUpdateFabricVni')
def vnisUpdateFabricVni(fabricId: str, vniId: str):
    return Nexus_hyperfabricClient().vnisUpdateFabricVni(**{'fabricId': fabricId, 'vniId': vniId})

@register('vnisGetFabricVniMembers')
def vnisGetFabricVniMembers(fabricId: str, vniId: str, **kwargs):
    return Nexus_hyperfabricClient().vnisGetFabricVniMembers(**{'fabricId': fabricId, 'vniId': vniId, **kwargs})

@register('vnisAddFabricVniMembers')
def vnisAddFabricVniMembers(fabricId: str, vniId: str):
    return Nexus_hyperfabricClient().vnisAddFabricVniMembers(**{'fabricId': fabricId, 'vniId': vniId})

@register('vnisDeleteFabricVniMember')
def vnisDeleteFabricVniMember(fabricId: str, memberId: str, vniId: str):
    return Nexus_hyperfabricClient().vnisDeleteFabricVniMember(**{'fabricId': fabricId, 'memberId': memberId, 'vniId': vniId})

@register('vnisGetFabricVniMember')
def vnisGetFabricVniMember(fabricId: str, memberId: str, vniId: str, **kwargs):
    return Nexus_hyperfabricClient().vnisGetFabricVniMember(**{'fabricId': fabricId, 'memberId': memberId, 'vniId': vniId, **kwargs})

@register('vrfsGetFabricVrfs')
def vrfsGetFabricVrfs(fabricId: str, **kwargs):
    return Nexus_hyperfabricClient().vrfsGetFabricVrfs(**{'fabricId': fabricId, **kwargs})

@register('vrfsAddFabricVrfs')
def vrfsAddFabricVrfs(fabricId: str):
    return Nexus_hyperfabricClient().vrfsAddFabricVrfs(**{'fabricId': fabricId})

@register('vrfsDeleteFabricVrf')
def vrfsDeleteFabricVrf(fabricId: str, vrfId: str):
    return Nexus_hyperfabricClient().vrfsDeleteFabricVrf(**{'fabricId': fabricId, 'vrfId': vrfId})

@register('vrfsGetFabricVrf')
def vrfsGetFabricVrf(fabricId: str, vrfId: str, **kwargs):
    return Nexus_hyperfabricClient().vrfsGetFabricVrf(**{'fabricId': fabricId, 'vrfId': vrfId, **kwargs})

@register('vrfsUpdateFabricVrf')
def vrfsUpdateFabricVrf(fabricId: str, vrfId: str):
    return Nexus_hyperfabricClient().vrfsUpdateFabricVrf(**{'fabricId': fabricId, 'vrfId': vrfId})

@register('vrfsGetFabricStaticRoutes')
def vrfsGetFabricStaticRoutes(fabricId: str, vrfId: str, **kwargs):
    return Nexus_hyperfabricClient().vrfsGetFabricStaticRoutes(**{'fabricId': fabricId, 'vrfId': vrfId, **kwargs})

@register('vrfsAddFabricStaticRoutes')
def vrfsAddFabricStaticRoutes(fabricId: str, vrfId: str):
    return Nexus_hyperfabricClient().vrfsAddFabricStaticRoutes(**{'fabricId': fabricId, 'vrfId': vrfId})

@register('vrfsDeleteFabricStaticRoute')
def vrfsDeleteFabricStaticRoute(fabricId: str, routeId: str, vrfId: str):
    return Nexus_hyperfabricClient().vrfsDeleteFabricStaticRoute(**{'fabricId': fabricId, 'routeId': routeId, 'vrfId': vrfId})

@register('vrfsGetFabricStaticRoute')
def vrfsGetFabricStaticRoute(fabricId: str, routeId: str, vrfId: str, **kwargs):
    return Nexus_hyperfabricClient().vrfsGetFabricStaticRoute(**{'fabricId': fabricId, 'routeId': routeId, 'vrfId': vrfId, **kwargs})

@register('vrfsUpdateFabricStaticRoute')
def vrfsUpdateFabricStaticRoute(fabricId: str, routeId: str, vrfId: str):
    return Nexus_hyperfabricClient().vrfsUpdateFabricStaticRoute(**{'fabricId': fabricId, 'routeId': routeId, 'vrfId': vrfId})

@register('authGetUsers')
def authGetUsers(**kwargs):
    return Nexus_hyperfabricClient().authGetUsers(**{**kwargs})

@register('authSetUsers')
def authSetUsers():
    return Nexus_hyperfabricClient().authSetUsers(**{})

@register('authDeleteUser')
def authDeleteUser(userId: str):
    return Nexus_hyperfabricClient().authDeleteUser(**{'userId': userId})

@register('authGetUser')
def authGetUser(userId: str, **kwargs):
    return Nexus_hyperfabricClient().authGetUser(**{'userId': userId, **kwargs})

@register('authUpdateUser')
def authUpdateUser(userId: str):
    return Nexus_hyperfabricClient().authUpdateUser(**{'userId': userId})
