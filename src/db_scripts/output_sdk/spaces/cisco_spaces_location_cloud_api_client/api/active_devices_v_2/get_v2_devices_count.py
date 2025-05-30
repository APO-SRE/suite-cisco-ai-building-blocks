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
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["deviceType"] = device_type

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
) -> Response[Union[ClientCountResponse, Errors]]:
    """Retrieve the active devices count. The API supports searching by a variety of parameters. If no
    parameters are given, the count of all active devices are returned.

    Args:
        device_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientCountResponse, Errors]]
    """

    kwargs = _get_kwargs(
        device_type=device_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    device_type: Union[Unset, str] = UNSET,
) -> Optional[Union[ClientCountResponse, Errors]]:
    """Retrieve the active devices count. The API supports searching by a variety of parameters. If no
    parameters are given, the count of all active devices are returned.

    Args:
        device_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClientCountResponse, Errors]
    """

    return sync_detailed(
        client=client,
        device_type=device_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    device_type: Union[Unset, str] = UNSET,
) -> Response[Union[ClientCountResponse, Errors]]:
    """Retrieve the active devices count. The API supports searching by a variety of parameters. If no
    parameters are given, the count of all active devices are returned.

    Args:
        device_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClientCountResponse, Errors]]
    """

    kwargs = _get_kwargs(
        device_type=device_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    device_type: Union[Unset, str] = UNSET,
) -> Optional[Union[ClientCountResponse, Errors]]:
    """Retrieve the active devices count. The API supports searching by a variety of parameters. If no
    parameters are given, the count of all active devices are returned.

    Args:
        device_type (Union[Unset, str]):

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
        )
    ).parsed
