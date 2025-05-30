from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors import Errors
from ...models.v2_location_device_results import V2LocationDeviceResults
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
        "url": "/v2/devices",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Errors, V2LocationDeviceResults]]:
    if response.status_code == 200:
        response_200 = V2LocationDeviceResults.from_dict(response.json())

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
) -> Response[Union[Errors, V2LocationDeviceResults]]:
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
) -> Response[Union[Errors, V2LocationDeviceResults]]:
    """This API supports searching by a variety of parameters. If no parameters are given, all active
    devices are returned with pagination. The default page number is 1, default number of items per page
    is 1000.

    Args:
        device_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, V2LocationDeviceResults]]
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
) -> Optional[Union[Errors, V2LocationDeviceResults]]:
    """This API supports searching by a variety of parameters. If no parameters are given, all active
    devices are returned with pagination. The default page number is 1, default number of items per page
    is 1000.

    Args:
        device_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, V2LocationDeviceResults]
    """

    return sync_detailed(
        client=client,
        device_type=device_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    device_type: Union[Unset, str] = UNSET,
) -> Response[Union[Errors, V2LocationDeviceResults]]:
    """This API supports searching by a variety of parameters. If no parameters are given, all active
    devices are returned with pagination. The default page number is 1, default number of items per page
    is 1000.

    Args:
        device_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Errors, V2LocationDeviceResults]]
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
) -> Optional[Union[Errors, V2LocationDeviceResults]]:
    """This API supports searching by a variety of parameters. If no parameters are given, all active
    devices are returned with pagination. The default page number is 1, default number of items per page
    is 1000.

    Args:
        device_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Errors, V2LocationDeviceResults]
    """

    return (
        await asyncio_detailed(
            client=client,
            device_type=device_type,
        )
    ).parsed
