from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.mac_and_details import MacAndDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    device_id_path: str,
    *,
    device_id_query: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["deviceId"] = device_id_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/history/device/{device_id_path}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Errors, list["MacAndDetails"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_history_clients_item_data in _response_200:
            componentsschemas_history_clients_item = MacAndDetails.from_dict(
                componentsschemas_history_clients_item_data
            )

            response_200.append(componentsschemas_history_clients_item)

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
) -> Response[Union[Errors, list["MacAndDetails"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    device_id_path: str,
    *,
    client: Union[AuthenticatedClient, Client],
    device_id_query: Union[Unset, str] = UNSET,
) -> Response[Union[Errors, list["MacAndDetails"]]]:
    """Get the given device's history details. The pagination is provided. If startTime and endTime is not
    given, then the default time range is the last 24 hours. Also, the time range is 1 day at most.
    Device type INTERFERER and ROGUE_AP are not supported.

    Args:
        device_id_path (str):
        device_id_query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, list['MacAndDetails']]]
    """

    kwargs = _get_kwargs(
        device_id_path=device_id_path,
        device_id_query=device_id_query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    device_id_path: str,
    *,
    client: Union[AuthenticatedClient, Client],
    device_id_query: Union[Unset, str] = UNSET,
) -> Optional[Union[Errors, list["MacAndDetails"]]]:
    """Get the given device's history details. The pagination is provided. If startTime and endTime is not
    given, then the default time range is the last 24 hours. Also, the time range is 1 day at most.
    Device type INTERFERER and ROGUE_AP are not supported.

    Args:
        device_id_path (str):
        device_id_query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, list['MacAndDetails']]
    """

    return sync_detailed(
        device_id_path=device_id_path,
        client=client,
        device_id_query=device_id_query,
    ).parsed


async def asyncio_detailed(
    device_id_path: str,
    *,
    client: Union[AuthenticatedClient, Client],
    device_id_query: Union[Unset, str] = UNSET,
) -> Response[Union[Errors, list["MacAndDetails"]]]:
    """Get the given device's history details. The pagination is provided. If startTime and endTime is not
    given, then the default time range is the last 24 hours. Also, the time range is 1 day at most.
    Device type INTERFERER and ROGUE_AP are not supported.

    Args:
        device_id_path (str):
        device_id_query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, list['MacAndDetails']]]
    """

    kwargs = _get_kwargs(
        device_id_path=device_id_path,
        device_id_query=device_id_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    device_id_path: str,
    *,
    client: Union[AuthenticatedClient, Client],
    device_id_query: Union[Unset, str] = UNSET,
) -> Optional[Union[Errors, list["MacAndDetails"]]]:
    """Get the given device's history details. The pagination is provided. If startTime and endTime is not
    given, then the default time range is the last 24 hours. Also, the time range is 1 day at most.
    Device type INTERFERER and ROGUE_AP are not supported.

    Args:
        device_id_path (str):
        device_id_query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, list['MacAndDetails']]
    """

    return (
        await asyncio_detailed(
            device_id_path=device_id_path,
            client=client,
            device_id_query=device_id_query,
        )
    ).parsed
