from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    device_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["deviceId"] = device_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2//history/record/export",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None
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
) -> Response[Any]:
    """Exports client's history records in gzipped format. This API returns maximum of 5million records. If
    startTime and endTime is not given, then default time range is the last 24 hours. If the no.of
    records is more than 5million, API gives error mentioning to reduce the time range which can be done
    using startTime and endTime query params. Also, the time range is 1 day at most. Note: The API takes
    time(up to 2mins) because of the large data amount, please be patient. Device type INTERFERER and
    ROGUE_AP are not supported.
    **Supported Columns are**
    tenantid,macaddress,devicetype,campusid,buildingid,floorid,floorhierarchy,coordinatex,coordinatey,so
    urcetimestamp,manufacturer,associated,ssid,username,associatedapmac,computetype,sourcetype,hierarchy
    _id,ipaddress.
    **Non supported Columns w.r.t V1 History are**
    maxdetectedapmac,maxdetectedband,detectingcontrollers,firstactiveat,locatedsinceactivecount,changedo
    n,maxdetectedrssi,associatedaprssi,maxdetectedslot,staticdevice,machashed,policyname,udid,recordtype

    Args:
        device_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        device_id=device_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    device_id: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Exports client's history records in gzipped format. This API returns maximum of 5million records. If
    startTime and endTime is not given, then default time range is the last 24 hours. If the no.of
    records is more than 5million, API gives error mentioning to reduce the time range which can be done
    using startTime and endTime query params. Also, the time range is 1 day at most. Note: The API takes
    time(up to 2mins) because of the large data amount, please be patient. Device type INTERFERER and
    ROGUE_AP are not supported.
    **Supported Columns are**
    tenantid,macaddress,devicetype,campusid,buildingid,floorid,floorhierarchy,coordinatex,coordinatey,so
    urcetimestamp,manufacturer,associated,ssid,username,associatedapmac,computetype,sourcetype,hierarchy
    _id,ipaddress.
    **Non supported Columns w.r.t V1 History are**
    maxdetectedapmac,maxdetectedband,detectingcontrollers,firstactiveat,locatedsinceactivecount,changedo
    n,maxdetectedrssi,associatedaprssi,maxdetectedslot,staticdevice,machashed,policyname,udid,recordtype

    Args:
        device_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        device_id=device_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
