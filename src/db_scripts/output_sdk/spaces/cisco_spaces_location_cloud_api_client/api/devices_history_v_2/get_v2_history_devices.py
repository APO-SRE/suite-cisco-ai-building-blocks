from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.mac_address import MacAddress
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
        "url": "/v2/history/devices",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Errors, list["MacAddress"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_history_clients_mac_item_data in _response_200:
            componentsschemas_history_clients_mac_item = MacAddress.from_dict(
                componentsschemas_history_clients_mac_item_data
            )

            response_200.append(componentsschemas_history_clients_mac_item)

        return response_200
    if response.status_code == 400:
        response_400 = Errors.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = Errors.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = Errors.from_dict(response.json())

        return response_403
    if response.status_code == 500:
        response_500 = Errors.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Errors, list["MacAddress"]]]:
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
) -> Response[Union[Errors, list["MacAddress"]]]:
    """Get the list of clients macAddress. If startTime and endTime are not given, all the clients mac
    addresses in the last 1 day will be returned. Device type INTERFERER and ROGUE_AP are not supported.

    Args:
        device_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, list['MacAddress']]]
    """

    kwargs = _get_kwargs(
        device_id=device_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    device_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Errors, list["MacAddress"]]]:
    """Get the list of clients macAddress. If startTime and endTime are not given, all the clients mac
    addresses in the last 1 day will be returned. Device type INTERFERER and ROGUE_AP are not supported.

    Args:
        device_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, list['MacAddress']]
    """

    return sync_detailed(
        client=client,
        device_id=device_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    device_id: Union[Unset, str] = UNSET,
) -> Response[Union[Errors, list["MacAddress"]]]:
    """Get the list of clients macAddress. If startTime and endTime are not given, all the clients mac
    addresses in the last 1 day will be returned. Device type INTERFERER and ROGUE_AP are not supported.

    Args:
        device_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, list['MacAddress']]]
    """

    kwargs = _get_kwargs(
        device_id=device_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    device_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Errors, list["MacAddress"]]]:
    """Get the list of clients macAddress. If startTime and endTime are not given, all the clients mac
    addresses in the last 1 day will be returned. Device type INTERFERER and ROGUE_AP are not supported.

    Args:
        device_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, list['MacAddress']]
    """

    return (
        await asyncio_detailed(
            client=client,
            device_id=device_id,
        )
    ).parsed
