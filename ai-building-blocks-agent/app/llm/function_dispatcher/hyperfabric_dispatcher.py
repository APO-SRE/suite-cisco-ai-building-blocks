# app/llm/function_dispatcher/hyperfabric_dispatcher.py
from app.llm.function_dispatcher import register
from app.llm.platform_clients.hyperfabric_client import HyperfabricClient

@register('historyGetAssertionHistoryCounterReport')
def historyGetAssertionHistoryCounterReport(**kwargs):
    return HyperfabricClient().historyGetAssertionHistoryCounterReport(**kwargs)

@register('historyGetAssertionHistoryRecord')
def historyGetAssertionHistoryRecord(**kwargs):
    return HyperfabricClient().historyGetAssertionHistoryRecord(**kwargs)

@register('authGetBearerTokens')
def authGetBearerTokens(**kwargs):
    return HyperfabricClient().authGetBearerTokens(**kwargs)

@register('authGetBearerToken')
def authGetBearerToken(**kwargs):
    return HyperfabricClient().authGetBearerToken(**kwargs)

@register('devicesGetDevices')
def devicesGetDevices(**kwargs):
    return HyperfabricClient().devicesGetDevices(**kwargs)

@register('fabricsGetAllFabrics')
def fabricsGetAllFabrics(**kwargs):
    return HyperfabricClient().fabricsGetAllFabrics(**kwargs)

@register('fabricsGetFabric')
def fabricsGetFabric(**kwargs):
    return HyperfabricClient().fabricsGetFabric(**kwargs)

@register('fabricsGetFabricCandidates')
def fabricsGetFabricCandidates(**kwargs):
    return HyperfabricClient().fabricsGetFabricCandidates(**kwargs)

@register('fabricsGetFabricCandidate')
def fabricsGetFabricCandidate(**kwargs):
    return HyperfabricClient().fabricsGetFabricCandidate(**kwargs)

@register('fabricsGetFabricConfig')
def fabricsGetFabricConfig(**kwargs):
    return HyperfabricClient().fabricsGetFabricConfig(**kwargs)

@register('fabricsGetFabricConnections')
def fabricsGetFabricConnections(**kwargs):
    return HyperfabricClient().fabricsGetFabricConnections(**kwargs)

@register('fabricsGetFabricConnection')
def fabricsGetFabricConnection(**kwargs):
    return HyperfabricClient().fabricsGetFabricConnection(**kwargs)

@register('stateGetDeviceAssertions')
def stateGetDeviceAssertions(**kwargs):
    return HyperfabricClient().stateGetDeviceAssertions(**kwargs)

@register('stateGetDeviceCounters')
def stateGetDeviceCounters(**kwargs):
    return HyperfabricClient().stateGetDeviceCounters(**kwargs)

@register('devicesGetDeviceManagementPorts')
def devicesGetDeviceManagementPorts(**kwargs):
    return HyperfabricClient().devicesGetDeviceManagementPorts(**kwargs)

@register('stateGetDevicePortAssertions')
def stateGetDevicePortAssertions(**kwargs):
    return HyperfabricClient().stateGetDevicePortAssertions(**kwargs)

@register('stateGetDevicePortCounters')
def stateGetDevicePortCounters(**kwargs):
    return HyperfabricClient().stateGetDevicePortCounters(**kwargs)

@register('stateGetDeviceSensors')
def stateGetDeviceSensors(**kwargs):
    return HyperfabricClient().stateGetDeviceSensors(**kwargs)

@register('nodesGetFabricNodes')
def nodesGetFabricNodes(**kwargs):
    return HyperfabricClient().nodesGetFabricNodes(**kwargs)

@register('nodesGetNamedFabricNode')
def nodesGetNamedFabricNode(**kwargs):
    return HyperfabricClient().nodesGetNamedFabricNode(**kwargs)

@register('nodesGetManagementPorts')
def nodesGetManagementPorts(**kwargs):
    return HyperfabricClient().nodesGetManagementPorts(**kwargs)

@register('nodesGetManagementPort')
def nodesGetManagementPort(**kwargs):
    return HyperfabricClient().nodesGetManagementPort(**kwargs)

@register('nodesGetPorts')
def nodesGetPorts(**kwargs):
    return HyperfabricClient().nodesGetPorts(**kwargs)

@register('nodesGetPort')
def nodesGetPort(**kwargs):
    return HyperfabricClient().nodesGetPort(**kwargs)

@register('vnisGetFabricVnis')
def vnisGetFabricVnis(**kwargs):
    return HyperfabricClient().vnisGetFabricVnis(**kwargs)

@register('vnisGetFabricVni')
def vnisGetFabricVni(**kwargs):
    return HyperfabricClient().vnisGetFabricVni(**kwargs)

@register('vnisGetFabricVniMembers')
def vnisGetFabricVniMembers(**kwargs):
    return HyperfabricClient().vnisGetFabricVniMembers(**kwargs)

@register('vnisGetFabricVniMember')
def vnisGetFabricVniMember(**kwargs):
    return HyperfabricClient().vnisGetFabricVniMember(**kwargs)

@register('vrfsGetFabricVrfs')
def vrfsGetFabricVrfs(**kwargs):
    return HyperfabricClient().vrfsGetFabricVrfs(**kwargs)

@register('vrfsGetFabricVrf')
def vrfsGetFabricVrf(**kwargs):
    return HyperfabricClient().vrfsGetFabricVrf(**kwargs)

@register('vrfsGetFabricStaticRoutes')
def vrfsGetFabricStaticRoutes(**kwargs):
    return HyperfabricClient().vrfsGetFabricStaticRoutes(**kwargs)

@register('vrfsGetFabricStaticRoute')
def vrfsGetFabricStaticRoute(**kwargs):
    return HyperfabricClient().vrfsGetFabricStaticRoute(**kwargs)

@register('authGetUsers')
def authGetUsers(**kwargs):
    return HyperfabricClient().authGetUsers(**kwargs)

@register('authGetUser')
def authGetUser(**kwargs):
    return HyperfabricClient().authGetUser(**kwargs)
