from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.history_csv_records import HistoryCsvRecords
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    format_type: str,
    limit: Union[Unset, float] = UNSET,
    format_: Union[Unset, str] = UNSET,
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

    params["formatType"] = format_type

    params["limit"] = limit

    params["format"] = format_

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
        "url": "/v2/history/record/export?formatType=csv",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Errors, HistoryCsvRecords]]:
    if response.status_code == 200:
        response_200 = HistoryCsvRecords.from_dict(response.text)

        return response_200
    if response.status_code == 400:
        response_400 = Errors.from_dict(response.text)

        return response_400
    if response.status_code == 401:
        response_401 = Errors.from_dict(response.text)

        return response_401
    if response.status_code == 403:
        response_403 = Errors.from_dict(response.text)

        return response_403
    if response.status_code == 500:
        response_500 = Errors.from_dict(response.text)

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Errors, HistoryCsvRecords]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    format_type: str,
    limit: Union[Unset, float] = UNSET,
    format_: Union[Unset, str] = UNSET,
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
) -> Response[Union[Errors, HistoryCsvRecords]]:
    r"""Exports client's history records to a file \"history_dump.csv\". This API returns maximum of 50,000
    records. If startTime and endTime is not given, then default time range is the last 24 hours. If the
    no.of records is more than 50,000 API gives error mentioning to reduce the time range which can be
    done using startTime and endTime query params. Also, the time range is 1 day at most. Device type
    INTERFERER and ROGUE_AP are not supported.
    **Supported Columns are**
    tenantid,macaddress,devicetype,campusid,buildingid,floorid,floorhierarchy,coordinatex,coordinatey,so
    urcetimestamp,manufacturer,associated,ssid,username,associatedapmac,computetype,sourcetype,hierarchy
    _id,ipaddress.
    **Non supported Columns w.r.t V1 History are**
    maxdetectedapmac,maxdetectedband,detectingcontrollers,firstactiveat,locatedsinceactivecount,changedo
    n,maxdetectedrssi,associatedaprssi,maxdetectedslot,staticdevice,machashed,policyname,udid,recordtype

    Args:
        format_type (str):
        limit (Union[Unset, float]):
        format_ (Union[Unset, str]):
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
        Response[Union[Errors, HistoryCsvRecords]]
    """

    kwargs = _get_kwargs(
        format_type=format_type,
        limit=limit,
        format_=format_,
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


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    format_type: str,
    limit: Union[Unset, float] = UNSET,
    format_: Union[Unset, str] = UNSET,
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
) -> Optional[Union[Errors, HistoryCsvRecords]]:
    r"""Exports client's history records to a file \"history_dump.csv\". This API returns maximum of 50,000
    records. If startTime and endTime is not given, then default time range is the last 24 hours. If the
    no.of records is more than 50,000 API gives error mentioning to reduce the time range which can be
    done using startTime and endTime query params. Also, the time range is 1 day at most. Device type
    INTERFERER and ROGUE_AP are not supported.
    **Supported Columns are**
    tenantid,macaddress,devicetype,campusid,buildingid,floorid,floorhierarchy,coordinatex,coordinatey,so
    urcetimestamp,manufacturer,associated,ssid,username,associatedapmac,computetype,sourcetype,hierarchy
    _id,ipaddress.
    **Non supported Columns w.r.t V1 History are**
    maxdetectedapmac,maxdetectedband,detectingcontrollers,firstactiveat,locatedsinceactivecount,changedo
    n,maxdetectedrssi,associatedaprssi,maxdetectedslot,staticdevice,machashed,policyname,udid,recordtype

    Args:
        format_type (str):
        limit (Union[Unset, float]):
        format_ (Union[Unset, str]):
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
        Union[Errors, HistoryCsvRecords]
    """

    return sync_detailed(
        client=client,
        format_type=format_type,
        limit=limit,
        format_=format_,
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
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    format_type: str,
    limit: Union[Unset, float] = UNSET,
    format_: Union[Unset, str] = UNSET,
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
) -> Response[Union[Errors, HistoryCsvRecords]]:
    r"""Exports client's history records to a file \"history_dump.csv\". This API returns maximum of 50,000
    records. If startTime and endTime is not given, then default time range is the last 24 hours. If the
    no.of records is more than 50,000 API gives error mentioning to reduce the time range which can be
    done using startTime and endTime query params. Also, the time range is 1 day at most. Device type
    INTERFERER and ROGUE_AP are not supported.
    **Supported Columns are**
    tenantid,macaddress,devicetype,campusid,buildingid,floorid,floorhierarchy,coordinatex,coordinatey,so
    urcetimestamp,manufacturer,associated,ssid,username,associatedapmac,computetype,sourcetype,hierarchy
    _id,ipaddress.
    **Non supported Columns w.r.t V1 History are**
    maxdetectedapmac,maxdetectedband,detectingcontrollers,firstactiveat,locatedsinceactivecount,changedo
    n,maxdetectedrssi,associatedaprssi,maxdetectedslot,staticdevice,machashed,policyname,udid,recordtype

    Args:
        format_type (str):
        limit (Union[Unset, float]):
        format_ (Union[Unset, str]):
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
        Response[Union[Errors, HistoryCsvRecords]]
    """

    kwargs = _get_kwargs(
        format_type=format_type,
        limit=limit,
        format_=format_,
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


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    format_type: str,
    limit: Union[Unset, float] = UNSET,
    format_: Union[Unset, str] = UNSET,
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
) -> Optional[Union[Errors, HistoryCsvRecords]]:
    r"""Exports client's history records to a file \"history_dump.csv\". This API returns maximum of 50,000
    records. If startTime and endTime is not given, then default time range is the last 24 hours. If the
    no.of records is more than 50,000 API gives error mentioning to reduce the time range which can be
    done using startTime and endTime query params. Also, the time range is 1 day at most. Device type
    INTERFERER and ROGUE_AP are not supported.
    **Supported Columns are**
    tenantid,macaddress,devicetype,campusid,buildingid,floorid,floorhierarchy,coordinatex,coordinatey,so
    urcetimestamp,manufacturer,associated,ssid,username,associatedapmac,computetype,sourcetype,hierarchy
    _id,ipaddress.
    **Non supported Columns w.r.t V1 History are**
    maxdetectedapmac,maxdetectedband,detectingcontrollers,firstactiveat,locatedsinceactivecount,changedo
    n,maxdetectedrssi,associatedaprssi,maxdetectedslot,staticdevice,machashed,policyname,udid,recordtype

    Args:
        format_type (str):
        limit (Union[Unset, float]):
        format_ (Union[Unset, str]):
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
        Union[Errors, HistoryCsvRecords]
    """

    return (
        await asyncio_detailed(
            client=client,
            format_type=format_type,
            limit=limit,
            format_=format_,
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
    ).parsed
