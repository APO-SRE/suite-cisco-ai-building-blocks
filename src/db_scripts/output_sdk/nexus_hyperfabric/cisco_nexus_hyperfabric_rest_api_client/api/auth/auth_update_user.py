from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.auth_update_user import AuthUpdateUser
from ...models.common_rest_error import CommonRestError
from ...models.models_user import ModelsUser
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    body: AuthUpdateUser,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/users/{user_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CommonRestError, ModelsUser]]:
    if response.status_code == 200:
        response_200 = ModelsUser.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = CommonRestError.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = CommonRestError.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = CommonRestError.from_dict(response.json())

        return response_403
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
) -> Response[Union[CommonRestError, ModelsUser]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: AuthUpdateUser,
) -> Response[Union[CommonRestError, ModelsUser]]:
    """Update a specific user.

     Update a specific user associated with the organization.

    Args:
        user_id (str):
        body (AuthUpdateUser): Update a specific user.
            Update a specific user associated with the organization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommonRestError, ModelsUser]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: AuthUpdateUser,
) -> Optional[Union[CommonRestError, ModelsUser]]:
    """Update a specific user.

     Update a specific user associated with the organization.

    Args:
        user_id (str):
        body (AuthUpdateUser): Update a specific user.
            Update a specific user associated with the organization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommonRestError, ModelsUser]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: AuthUpdateUser,
) -> Response[Union[CommonRestError, ModelsUser]]:
    """Update a specific user.

     Update a specific user associated with the organization.

    Args:
        user_id (str):
        body (AuthUpdateUser): Update a specific user.
            Update a specific user associated with the organization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommonRestError, ModelsUser]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: AuthUpdateUser,
) -> Optional[Union[CommonRestError, ModelsUser]]:
    """Update a specific user.

     Update a specific user associated with the organization.

    Args:
        user_id (str):
        body (AuthUpdateUser): Update a specific user.
            Update a specific user associated with the organization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommonRestError, ModelsUser]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
