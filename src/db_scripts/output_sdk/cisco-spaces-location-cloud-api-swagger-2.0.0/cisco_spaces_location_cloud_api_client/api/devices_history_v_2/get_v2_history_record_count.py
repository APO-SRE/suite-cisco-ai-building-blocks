from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    device_id: Union[Unset, str] = UNSET,
    device_type: Union[Unset, str] = UNSET,
    ap_mac_address: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    ssid: Union[Unset, str] = UNSET,
    floor_id: Union[Unset, str] = UNSET,
    campus_id: Union[Unset, str] = UNSET,
    building_id: Union[Unset, str] = UNSET,
    start_time: Union[Unset, str] = UNSET,
    end_time: Union[Unset, str] = UNSET,
    associated: Union[Unset, bool] = UNSET,
    time_zone: Union[Unset, float] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["deviceId"] = device_id

    params["deviceType"] = device_type

    params["apMacAddress"] = ap_mac_address

    params["username"] = username

    params["ssid"] = ssid

    params["floorId"] = floor_id

    params["campusId"] = campus_id

    params["buildingId"] = building_id

    params["startTime"] = start_time

    params["endTime"] = end_time

    params["associated"] = associated

    params["timeZone"] = time_zone

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/history/record/count",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    device_id: Union[Unset, str] = UNSET,
    device_type: Union[Unset, str] = UNSET,
    ap_mac_address: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    ssid: Union[Unset, str] = UNSET,
    floor_id: Union[Unset, str] = UNSET,
    campus_id: Union[Unset, str] = UNSET,
    building_id: Union[Unset, str] = UNSET,
    start_time: Union[Unset, str] = UNSET,
    end_time: Union[Unset, str] = UNSET,
    associated: Union[Unset, bool] = UNSET,
    time_zone: Union[Unset, float] = UNSET,
) -> Response[Any]:
    """Gives the count of history records in given time range. If startTime and endTime is not given, then
    the default time range is the last 24 hours. Also, the time range is 1 day at most. Device type
    INTERFERER and ROGUE_AP are not supported.

    Args:
        device_id (Union[Unset, str]):
        device_type (Union[Unset, str]):
        ap_mac_address (Union[Unset, str]):
        username (Union[Unset, str]):
        ssid (Union[Unset, str]):
        floor_id (Union[Unset, str]):
        campus_id (Union[Unset, str]):
        building_id (Union[Unset, str]):
        start_time (Union[Unset, str]):
        end_time (Union[Unset, str]):
        associated (Union[Unset, bool]):
        time_zone (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        device_id=device_id,
        device_type=device_type,
        ap_mac_address=ap_mac_address,
        username=username,
        ssid=ssid,
        floor_id=floor_id,
        campus_id=campus_id,
        building_id=building_id,
        start_time=start_time,
        end_time=end_time,
        associated=associated,
        time_zone=time_zone,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    device_id: Union[Unset, str] = UNSET,
    device_type: Union[Unset, str] = UNSET,
    ap_mac_address: Union[Unset, str] = UNSET,
    username: Union[Unset, str] = UNSET,
    ssid: Union[Unset, str] = UNSET,
    floor_id: Union[Unset, str] = UNSET,
    campus_id: Union[Unset, str] = UNSET,
    building_id: Union[Unset, str] = UNSET,
    start_time: Union[Unset, str] = UNSET,
    end_time: Union[Unset, str] = UNSET,
    associated: Union[Unset, bool] = UNSET,
    time_zone: Union[Unset, float] = UNSET,
) -> Response[Any]:
    """Gives the count of history records in given time range. If startTime and endTime is not given, then
    the default time range is the last 24 hours. Also, the time range is 1 day at most. Device type
    INTERFERER and ROGUE_AP are not supported.

    Args:
        device_id (Union[Unset, str]):
        device_type (Union[Unset, str]):
        ap_mac_address (Union[Unset, str]):
        username (Union[Unset, str]):
        ssid (Union[Unset, str]):
        floor_id (Union[Unset, str]):
        campus_id (Union[Unset, str]):
        building_id (Union[Unset, str]):
        start_time (Union[Unset, str]):
        end_time (Union[Unset, str]):
        associated (Union[Unset, bool]):
        time_zone (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        device_id=device_id,
        device_type=device_type,
        ap_mac_address=ap_mac_address,
        username=username,
        ssid=ssid,
        floor_id=floor_id,
        campus_id=campus_id,
        building_id=building_id,
        start_time=start_time,
        end_time=end_time,
        associated=associated,
        time_zone=time_zone,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
