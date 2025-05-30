from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.common_rest_error import CommonRestError
from ...models.state_assertions_response import StateAssertionsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    fabric_id: str,
    device_id: str,
    *,
    state: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["state"] = state

    params["type"] = type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/fabrics/{fabric_id}/devices/{device_id}/assertions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CommonRestError, StateAssertionsResponse]]:
    if response.status_code == 200:
        response_200 = StateAssertionsResponse.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = CommonRestError.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = CommonRestError.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = CommonRestError.from_dict(response.json())

        return response_404
    if response.status_code == 409:
        response_409 = CommonRestError.from_dict(response.json())

        return response_409
    if response.status_code == 429:
        response_429 = CommonRestError.from_dict(response.json())

        return response_429
    if response.status_code == 500:
        response_500 = CommonRestError.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CommonRestError, StateAssertionsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    fabric_id: str,
    device_id: str,
    *,
    client: AuthenticatedClient,
    state: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Response[Union[CommonRestError, StateAssertionsResponse]]:
    """Get the list of assertions of a specific device.

    Args:
        fabric_id (str):
        device_id (str):
        state (Union[Unset, str]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommonRestError, StateAssertionsResponse]]
    """

    kwargs = _get_kwargs(
        fabric_id=fabric_id,
        device_id=device_id,
        state=state,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fabric_id: str,
    device_id: str,
    *,
    client: AuthenticatedClient,
    state: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Optional[Union[CommonRestError, StateAssertionsResponse]]:
    """Get the list of assertions of a specific device.

    Args:
        fabric_id (str):
        device_id (str):
        state (Union[Unset, str]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommonRestError, StateAssertionsResponse]
    """

    return sync_detailed(
        fabric_id=fabric_id,
        device_id=device_id,
        client=client,
        state=state,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    fabric_id: str,
    device_id: str,
    *,
    client: AuthenticatedClient,
    state: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Response[Union[CommonRestError, StateAssertionsResponse]]:
    """Get the list of assertions of a specific device.

    Args:
        fabric_id (str):
        device_id (str):
        state (Union[Unset, str]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommonRestError, StateAssertionsResponse]]
    """

    kwargs = _get_kwargs(
        fabric_id=fabric_id,
        device_id=device_id,
        state=state,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fabric_id: str,
    device_id: str,
    *,
    client: AuthenticatedClient,
    state: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Optional[Union[CommonRestError, StateAssertionsResponse]]:
    """Get the list of assertions of a specific device.

    Args:
        fabric_id (str):
        device_id (str):
        state (Union[Unset, str]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommonRestError, StateAssertionsResponse]
    """

    return (
        await asyncio_detailed(
            fabric_id=fabric_id,
            device_id=device_id,
            client=client,
            state=state,
            type_=type_,
        )
    ).parsed
