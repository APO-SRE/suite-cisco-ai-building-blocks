# app/llm/function_dispatcher/nexus_hyperfabric_dispatcher.py
from typing import Any
from app.llm.function_dispatcher import register
from app.llm.platform_clients.nexus_hyperfabric_client import Nexus_hyperfabricClient

@register('authGetBearerTokens')
def authGetBearerTokens(**kwargs):
    return Nexus_hyperfabricClient().authGetBearerTokens(**{**kwargs})

@register('authGetBearerToken')
def authGetBearerToken(tokenId: str, **kwargs):
    return Nexus_hyperfabricClient().authGetBearerToken(**{'tokenId': tokenId, **kwargs})

@register('devicesGetDevices')
def devicesGetDevices():
    return Nexus_hyperfabricClient().devicesGetDevices(**{})

@register('fabricsGetAllFabrics')
def fabricsGetAllFabrics(**kwargs):
    return Nexus_hyperfabricClient().fabricsGetAllFabrics(**{**kwargs})

@register('fabricsGetFabric')
def fabricsGetFabric(fabricId: str, **kwargs):
    return Nexus_hyperfabricClient().fabricsGetFabric(**{'fabricId': fabricId, **kwargs})

@register('fabricsGetFabricCandidates')
def fabricsGetFabricCandidates(fabricId: str, **kwargs):
    return Nexus_hyperfabricClient().fabricsGetFabricCandidates(**{'fabricId': fabricId, **kwargs})

@register('fabricsGetFabricCandidate')
def fabricsGetFabricCandidate(fabricId: str, name: str, **kwargs):
    return Nexus_hyperfabricClient().fabricsGetFabricCandidate(**{'fabricId': fabricId, 'name': name, **kwargs})

@register('fabricsGetFabricConnections')
def fabricsGetFabricConnections(fabricId: str, **kwargs):
    return Nexus_hyperfabricClient().fabricsGetFabricConnections(**{'fabricId': fabricId, **kwargs})

@register('fabricsGetFabricConnection')
def fabricsGetFabricConnection(connectionId: str, fabricId: str, **kwargs):
    return Nexus_hyperfabricClient().fabricsGetFabricConnection(**{'connectionId': connectionId, 'fabricId': fabricId, **kwargs})

@register('nodesGetFabricNodes')
def nodesGetFabricNodes(fabricId: str, **kwargs):
    return Nexus_hyperfabricClient().nodesGetFabricNodes(**{'fabricId': fabricId, **kwargs})

@register('nodesGetNamedFabricNode')
def nodesGetNamedFabricNode(fabricId: str, nodeId: str, **kwargs):
    return Nexus_hyperfabricClient().nodesGetNamedFabricNode(**{'fabricId': fabricId, 'nodeId': nodeId, **kwargs})

@register('nodesGetManagementPorts')
def nodesGetManagementPorts(fabricId: str, nodeId: str, **kwargs):
    return Nexus_hyperfabricClient().nodesGetManagementPorts(**{'fabricId': fabricId, 'nodeId': nodeId, **kwargs})

@register('nodesGetManagementPort')
def nodesGetManagementPort(fabricId: str, id: str, nodeId: str, **kwargs):
    return Nexus_hyperfabricClient().nodesGetManagementPort(**{'fabricId': fabricId, 'id': id, 'nodeId': nodeId, **kwargs})

@register('nodesGetPorts')
def nodesGetPorts(fabricId: str, nodeId: str, **kwargs):
    return Nexus_hyperfabricClient().nodesGetPorts(**{'fabricId': fabricId, 'nodeId': nodeId, **kwargs})

@register('nodesGetPort')
def nodesGetPort(fabricId: str, nodeId: str, portId: str, **kwargs):
    return Nexus_hyperfabricClient().nodesGetPort(**{'fabricId': fabricId, 'nodeId': nodeId, 'portId': portId, **kwargs})

@register('vnisGetFabricVnis')
def vnisGetFabricVnis(fabricId: str, **kwargs):
    return Nexus_hyperfabricClient().vnisGetFabricVnis(**{'fabricId': fabricId, **kwargs})

@register('vnisGetFabricVni')
def vnisGetFabricVni(fabricId: str, vniId: str, **kwargs):
    return Nexus_hyperfabricClient().vnisGetFabricVni(**{'fabricId': fabricId, 'vniId': vniId, **kwargs})

@register('vnisGetFabricVniMembers')
def vnisGetFabricVniMembers(fabricId: str, vniId: str, **kwargs):
    return Nexus_hyperfabricClient().vnisGetFabricVniMembers(**{'fabricId': fabricId, 'vniId': vniId, **kwargs})

@register('vnisGetFabricVniMember')
def vnisGetFabricVniMember(fabricId: str, memberId: str, vniId: str, **kwargs):
    return Nexus_hyperfabricClient().vnisGetFabricVniMember(**{'fabricId': fabricId, 'memberId': memberId, 'vniId': vniId, **kwargs})

@register('vrfsGetFabricVrfs')
def vrfsGetFabricVrfs(fabricId: str, **kwargs):
    return Nexus_hyperfabricClient().vrfsGetFabricVrfs(**{'fabricId': fabricId, **kwargs})

@register('vrfsGetFabricVrf')
def vrfsGetFabricVrf(fabricId: str, vrfId: str, **kwargs):
    return Nexus_hyperfabricClient().vrfsGetFabricVrf(**{'fabricId': fabricId, 'vrfId': vrfId, **kwargs})

@register('vrfsGetFabricStaticRoutes')
def vrfsGetFabricStaticRoutes(fabricId: str, vrfId: str, **kwargs):
    return Nexus_hyperfabricClient().vrfsGetFabricStaticRoutes(**{'fabricId': fabricId, 'vrfId': vrfId, **kwargs})

@register('vrfsGetFabricStaticRoute')
def vrfsGetFabricStaticRoute(fabricId: str, routeId: str, vrfId: str, **kwargs):
    return Nexus_hyperfabricClient().vrfsGetFabricStaticRoute(**{'fabricId': fabricId, 'routeId': routeId, 'vrfId': vrfId, **kwargs})

@register('authGetUsers')
def authGetUsers(**kwargs):
    return Nexus_hyperfabricClient().authGetUsers(**{**kwargs})

@register('authGetUser')
def authGetUser(userId: str, **kwargs):
    return Nexus_hyperfabricClient().authGetUser(**{'userId': userId, **kwargs})
