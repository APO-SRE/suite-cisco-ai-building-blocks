from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.auth_get_users_roles import AuthGetUsersRoles
from ...models.auth_users_response import AuthUsersResponse
from ...models.common_rest_error import CommonRestError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    emails: Union[Unset, str] = UNSET,
    enabled: Union[Unset, bool] = UNSET,
    roles: Union[Unset, AuthGetUsersRoles] = AuthGetUsersRoles.ADMIN,
    include_metadata: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["emails"] = emails

    params["enabled"] = enabled

    json_roles: Union[Unset, str] = UNSET
    if not isinstance(roles, Unset):
        json_roles = roles.value

    params["roles"] = json_roles

    params["includeMetadata"] = include_metadata

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AuthUsersResponse, CommonRestError]]:
    if response.status_code == 200:
        response_200 = AuthUsersResponse.from_dict(response.json())

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
) -> Response[Union[AuthUsersResponse, CommonRestError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    emails: Union[Unset, str] = UNSET,
    enabled: Union[Unset, bool] = UNSET,
    roles: Union[Unset, AuthGetUsersRoles] = AuthGetUsersRoles.ADMIN,
    include_metadata: Union[Unset, bool] = UNSET,
) -> Response[Union[AuthUsersResponse, CommonRestError]]:
    """Get a list of users.

     Get the list of users associated with the organization.

    Args:
        emails (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        roles (Union[Unset, AuthGetUsersRoles]): An enum value, select either string or integer
            Default: AuthGetUsersRoles.ADMIN.
        include_metadata (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AuthUsersResponse, CommonRestError]]
    """

    kwargs = _get_kwargs(
        emails=emails,
        enabled=enabled,
        roles=roles,
        include_metadata=include_metadata,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    emails: Union[Unset, str] = UNSET,
    enabled: Union[Unset, bool] = UNSET,
    roles: Union[Unset, AuthGetUsersRoles] = AuthGetUsersRoles.ADMIN,
    include_metadata: Union[Unset, bool] = UNSET,
) -> Optional[Union[AuthUsersResponse, CommonRestError]]:
    """Get a list of users.

     Get the list of users associated with the organization.

    Args:
        emails (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        roles (Union[Unset, AuthGetUsersRoles]): An enum value, select either string or integer
            Default: AuthGetUsersRoles.ADMIN.
        include_metadata (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AuthUsersResponse, CommonRestError]
    """

    return sync_detailed(
        client=client,
        emails=emails,
        enabled=enabled,
        roles=roles,
        include_metadata=include_metadata,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    emails: Union[Unset, str] = UNSET,
    enabled: Union[Unset, bool] = UNSET,
    roles: Union[Unset, AuthGetUsersRoles] = AuthGetUsersRoles.ADMIN,
    include_metadata: Union[Unset, bool] = UNSET,
) -> Response[Union[AuthUsersResponse, CommonRestError]]:
    """Get a list of users.

     Get the list of users associated with the organization.

    Args:
        emails (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        roles (Union[Unset, AuthGetUsersRoles]): An enum value, select either string or integer
            Default: AuthGetUsersRoles.ADMIN.
        include_metadata (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AuthUsersResponse, CommonRestError]]
    """

    kwargs = _get_kwargs(
        emails=emails,
        enabled=enabled,
        roles=roles,
        include_metadata=include_metadata,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    emails: Union[Unset, str] = UNSET,
    enabled: Union[Unset, bool] = UNSET,
    roles: Union[Unset, AuthGetUsersRoles] = AuthGetUsersRoles.ADMIN,
    include_metadata: Union[Unset, bool] = UNSET,
) -> Optional[Union[AuthUsersResponse, CommonRestError]]:
    """Get a list of users.

     Get the list of users associated with the organization.

    Args:
        emails (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        roles (Union[Unset, AuthGetUsersRoles]): An enum value, select either string or integer
            Default: AuthGetUsersRoles.ADMIN.
        include_metadata (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AuthUsersResponse, CommonRestError]
    """

    return (
        await asyncio_detailed(
            client=client,
            emails=emails,
            enabled=enabled,
            roles=roles,
            include_metadata=include_metadata,
        )
    ).parsed
