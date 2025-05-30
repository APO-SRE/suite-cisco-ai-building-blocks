from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_count_response import ClientCountResponse
from ...models.errors import Errors
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    device_type: Union[Unset, str] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    ip_address: Union[Unset, str] = UNSET,
    floor_id: Union[Unset, str] = UNSET,
    building_id: Union[Unset, str] = UNSET,
    campus_id: Union[Unset, str] = UNSET,
    associated: Union[Unset, bool] = UNSET,
    ssid: Union[Unset, str] = UNSET,
    ap_mac_address: Union[Unset, str] = UNSET,
    rogue_ap_clients: Union[Unset, bool] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    group_by: Union[Unset, str] = UNSET,
    map_element_id: Union[Unset, str] = UNSET,
    map_element_level: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["deviceType"] = device_type

    params["deviceId"] = device_id

    params["ipAddress"] = ip_address

    params["floorId"] = floor_id

    params["buildingId"] = building_id

    params["campusId"] = campus_id

    params["associated"] = associated

    params["ssid"] = ssid

    params["apMacAddress"] = ap_mac_address

    params["rogueApClients"] = rogue_ap_clients

    params["manufacturer"] = manufacturer

    params["groupBy"] = group_by

    params["mapElementId"] = map_element_id

    params["mapElementLevel"] = map_element_level

    params["username"] = username

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/devices/count",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ClientCountResponse, Errors]]:
    if response.status_code == 200:
        response_200 = ClientCountResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Errors.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = Errors.from_dict(response.json())

        return response_401
    if response.status_code == 500:
        response_500 = Errors.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ClientCountResponse, Errors]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    device_type: Union[Unset, str] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    ip_address: Union[Unset, str] = UNSET,
    floor_id: Union[Unset, str] = UNSET,
    building_id: Union[Unset, str] = UNSET,
    campus_id: Union[Unset, str] = UNSET,
    associated: Union[Unset, bool] = UNSET,
    ssid: Union[Unset, str] = UNSET,
    ap_mac_address: Union[Unset, str] = UNSET,
    rogue_ap_clients: Union[Unset, bool] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    group_by: Union[Unset, str] = UNSET,
    map_element_id: Union[Unset, str] = UNSET,
    map_element_level: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Response[Union[ClientCountResponse, Errors]]:
    """Retrieve the active devices count. The API supports searching by a variety of parameters. If no
    parameters are given, the count of all active devices are returned.

    Args:
        device_type (Union[Unset, str]):
        device_id (Union[Unset, str]):
        ip_address (Union[Unset, str]):
        floor_id (Union[Unset, str]):
        building_id (Union[Unset, str]):
        campus_id (Union[Unset, str]):
        associated (Union[Unset, bool]):
        ssid (Union[Unset, str]):
        ap_mac_address (Union[Unset, str]):
        rogue_ap_clients (Union[Unset, bool]):
        manufacturer (Union[Unset, str]):
        group_by (Union[Unset, str]):
        map_element_id (Union[Unset, str]):
        map_element_level (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientCountResponse, Errors]]
    """

    kwargs = _get_kwargs(
        device_type=device_type,
        device_id=device_id,
        ip_address=ip_address,
        floor_id=floor_id,
        building_id=building_id,
        campus_id=campus_id,
        associated=associated,
        ssid=ssid,
        ap_mac_address=ap_mac_address,
        rogue_ap_clients=rogue_ap_clients,
        manufacturer=manufacturer,
        group_by=group_by,
        map_element_id=map_element_id,
        map_element_level=map_element_level,
        username=username,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    device_type: Union[Unset, str] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    ip_address: Union[Unset, str] = UNSET,
    floor_id: Union[Unset, str] = UNSET,
    building_id: Union[Unset, str] = UNSET,
    campus_id: Union[Unset, str] = UNSET,
    associated: Union[Unset, bool] = UNSET,
    ssid: Union[Unset, str] = UNSET,
    ap_mac_address: Union[Unset, str] = UNSET,
    rogue_ap_clients: Union[Unset, bool] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    group_by: Union[Unset, str] = UNSET,
    map_element_id: Union[Unset, str] = UNSET,
    map_element_level: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Optional[Union[ClientCountResponse, Errors]]:
    """Retrieve the active devices count. The API supports searching by a variety of parameters. If no
    parameters are given, the count of all active devices are returned.

    Args:
        device_type (Union[Unset, str]):
        device_id (Union[Unset, str]):
        ip_address (Union[Unset, str]):
        floor_id (Union[Unset, str]):
        building_id (Union[Unset, str]):
        campus_id (Union[Unset, str]):
        associated (Union[Unset, bool]):
        ssid (Union[Unset, str]):
        ap_mac_address (Union[Unset, str]):
        rogue_ap_clients (Union[Unset, bool]):
        manufacturer (Union[Unset, str]):
        group_by (Union[Unset, str]):
        map_element_id (Union[Unset, str]):
        map_element_level (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientCountResponse, Errors]
    """

    return sync_detailed(
        client=client,
        device_type=device_type,
        device_id=device_id,
        ip_address=ip_address,
        floor_id=floor_id,
        building_id=building_id,
        campus_id=campus_id,
        associated=associated,
        ssid=ssid,
        ap_mac_address=ap_mac_address,
        rogue_ap_clients=rogue_ap_clients,
        manufacturer=manufacturer,
        group_by=group_by,
        map_element_id=map_element_id,
        map_element_level=map_element_level,
        username=username,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    device_type: Union[Unset, str] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    ip_address: Union[Unset, str] = UNSET,
    floor_id: Union[Unset, str] = UNSET,
    building_id: Union[Unset, str] = UNSET,
    campus_id: Union[Unset, str] = UNSET,
    associated: Union[Unset, bool] = UNSET,
    ssid: Union[Unset, str] = UNSET,
    ap_mac_address: Union[Unset, str] = UNSET,
    rogue_ap_clients: Union[Unset, bool] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    group_by: Union[Unset, str] = UNSET,
    map_element_id: Union[Unset, str] = UNSET,
    map_element_level: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Response[Union[ClientCountResponse, Errors]]:
    """Retrieve the active devices count. The API supports searching by a variety of parameters. If no
    parameters are given, the count of all active devices are returned.

    Args:
        device_type (Union[Unset, str]):
        device_id (Union[Unset, str]):
        ip_address (Union[Unset, str]):
        floor_id (Union[Unset, str]):
        building_id (Union[Unset, str]):
        campus_id (Union[Unset, str]):
        associated (Union[Unset, bool]):
        ssid (Union[Unset, str]):
        ap_mac_address (Union[Unset, str]):
        rogue_ap_clients (Union[Unset, bool]):
        manufacturer (Union[Unset, str]):
        group_by (Union[Unset, str]):
        map_element_id (Union[Unset, str]):
        map_element_level (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientCountResponse, Errors]]
    """

    kwargs = _get_kwargs(
        device_type=device_type,
        device_id=device_id,
        ip_address=ip_address,
        floor_id=floor_id,
        building_id=building_id,
        campus_id=campus_id,
        associated=associated,
        ssid=ssid,
        ap_mac_address=ap_mac_address,
        rogue_ap_clients=rogue_ap_clients,
        manufacturer=manufacturer,
        group_by=group_by,
        map_element_id=map_element_id,
        map_element_level=map_element_level,
        username=username,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    device_type: Union[Unset, str] = UNSET,
    device_id: Union[Unset, str] = UNSET,
    ip_address: Union[Unset, str] = UNSET,
    floor_id: Union[Unset, str] = UNSET,
    building_id: Union[Unset, str] = UNSET,
    campus_id: Union[Unset, str] = UNSET,
    associated: Union[Unset, bool] = UNSET,
    ssid: Union[Unset, str] = UNSET,
    ap_mac_address: Union[Unset, str] = UNSET,
    rogue_ap_clients: Union[Unset, bool] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    group_by: Union[Unset, str] = UNSET,
    map_element_id: Union[Unset, str] = UNSET,
    map_element_level: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
) -> Optional[Union[ClientCountResponse, Errors]]:
    """Retrieve the active devices count. The API supports searching by a variety of parameters. If no
    parameters are given, the count of all active devices are returned.

    Args:
        device_type (Union[Unset, str]):
        device_id (Union[Unset, str]):
        ip_address (Union[Unset, str]):
        floor_id (Union[Unset, str]):
        building_id (Union[Unset, str]):
        campus_id (Union[Unset, str]):
        associated (Union[Unset, bool]):
        ssid (Union[Unset, str]):
        ap_mac_address (Union[Unset, str]):
        rogue_ap_clients (Union[Unset, bool]):
        manufacturer (Union[Unset, str]):
        group_by (Union[Unset, str]):
        map_element_id (Union[Unset, str]):
        map_element_level (Union[Unset, str]):
        username (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientCountResponse, Errors]
    """

    return (
        await asyncio_detailed(
            client=client,
            device_type=device_type,
            device_id=device_id,
            ip_address=ip_address,
            floor_id=floor_id,
            building_id=building_id,
            campus_id=campus_id,
            associated=associated,
            ssid=ssid,
            ap_mac_address=ap_mac_address,
            rogue_ap_clients=rogue_ap_clients,
            manufacturer=manufacturer,
            group_by=group_by,
            map_element_id=map_element_id,
            map_element_level=map_element_level,
            username=username,
        )
    ).parsed
