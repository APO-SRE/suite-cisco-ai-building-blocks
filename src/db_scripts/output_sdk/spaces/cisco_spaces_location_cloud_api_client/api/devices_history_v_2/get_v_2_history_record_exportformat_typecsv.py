from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.history_csv_records import HistoryCsvRecords
from ...types import UNSET, Response


def _get_kwargs(
    *,
    format_type: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["formatType"] = format_type

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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, HistoryCsvRecords]]
    """

    kwargs = _get_kwargs(
        format_type=format_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    format_type: str,
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, HistoryCsvRecords]
    """

    return sync_detailed(
        client=client,
        format_type=format_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    format_type: str,
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, HistoryCsvRecords]]
    """

    kwargs = _get_kwargs(
        format_type=format_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    format_type: str,
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
        )
    ).parsed
